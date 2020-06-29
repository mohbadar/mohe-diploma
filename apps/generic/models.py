from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import datetime
from django.conf import settings
# Create your models here.

GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)
class Contact(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    email = models.EmailField(name="email", max_length=255, unique=True, db_index=True,verbose_name="Email")
    phone = models.CharField(name="phone", max_length=13, unique=True, db_index=True,verbose_name="Phone")
    message = models.TextField(name="message",verbose_name="Message")

    def __str__(self):
        return self.name +" - "+ self.email +" - "+ self.message

class University(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=32 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=32 )
    province = models.CharField("province", max_length=50)

    def __str__(self):
        return self.name +" - "+ self.code 


class Faculty(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=32 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=32 )
    university = models.ForeignKey(to=University, related_name ="faculty_university", on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.university.name +" - "+ self.name +" - "+ self.code


class Department(models.Model):
    name = models.CharField(name="name",verbose_name="Name", unique=True, db_index=True,max_length=255 )
    code = models.CharField(name="code",verbose_name="code", unique=True, db_index=True,max_length=255 )
    university = models.ForeignKey(to=University, related_name ="department_university", on_delete=models.CASCADE, blank=True, null=True, default=1)
    faculty = models.ForeignKey(to=Faculty , related_name ="department_faculty", on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.university.name +" - "+ self.faculty.name +" - "+ self.name + " - " + self.code


class BlankDiploma(models.Model):
    barcode = models.CharField(name="barcode", max_length=255, unique=True, db_index=True,help_text="Barcode")
    status = models.BooleanField(name="status", default=False)
    university = models.ForeignKey(University, related_name ="blank_diploma_university", verbose_name="University", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return  "{barcode}".format( barcode = self.barcode)

    class Meta:
        ordering = ['-created_at']


class Certificate(models.Model):
    firstname = models.CharField(name="firstname", max_length=255,help_text="First Name")
    lastname = models.CharField(name="lastname", max_length=255,help_text="Last Name")
    fathername =  models.CharField(name="fathername", max_length=255,help_text="Father Name")
    birth_year = models.IntegerField(name="birth_year",help_text="Birth Year")
    university = models.ForeignKey(University, related_name ="certificate_university", verbose_name="University", on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, related_name ="certificate_faculty", verbose_name="Faculty", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name ="certificate_department", verbose_name="Department", on_delete=models.CASCADE)
    graduation_year = models.IntegerField(name="graduation_year", unique=True, db_index=True,help_text="Graduation Year")
    slug = models.SlugField(max_length = 250, null = True, blank = True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    qrtext  = models.TextField(name="qrtext", editable=False,help_text="QR Code")
    degree_title= models.CharField(name="degree_title",help_text="Degree Title", max_length=255)
    gender = models.CharField(choices= GENDER,max_length=6, default="MALE")
    picture = models.ImageField(name="picture", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname)
        super(Certificate, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return  "{university}-{faculty}-{department}-{firstname}-{lastname}-{graduation_year}".format(university = self.university.code ,faculty = self.faculty.code,department = self.department.code, firstname = self.firstname,lastname = self.lastname, graduation_year = self.graduation_year)

    class Meta:
        ordering = ['-created_at']
        permissions = (
            ("can_register_certificate", "Can Register a New Certificate"),
            ("can_view_ownfaculty_certificates", "Can View Own Faculty Certificate")
        )


class UniversityDiplomaDistribution(models.Model):
    university = models.ForeignKey(University, related_name ="diploma_distribution_university",verbose_name="University", on_delete=models.CASCADE)
    number = models.IntegerField(name="number",verbose_name="Diploma Number" )
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


class UserFacultyRelation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    university = models.OneToOneField(University,
        on_delete=models.CASCADE,
        related_name='user_faculty_relation_university'
    )
    faculty = models.OneToOneField(Faculty,
        on_delete=models.CASCADE,
        related_name='user_faculty_relation_faculty',
    )


