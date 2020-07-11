from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import datetime
from django.conf import settings
import hashlib
# Create your models here.

GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)

DEGREE = (
    ("BACHELOR", "BACHELOR"),
    ("MASTER", "MASTER"),
    ("PHD", "PHD")
)

class University(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=128 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=128 )
    user = models.ForeignKey(User, editable=False, null=True, blank=True, related_name ="university_user", verbose_name="User", on_delete=models.CASCADE)
    province = models.CharField("province", max_length=50)

    def __str__(self):
        return  "{name}-{code}".format( name = self.name, code=self.code)


class Faculty(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=32 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=32 )
    user = models.ForeignKey(User, editable=False, null=True, blank=True, related_name ="faculty_user", verbose_name="User", on_delete=models.CASCADE)
    university = models.ForeignKey(to=University, related_name ="faculty_university", on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return "{university}-{name}-{code}".format(university=self.university.name, name = self.name, code=self.code)

class Department(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=255 )
    user = models.ForeignKey(User, editable=False, null=True, blank=True, related_name ="department_user", verbose_name="User", on_delete=models.CASCADE)
    university = models.ForeignKey(to=University, related_name ="department_university", on_delete=models.CASCADE, blank=True, null=True, default=1)
    faculty = models.ForeignKey(to=Faculty , related_name ="department_faculty", on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return "{university}-{faculty}-{name}-{code}".format(university=self.university.name, faculty=self.faculty.name, name = self.name, code=self.code)



CERTIFICATE_STATUS =(
    ("SUBMITTED", "SUBMITTED"),
    ("POSTED", "POSTED"),
    ("MAPPED", "MAPPED")
)

class Certificate(models.Model):
    firstname = models.CharField(name="firstname", max_length=255,help_text="First Name")
    lastname = models.CharField(name="lastname", max_length=255,help_text="Last Name")
    fathername =  models.CharField(name="fathername", max_length=255,help_text="Father Name")
    dob = models.DateField(name="dob",help_text="Birth of Date", verbose_name="Date of Birth")
    user = models.ForeignKey(User, editable=False, null=True, blank=True, related_name ="certificate_user", verbose_name="User", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name ="certificate_department", verbose_name="Department", on_delete=models.CASCADE)
    graduation_year = models.IntegerField(name="graduation_year",help_text="Graduation Year")
    slug = models.SlugField(max_length = 250, null = True, blank = True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    qrtext  = models.TextField(name="qrtext", editable=False,help_text="QR Code")
    degree_title= models.CharField(name="degree_title", default='BACHELOR', choices=DEGREE ,help_text="Degree Title", max_length=255)
    gender = models.CharField(choices= GENDER,max_length=6, default="MALE")
    certificate_status = models.CharField(name='certificate_status',choices= CERTIFICATE_STATUS,max_length=32, default="SUBMITTED")
    picture = models.ImageField(name="picture", null=True, blank=True)

    def save(self, *args, **kwargs):
        qrcontent = "{firstname}:{lastname}:{fathername}:{dob}:{university}:{faculty}:{department}:{graduation_year}:{degree_title}".format(firstname=self.firstname, lastname=self.lastname, fathername=self.fathername, dob=self.dob, university=self.department.university.code, faculty=self.department.faculty.code, department=self.department.code, graduation_year=self.graduation_year, degree_title=self.degree_title).encode('utf-8')
        self.qrtext = hashlib.sha224(qrcontent).hexdigest()
        self.slug = slugify(self.qrtext)
        super(Certificate, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return  "{university}-{faculty}-{department}-{firstname}-{lastname}-{graduation_year}".format(university = self.department.university.code ,faculty = self.department.faculty.code,department = self.department.code, firstname = self.firstname,lastname = self.lastname, graduation_year = self.graduation_year)

    class Meta:
        ordering = ['-created_at']
        permissions = (
            ("can_register_certificate", "Can Register a New Certificate"),
            ("can_view_ownfaculty_certificates", "Can View Own Faculty Certificate")
        )

class BlankDiploma(models.Model):
    barcode = models.CharField(name="barcode", max_length=255, unique=True, db_index=True,help_text="Barcode")
    status = models.BooleanField(name="status", default=False)
    university = models.ForeignKey(University, editable=False, related_name ="blank_diploma_university", verbose_name="University", on_delete=models.CASCADE)
    user = models.ForeignKey(User, editable=False, null=True, blank=True, related_name ="blank_diploma_user", verbose_name="User", on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificate, null=True, blank=True, related_name ="blank_diploma_certificate", verbose_name="Certificate", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return  "{barcode}".format( barcode = self.barcode)

    class Meta:
        ordering = ['-created_at']



class UniversityDiplomaDistribution(models.Model):
    university = models.ForeignKey(University, related_name ="diploma_distribution_university",verbose_name="University", on_delete=models.CASCADE)
    number = models.IntegerField(name="number",verbose_name="Diploma Number" )
    user = models.ForeignKey(User, editable=False, null=True, blank=True, related_name ="university_distribution_user", verbose_name="User", on_delete=models.CASCADE) 
    date = models.DateField(name="date", auto_now=False, auto_now_add=False)
    last_no = models.CharField(max_length=500, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)


    def save(self, *args, **kwargs):
        last_no = BlankDiploma.objects.filter(university=self.university.id).order_by('id').last()
        if not last_no:
            index = 10000
            count = self.number + 10000
            while(index < count ):
                index = index + 1
                barcode = "{university}-{index}".format(university = self.university.code , index = index)
                print(barcode)
                item = BlankDiploma()
                item.barcode = barcode
                item.university = self.university
                item.status = False
                item.save()
        else:
            index = int(last_no.barcode.split(str(self.university.code) + "-")[-1])
            print("lastindex", index)
            count = self.number + index
            print("Count ", count)
            while(index < count):
                index = index + 1
                barcode = "{university}-{index}".format(university = self.university.code , index = index)

                item = BlankDiploma()
                item.barcode = barcode
                item.university = self.university
                item.status = False
                item.save()

        super(UniversityDiplomaDistribution, self).save(*args, **kwargs) # Call the real save() method


    def __str__(self):
        return  "{university}-{number}-{last_no}".format(university = self.university.name , number = self.number, last_no=self.last_no)


class Diploma(models.Model):
    number = models.CharField(name="number",verbose_name="Number", unique=True, db_index=True,max_length=255 )
    university = models.ForeignKey(to=University, related_name ="diploma_university",  on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.university.name +" - "+ self.faculty.name +" - "+ self.name + " - " + self.code



APPLY_LEVEL  = (
    ("SYSTEM", "SYSTEM"),
    ("UNIVERSITY", "UNIVERSITY"),
    ("FACULTY", "FACULTY")
)

class UserFacultyRelation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    apply_level= models.CharField(name="apply_level", default='FACULTY', choices=APPLY_LEVEL ,help_text="User Apply Level", max_length=255)
    university = models.ForeignKey(to=University , related_name ="user_university_relation", on_delete=models.CASCADE, blank=True, null=True) 
    faculty = models.ForeignKey(to=Faculty , related_name ="user_faculty_relation", on_delete=models.CASCADE, blank=True, null=True)


