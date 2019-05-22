from django.contrib import admin

# Register your models here.
from cms_model.models import Test
# admin.site.register(Test)

# 新加
class TestAdmin(admin.ModelAdmin):
    # pass
    list_display = ['date','source','title','content','link']
    list_filter = ['date','source',]
    # search_fields = ['date','source']
    list_per_page = 5
    fieldsets = [
        ('basic',{'fields':['date']}),
        ('more',{'fields':['source']}),
    ]
admin.site.register(Test,TestAdmin)