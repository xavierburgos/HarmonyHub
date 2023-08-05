from django.contrib import admin
from django.urls import path
from HarmonyHub.views import categories
from HarmonyHub.views import posts
from HarmonyHub.views import socialmedia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', categories, name='categories'),
    path('post/', posts, name='posts'),
    path('socialmedia/', socialmedia, name='socialmedia')
]
