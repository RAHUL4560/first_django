from django.contrib import admin
from .models import Image_details
from .models import LoadedImagedata

# Register your models here.
admin.site.register(Image_details)
admin.site.register(LoadedImagedata)
