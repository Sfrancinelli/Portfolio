from django.contrib import admin
from projects.models import Project, Tag, ProjectTag
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


# Register your models here.
class MyAdmin(admin.AdminSite):
    site_header = 'Francinelli Admin'
    site_title = 'Administración'
    index_title = 'Modelos'
    empty_value_display = 'No se encontraron registros'


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image']
    list_display_links = ('id', )


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', )


class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'tag']
    list_display_links = ('id', )


my_admin = MyAdmin(name='SF')
my_admin.register(Project, ProjectsAdmin)
my_admin.register(Tag, TagAdmin)
my_admin.register(ProjectTag, ProjectTagAdmin)

my_admin.register(User, UserAdmin)
my_admin.register(Group, GroupAdmin)
