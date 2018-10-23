from django.contrib import admin
from .models import Department, Part1

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    '''
        Admin View for Department
    '''
    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    pass

admin.site.register(Department, DepartmentAdmin)

class Part1Admin(admin.ModelAdmin):
    '''
        Admin View for Part1
    '''
    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    fieldsets = (
    	("Detail", {"fields": ("department", 'user')}),
    	("Quetion 1)", {"fields": ("que_1",)}),
    	("Quetion 2)", {"fields": ("que_2",)}),
    	("Quetion 3)", {"fields": ("que_3",)}),
    	("Quetion 4)", {"fields": ("que_4",)}),
    	("Quetion 5)", {"fields": ("que_5",)}),
    	)

admin.site.register(Part1, Part1Admin)