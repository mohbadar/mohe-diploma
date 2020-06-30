# Generated by Django 3.0.7 on 2020-06-30 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('phone', models.CharField(db_index=True, max_length=13, unique=True, verbose_name='Phone')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Name')),
                ('code', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Name')),
                ('code', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='code')),
                ('province', models.CharField(max_length=50, verbose_name='province')),
            ],
        ),
        migrations.CreateModel(
            name='UserFacultyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_faculty_relation_faculty', to='generic.Faculty')),
                ('university', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_faculty_relation_university', to='generic.University')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityDiplomaDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Diploma Number')),
                ('date', models.DateField()),
                ('last_no', models.CharField(blank=True, editable=False, max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diploma_distribution_university', to='generic.University', verbose_name='University')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_university', to='generic.University'),
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Number')),
                ('university', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diploma_university', to='generic.University')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('code', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='code')),
                ('faculty', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_faculty', to='generic.Faculty')),
                ('university', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_university', to='generic.University')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='First Name', max_length=255)),
                ('lastname', models.CharField(help_text='Last Name', max_length=255)),
                ('fathername', models.CharField(help_text='Father Name', max_length=255)),
                ('birth_year', models.IntegerField(help_text='Birth Year')),
                ('graduation_year', models.IntegerField(help_text='Graduation Year', max_length=4)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=250, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('qrtext', models.TextField(editable=False, help_text='QR Code')),
                ('degree_title', models.CharField(choices=[('BACHELOR', 'BACHELOR'), ('MASTER', 'MASTER'), ('PHD', 'PHD')], help_text='Degree Title', max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=6)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_department', to='generic.Department', verbose_name='Department')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-created_at'],
                'permissions': (('can_register_certificate', 'Can Register a New Certificate'), ('can_view_ownfaculty_certificates', 'Can View Own Faculty Certificate')),
            },
        ),
        migrations.CreateModel(
            name='BlankDiploma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(db_index=True, help_text='Barcode', max_length=255, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blank_diploma_university', to='generic.University', verbose_name='University')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
