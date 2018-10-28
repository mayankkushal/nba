from django.contrib import admin
from .models import *

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    """
        Admin View for Department
    """

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
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)
