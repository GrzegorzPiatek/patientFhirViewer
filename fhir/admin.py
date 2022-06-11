from django.contrib import admin
from fhir.models import Medicationstatement, Observation, Patient

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("identifier", "name", "gender", "birthdate")

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ("coding", "value", "unit", "date", "patientidentifier")


@admin.register(Medicationstatement)
class MedicationstatementAdmin(admin.ModelAdmin):
    list_display = ("concept", "patientid")

