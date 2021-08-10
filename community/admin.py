from django.contrib import admin
from .models import Graduate, Information, Pr, Post, Comment, PrComment, InfoComment, GradComment

admin.site.register(Post)
admin.site.register(Pr)
admin.site.register(Information)
admin.site.register(Graduate)
admin.site.register(Comment)
#admin.site.register(PrComment)

@admin.register(PrComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment',  'post', 'created_on')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(InfoComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment',  'post', 'created_on')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(GradComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment',  'post', 'created_on')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)