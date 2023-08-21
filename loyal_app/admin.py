from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.safestring import mark_safe

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tg_id', 'phone', 'point', 'created_at']
    list_filter = ['id', 'name', 'tg_id', 'phone', 'created_at']
    search_fields = ['name', 'tg_id', 'phone']
    list_editable = ['point']
    change_list_template = "test.html"

    def reset_point(self, request):
        User.objects.all().update(point=0)
        self.message_user(request, "Hamma foydalanuvchilar ballari o'zgartirildi")
        return HttpResponseRedirect("../")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('set_null/', self.reset_point)
        ]
        return my_urls + urls


class BonusAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'point', 'user', 'created_at']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_image', 'created_at']

    def get_image(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_image.short_description = 'Rasim'


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'prod', 'price']
    list_editable = ['name', 'price']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


admin.site.unregister(Group)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'
