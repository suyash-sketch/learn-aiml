from django.contrib import admin
from .models import ChaiVareity, ChaiReview, Store, ChaiCertificate



# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra =2


class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added',)
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    filter_horizontal = ('chai_varieties',)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number',)

admin.site.register(ChaiVareity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)

