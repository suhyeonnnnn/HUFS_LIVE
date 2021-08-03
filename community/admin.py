from django.contrib import admin
from .models import Graduate, Information, Pr, Post, Comment

admin.site.register(Post)
admin.site.register(Pr)
admin.site.register(Information)
admin.site.register(Graduate)
admin.site.register(Comment)