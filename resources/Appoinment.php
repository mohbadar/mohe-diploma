<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use \Hijri;
use App\Center;
class Appointment extends Model
{
   

    public function isAvailable(){
        $date      = explode("-",$this->appointment_date);
        if( count($date) != 3){
            return false;
        }
        $year   = $date[0];
        $month  = $date[1];
        $day    = $date[2];
        $date   = new \Hijri($year,$month,$day);
        $center = \App\Center::where('id',$this->center_id)->first();
        if(!$center){
            return false;
        }
        return $center->getAvailableSlots($date->toCarbon(),$this->start_time,$this->end_time) > 0 ? true : false;
    }

    public function getStartTime(){
        return Appointment::formatTime($this->start_time);
    }
    public function getEndTime(){
        return Appointment::formatTime($this->end_time);
    }

    public function getDateTime(){
        return $this->appointment_date." ".$this->getStartTime()." الی ". $this->getEndTime();
    }
    public function center(){
        return $this->belongsTo(\App\Center::class);
    }
    public function address(){
        $center = $this->center()->first();
        if(!$center){
            return '';
        }

        return $center->address();
    }

    public function getCurrentQueueNo(){
        $date = \Hijri::fromFormat('Y-m-d',$this->appointment_date);
        $lastAppointment = Appointment::where('appointment_date',$date->format('Y-m-d'))->where('center_id',$this->center_id)->orderBy('queue_no','desc')->first();
        if($lastAppointment){
            return $lastAppointment->queue_no+1;
        }
        return 1;
    }

    public static function getAppointments($user,$formsTable,$center_id=false,$status=false){
        $appointments= Appointment::leftJoin($formsTable,'appointments.family_form_reference_no',$formsTable.".family_form_reference_no");
        
        if($formsTable == 'individualforms'){
            $appointments= $appointments->where('apply_for_new_id','بلی');
        }

        if($status!==false){
            $appointments->where('status',$status);
        }

        if($center_id){
            $appointments->where('appointments.center_id',$center_id);
        }
        
        $appointments=$appointments->selectRaw('count(appointment_date) as total_individual,count(distinct(appointments.family_form_reference_no)) as total_family,appointment_date,year(appointment_date) as y,month(appointment_date) as m, day(appointment_date) as d')
        ->groupBy('appointment_date')
        ->orderBy('appointment_date','asc')->get();
        
        $result=[];
        foreach( Appointment::groupAppointmentDates($appointments) as $year=>$months):   
            $years=['year'=>$year,'months'=>[],'open'=>false];
            foreach($months as $month=>$days):
                $monthName = \App\HijriMonth::getMonthName($month);
                $years['months'][]=['value'=>$month,'month'=>$monthName,'days'=>$days,'open'=>false];
            endforeach;
            $result[]=$years;
        endforeach;

        return $result;
        
    }


    private static function groupAppointmentDates($appointments){
        $result=[];
        foreach($appointments as $key=>$a):
        
            $result[$a->y][$a->m][]=[
                'total_individual'=>$a->total_individual,
                'total_family'=>$a->total_family,
                'value'=>$a->appointment_date,
                'y'=>$a->y,
                'm'=>$a->m,
                'd'=>$a->d,
          

            ];
                   
        endforeach;
        return $result;
    }

    
    public static function getAppointmentDateByReferenceNo($reference_no){
        $i=\DB::table('familyapplications')->where('reference_no',$reference_no)->first();
        if(!$i){
            return '';
        }
       

        return $i->appointment_date;
    }
}
