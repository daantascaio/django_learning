from blog import views
from django.urls import path

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<id>', views.blog, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
