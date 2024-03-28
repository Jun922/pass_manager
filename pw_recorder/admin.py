from django.contrib import admin
from .models import App


class AppAdmin(admin.ModelAdmin):
    fields = ('name', 'password', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(App, AppAdmin)