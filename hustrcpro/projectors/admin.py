from django.contrib import admin

# Register your models here.

from projectors.models import Build, Brand, Status, Event, Room, Projector, Maintenancerecord, Statusrecord
from projectors.app_view_models import Projectorstatus
from projectors.models import Problem

class BuildAdmin(admin.ModelAdmin):
    list_display = ('build_id', 'build_name', 'build_description', 'build_state')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_id', 'brand_cn', 'brand_en', 'model_number')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_id', 'status_name')

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name')

class ProblemAdmin(admin.ModelAdmin):
	list_display = ('projector', 'problem_id', 'content', 'date_register', 'checked')

admin.site.register(Build, BuildAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Problem, ProblemAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'room_style', 'room_description', 'room_state', 'build')

admin.site.register(Room, RoomAdmin)
#admin.site.register(Room)

class ProjectorAdmin(admin.ModelAdmin):
#	def build_room(self, obj):
#        buildroom = get_build_by_room(obj)
#        return buildroom
#    build_room.name = 'Weizhi'
#    build_room.allow_tags = True
    list_display = ('projector_id', 'brand', 'room', 'level_no', 'serial_no', 'note')

admin.site.register(Projector, ProjectorAdmin)

class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('m_r_id', 'projector', 'event', 'event_note', 'from_room', 'to_room', 'date_register')

class StatusRecordAdmin(admin.ModelAdmin):
    list_display = ('s_r_id', 'projector' ,'status' , 'date_register')

admin.site.register(Maintenancerecord, MaintenanceRecordAdmin)
admin.site.register(Statusrecord, StatusRecordAdmin)

class ProjectorStatusAdmin(admin.ModelAdmin):
    list_display = ('projector_id', 's_r_id', 'status_id', 'status_name', 'date_register')
admin.site.register(Projectorstatus, ProjectorStatusAdmin)

#class CustomUserAdmin(admin.ModelAdmin):
#    def city_name(self,obj):
#        cityname = get_city_by_user(obj)
#        return cityname
#    city_name.short_description = 'city' 
#    city_name.verbose_name = 'city2'
#    city_name.allow_tags = True

#admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)
