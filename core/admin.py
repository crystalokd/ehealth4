from django.contrib import admin
from .models import User, Profile, Appointment
# Register your models here.
admin.site.register(User)
admin.site.register(Appointment)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['image','Email','Stomach_ach', 'Diarrheal', 'Injuries', 'Head_ache', 'Cough']
    list_filter=['Stomach_ach', 'Diarrheal', 'Injuries', 'Head_ache', 'Cough']
    search_fields=['name']

admin.site.register(Profile , ProfileAdmin)
