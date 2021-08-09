# type:ignore
from django.contrib import admin
from .models import Profile,Patient,PatientInput,Doctor,DoctorsInput,ContactTracing,User

admin.site.register(Profile)
admin.site.register(PatientInput)
admin.site.register(Patient)
admin.site.register(DoctorsInput)
admin.site.register(Doctor)
admin.site.register(ContactTracing)