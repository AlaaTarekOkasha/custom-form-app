from django.contrib import admin
from .models import ExtraInfo
import csv
from django.http import HttpResponse
from io import StringIO


class ExtraInfoAdmin(admin.ModelAdmin):
    actions = ['download_csv'] 
    list_display = ('user', 'day_of_birth', 'month_of_birth', 'country_of_origin', 'country_codes', 'phone_number',)
    list_display_links = ('user', 'day_of_birth', 'month_of_birth', 'country_of_origin', 'country_codes', 'phone_number',)
    list_filter = ('user',)
    search_fields = ('user', 'day_of_birth', 'month_of_birth', 'country_of_origin', 'country_codes', 'phone_number',) #, 'date_of_birth'
    list_per_page = 25  
    def download_csv(self, request, queryset,*args, **kwargs):
        import csv
        f = open('some.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['user', 'day_of_birth', 'month_of_birth', 'country_of_origin', 'country_codes', 'phone_number',])
        for s in queryset:
            writer.writerow([s.user, s.day_of_birth, s.month_of_birth, s.country_of_origin, s.country_codes, s.phone_number])
        
        f.close()
        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response    
    download_csv.short_description = "Download CSV "



admin.site.register(ExtraInfo, ExtraInfoAdmin)
     
