from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display= ['id','name','contact','image','donation_amount',]
    # search_fields = ['name']
admin.site.register(User, UserAdmin)