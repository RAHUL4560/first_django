from django.db import models
import jsonfield

# Create your models here.
class Image_details(models.Model):
 radio = (
        ('left', 'Left'),
        ('right', 'Right'),)
 radio2 = (
        ('Poor Quality', 'Poor Quality'),
        ('Ungradable', 'Ungradable'),
        ('Gradable','Gradable'),)
 radio3 = (
        ('Disc boundary', 'Disc boundary'),
        ('Cup boundary', 'Cup boundary'),)
 radio4 = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),)
 radio5 = [
             ('Diabetic Retinopathy (DR)', 'Diabetic Retinopathy (DR)'),
             (' Glaucoma', '  Glaucoma'),
             ('Others','Others'),]

 CDR= models.FloatField(default=0.1)
 optradio = models.CharField(max_length = 20, choices = radio, default='Left')
 optradio1 = models.CharField(max_length = 20, choices = radio2, default='Poor Quality')
 optradio2 = models.CharField(max_length = 20, choices = radio3, default='Disc boundary')
 optradio3 = models.CharField(max_length = 20, choices = radio4, default='Present')
 optradio4 = models.CharField(max_length = 20, choices = radio4, default='Present')
 optradio5 = models.CharField(max_length = 20, choices = radio4, default='Present')
 optradio6 = models.CharField(max_length = 20, choices = radio4, default='Present')
 optradio7 = models.CharField(max_length = 20, choices = radio4, default='Present')
 optradio8 = models.CharField(max_length = 100, choices = radio5)
class LoadedImagedata(models.Model):
    """LoadedImagedata"""

    content = jsonfield.JSONField()
