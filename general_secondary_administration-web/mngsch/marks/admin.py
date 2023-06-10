from django.contrib import admin
from marks.models import Tmt,Tmt2,terms,years,year,nameschool
# Register your models here.

admin.site.register(Tmt)
admin.site.register(Tmt2)
admin.site.register(terms)
admin.site.register(years)
admin.site.register(year)
admin.site.register(nameschool)
admin.site.site_header="نظام ادارة المدارس الاساسية"
admin.site.site_titel="نظام ادارة المدارس الاساسية"

