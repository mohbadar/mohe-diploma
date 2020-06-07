<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use \Hijri;
use \Carbon\Carbon;
use \App\Appointment;
use \App\HijriMonth;
class Center extends Model
{
    protected $casts=['appointments'=>'array'];

    public function getAvailableAppointments(){
        $totalTries = 0;
        $today                  = Carbon::now()->addDays(1);
        $appointments=[];
            while(count($appointments) !=15 && $totalTries < 1000){
                try{
                    $available = $this->getAppointmentsByDay($today);
                    $hijriToday = \Hijri::fromCarbon($today);
                    if($available){
                        $key = $hijriToday->format('l')." ".$hijriToday->format('d')." ".HijriMonth::getMonthName($hijriToday->format('m'))." ".$hijriToday->format('Y');
                        $appointments[]=['month'=>$key,'times'=>$available];
                       
                    }
                    $today = $today->addDay();
                
                   
                }catch(\Exception $e){
                  
                }
                $totalTries ++;
            }
      

        return $appointments;

    }

    public function getAppointmentsByDay($date){
        if( $this->isPublicHoliday($date) ){
            return false;
        }
        $days        = isset($this->appointments['data']['days']) ? $this->appointments['data']['days']:[];
        $appointments=[];
        foreach($days as $d):
            if($d['active'] && $date->format('N') == $d['value']){
                foreach($d['slots'] as $t):
                    
                    $availableTimes = Center::getAvailableTimes($date,$t,$this->id);
                    if($availableTimes){
                        $appointments[]=$availableTimes;
                    }
                    
                endforeach;
               
            }
        endforeach;

        return count($appointments) > 0 ? $appointments :false;

    }
    public static function getAvailableTimes($date,$slot,$center_id){
        $hijriDate= \Hijri::fromCarbon($date);
        $taken_appointments = Appointment::where('appointment_date',$hijriDate->format('Y-m-d'))
            ->where('start_time',$slot['start'])
            ->where('center_id',$center_id)
            ->where('end_time',$slot['end'])->count();
        $available_appointments = $slot['number_of_appointments'] - $taken_appointments;
        if($available_appointments < 1){
            return false;
        }

  
        return [
                'appointment_date_day_label'=>$hijriDate->format('l'),
                'appointment_date_day'=>$hijriDate->format('d'),
                'appointment_date_month'=>$hijriDate->format('m'),
                'appointment_date_month_label'=>\App\HijriMonth::getMonthName($hijriDate->format('m')),
                'appointment_date_year'=>$hijriDate->format('Y'),
                'appointment_date'=>$hijriDate->format('Y-m-d'),
                'number_of_appointments'=>$available_appointments,
                'start'=>$slot['start'],
                'start_label'=>Appointment::formatTime($slot['start']),
                'label'=>Appointment::formatTime($slot['start'])." الی ".Appointment::formatTime($slot['end']),
                'end'=>$slot['end'],
                'end_label'=>Appointment::formatTime($slot['end'])
            
        ];

    }

    public function isPublicHoliday(Carbon $date){
        $public_holidays = $this->getPublicHolidays();
        foreach($public_holidays as $p){
            if( $date->isSameDay($p) ){
                return true;
            }
        }

        return false;
    }
    public function getPublicHolidays(){
        $public_holidays = [];
        $holidays        = isset($this->appointments['data']['public_holidays'])?$this->appointments['data']['public_holidays']:[];
        foreach($holidays as $h):
            $d= new Hijri($h['year'], $h['month'], $h['day']);
            $public_holidays[]=$d->toCarbon();
        endforeach;
        return $public_holidays;
    }

    public function getAvailableSlots($date,$start,$end){
        $appointments = $this->getAppointmentsByDay($date);
        if($appointments == false){
            return 0;
        }
        foreach($appointments as $a):
            if($a['start'] == $start && $a['end'] == $end){
                return $a['number_of_appointments'];
            }
        endforeach;
        return 0;
    }

    public function address(){
        return $this->name;
        //." ".$this->village." ".$this->town." ".$this->province." ".\App\Village::getCountryNameById($this->country);
    }


    public static function isIpAllowed($ip){
       return \App\Center::where('ip',$ip)->exists();
    }

    
}
