from django.contrib import admin
from .models import Person

# Register your models here.
admin.site.register(Person)

class PersonAdmin(admin.ModelAdmin):   # new
    list_display = ('ssn', 'tel', 'account')
    list_filter = ('ssn', 'tel', 'account')

    fieldsets = (
        (None, {
            'fields': ('ssn', 'tel', 'account')
        }),
        ('Availability', {
            'fields': ('ssn', 'tel')
        }),
    )