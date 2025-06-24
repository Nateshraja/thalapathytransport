from django.contrib import admin
from .models import Company, Goods, Trip, Vehicle, MyCompany
from django.utils.html import format_html
from import_export.admin import ExportMixin

# ✅ Trip Admin
@admin.register(Trip)
class TripAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        'date', 'company', 'pickup_location', 'drop_location', 'total', 'print_pdf', 'send_whatsapp'
    )
    search_fields = ('company__name', 'pickup_location', 'drop_location')
    ordering = ('-date',)

    def print_pdf(self, obj):
        return format_html(
            '<a class="button" href="/trips/{}/pdf/" target="_blank">🖨 Print</a>',
            obj.pk
        )
    print_pdf.short_description = "Print"

    def send_whatsapp(self, obj):
        return format_html(
            '<a class="button" href="/trips/{}/send-whatsapp/" target="_blank">📩 WhatsApp</a>',
            obj.pk
        )
    send_whatsapp.short_description = "Send WhatsApp"

# ✅ Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name',)

# ✅ Goods
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name',)

# ✅ Vehicle
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number', 'driver_name', 'vehicle_type', 'driver_contact')
    search_fields = ('number', 'driver_name')

# ✅ MyCompany (your company’s branding info)
@admin.register(MyCompany)
class MyCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'upi_id')
