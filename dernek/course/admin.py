from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import *


class ClassroomModelAdmin(admin.ModelAdmin):
    pass


class LectureModelAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)

        UserAdmin.list_display = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_lecturer',
        ]

        UserAdmin.ordering = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

        UserAdmin.actions = list(UserAdmin.actions) + [make_lecturer, remove_lecturer]

    def is_lecturer(self, obj):
        lecturer = False
        for group in obj.groups.all():
            if group.name == 'Eğitmen':
                lecturer = True
        return lecturer
    is_lecturer.admin_order_field ='groups__name'
    is_lecturer.short_description = 'Eğitmen'
    is_lecturer.boolean = True


def make_lecturer(modeladmin, request, queryset):
    group_returned, group_created = Group.objects.get_or_create(name="Eğitmen")
    group = group_returned if group_returned else group_created

    for user in queryset.all():
        user.groups.add(group)

make_lecturer.short_description = 'Eğitmen olarak yetkilendir'


def remove_lecturer(modeladmin, request, queryset):
    for user in queryset.all():
        user.groups.through.objects.filter(group__name='Eğitmen').delete()

remove_lecturer.short_description = 'Eğitmenlik yetkisini kaldır'

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Classroom, ClassroomModelAdmin)
admin.site.register(Lecture, LectureModelAdmin)
admin.site.unregister(Lecture)
