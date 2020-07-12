# Generated by Django 2.2.10 on 2020-07-12 09:55

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CDR', models.FloatField(default=0.1)),
                ('optradio', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default='Left', max_length=20)),
                ('optradio1', models.CharField(choices=[('Poor Quality', 'Poor Quality'), ('Ungradable', 'Ungradable'), ('Gradable', 'Gradable')], default='Poor Quality', max_length=20)),
                ('optradio2', models.CharField(choices=[('Disc boundary', 'Disc boundary'), ('Cup boundary', 'Cup boundary')], default='Disc boundary', max_length=20)),
                ('optradio3', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=20)),
                ('optradio4', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=20)),
                ('optradio5', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=20)),
                ('optradio6', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=20)),
                ('optradio7', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=20)),
                ('optradio8', models.CharField(choices=[('Diabetic Retinopathy (DR)', 'Diabetic Retinopathy (DR)'), (' Glaucoma', '  Glaucoma'), ('Others', 'Others')], default='Diabetic Retinopathy (DR)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoadedImagedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', jsonfield.fields.JSONField()),
            ],
        ),
    ]
