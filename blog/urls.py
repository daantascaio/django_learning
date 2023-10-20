from blog import views
from django.urls import path

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<id>', views.blog, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
