from . import views
from django.urls import path

# Here Create Our urls/path

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:pk>', views.blog, name='blog'),
    # path('post/<str:pk>', views.post, name='post'),
    path('webdesign', views.webdesign, name='webdesign'),
]
