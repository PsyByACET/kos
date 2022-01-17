from django.contrib import admin

from .models import *
from django.utils.safestring import mark_safe


class PassportInline(admin.StackedInline):
    model = Passport

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Клиенты и паспорта"""
    list_display = ['name_client', 'status_client']  # что видно о клиенте не переходя на его страницу
    search_fields = ('name_client', 'status_client')  
    inlines = [
        PassportInline,
    ]


@admin.register(Employee)
class StaffAdmin(admin.ModelAdmin):
	"""Сотрудники"""
	list_display = ('full_name', 'login')  
	search_fields = ('full_name', 'login')  
	readonly_fields = ('get_photo',)
    
	def get_photo(self, obj):
		return mark_safe(f'<img src={obj.link_photo.url} width="auto" height="140"')

	def has_add_permission(self, request):
		return True

	def has_delete_permission(self, request, obj=None):
		return False

	def has_view_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return True


admin.site.register(Office)
admin.site.register(Position)
admin.site.register(Contract)
admin.site.register(Tourist)
admin.site.register(Ticket)
admin.site.register(Currency)
admin.site.register(Deal)


class CityInline(admin.StackedInline):
    model = City

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """города и страны"""
    # list_display = ['name_client', 'status_client']  # что видно о клиенте не переходя на его страницу
    # search_fields = ('name_client', 'status_client')  # по каким полям реализован поиск
    inlines = [
        CityInline,
    ]


class RoomInline(admin.StackedInline):
    model = Room

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    """отели и номера"""
    # list_display = ['name_client', 'status_client']  # что видно о клиенте не переходя на его страницу
    # search_fields = ('name_client', 'status_client')  # по каким полям реализован поиск
    inlines = [
        RoomInline,
    ]

class IntermediatetransportInline(admin.StackedInline):
    model = Intermediatetransport

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    """тур и доп транспорт"""
    # list_display = ['name_client', 'status_client']  # что видно о клиенте не переходя на его страницу
    # search_fields = ('name_client', 'status_client')  # по каким полям реализован поиск
    inlines = [
        IntermediatetransportInline,
    ]