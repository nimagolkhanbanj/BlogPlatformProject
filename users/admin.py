from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

admin.site.register(Author)


class AuthorAdminSite(AdminSite):
    site_header = "Author Admin"


author_admin_site = AuthorAdminSite(name="author_admin")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "biography"]


author_admin_site.register(Author, AuthorAdmin)
