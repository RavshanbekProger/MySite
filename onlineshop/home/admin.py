from django.contrib import admin
from .models import Setting, Post, License, ImagesLic


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display =  ['title', 'author']


class LicenseImageInline(admin.TabularInline):
    model = ImagesLic
    extra = 5

class LicenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    inlines = [LicenseImageInline]


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at']

admin.site.register(Post, PostAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Setting, SettingAdmin)
#admin.site.register(Images)

