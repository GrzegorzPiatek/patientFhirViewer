from django.contrib import admin
from fhir.models import Medicationstatement, Observation, Patient
# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models

class ObservationAdmin(admin.StackedInline):
    model = Observation
    list_display = ("coding", "value", "unit", "date")
    # list_filter = ("date", "coding")
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
    
    
class MedicationstatementAdmin(admin.StackedInline):
    model = Medicationstatement
    list_display = ("concept", "patient")
    read_only = ('patient')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
    
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "birthdate")
    inlines = [ObservationAdmin, MedicationstatementAdmin]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
    
    

    
admin.site.register(Patient, PatientAdmin)