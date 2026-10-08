from django.contrib import admin
from tour.models import *

class UserAdmin(admin.ModelAdmin):
    list_display=("username","email","mobile_no","password",)
admin.site.register(UserRegister,UserAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display=("package_name","package_type","package_location","package_price","package_features","package_details","package_image",)
admin.site.register(CreatePackage,PackageAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=("username","email","mobile_no","subject","description",)
admin.site.register(Enquiry,EnquiryAdmin)

class RaisedAdmin(admin.ModelAdmin):
    list_display=("username","email","tour_name","location","details",)
admin.site.register(TicketRaised,RaisedAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=("username","email","package_name",)
admin.site.register(Bookings,BookingAdmin)