from django.contrib import admin

# Register your models here.
from .models import Person, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 3

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['name']}),
                    ('Tag', {'fields': ['tag'], 'classes': ['collapse']}),

    ]
    inlines = [ProfileInline]

admin.site.register(Person, PersonAdmin)
