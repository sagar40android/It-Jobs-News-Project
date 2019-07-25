from django.contrib import admin
from jobNewsApp.models import pubeJobs
# Register your models here.
class puneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(pubeJobs,puneJobsAdmin)



    