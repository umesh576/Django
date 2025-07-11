from django.contrib import admin
from .models import chaiModel ,ChaiReviews, Store, chaiCertificate

# Register your models here.

class chaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2 


class chaiModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','date')
    inlines = [chaiReviewInline,]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display= ('chai','number')

admin.site.register(chaiModel,chaiModelAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(chaiCertificate, chaiCertificateAdmin)
