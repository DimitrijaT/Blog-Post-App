from __future__ import annotations

from django.contrib import admin
from datetime import datetime
from django.forms import ModelForm
from django.http import HttpRequest
# from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder

from .models import BlogUser, Post, Comment, File, Block


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True
        return False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "user"]
    search_fields = ["title", "content"]
    # list_filter = (
    #     ('creation_date', DateFieldListFilter),
    # )
    # list_filter = (
    #     ("creation_date", DateRangeFilterBuilder()),
    #     (
    #         "updated_at",
    #         DateTimeRangeFilterBuilder(
    #             title="Custom title",
    #             default_start=datetime(2020, 1, 1),
    #             default_end=datetime(2030, 1, 1),
    #         ),
    #     ),
    #     ("num_value", NumericRangeFilterBuilder()),
    # )
    list_filter = (
        ("creation_date", DateRangeFilterBuilder()),
    )

    exclude = ["user"]

    def has_change_permission(self, request, obj=None):
        # obj.user is our custom BlogUser, obj.user.user is the Django out of the box user
        if obj and request.user == obj.user.user:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if obj:
            print(obj.user)  # BlogUser
            print(obj.user.user)  # user
            print(request.user)  # user

        if request.user.is_superuser or (
                obj and not Block.objects.filter(blocker__user=obj.user.user, blocked__user=request.user).exists()):
            return True
        return False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "creation_date"]
    exclude = ["user"]

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or (
                obj and not Block.objects.filter(blocker__user=obj.user.user, blocked__user=request.user).exists()):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        # obj.user is our custom BlogUser (Comment model has a User ForeignKey)
        # obj.user.user is the Django out of the box user
        if obj and request.user == obj.user.user:
            return True
        return False


@admin.register(File)
class FileAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or (
                obj and not Block.objects.filter(blocker__user=obj.user.user, blocked__user=request.user).exists()):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user.user:
            return True
        return False


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.blocker.user:
            return True
        return False
