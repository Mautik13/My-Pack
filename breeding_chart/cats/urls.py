from django.urls import path, include
from . import views
from .views import cat_table, add_cat, remove_cat, edit_cat, users_login, users_logout, users_register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cat_list/', cat_table, name='cat_table'),
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('cat/', views.cat, name='cat'),
    path('home/cat/', views.cat, name='cat'),
    path("home/cat/cat_detail/<int:id>", views.cat_detail, name='cat_detail'),
    path('tomcat/', views.tomcat, name='tomcat'),
    path('home/tomcat/', views.tomcat, name='tomcat'),
    path('home/tomcat/tomcat_detail/<int:id>', views.tomcat_detail, name='tom_detail'),
    path('kitten/', views.kitten, name='kitten'),
    path('home/kitten/', views.kitten, name='kitten'),
    path('home/kitten/kitten_detail/<int:id>', views.kitten_detail, name='kitten_detail'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('add_cat/', add_cat, name='add_cat'),
    path('remove_cat/<int:cat_id>/', remove_cat, name='remove_cat'),
    path('edit_cat/<int:cat_id>/', edit_cat, name='edit_cat'),
    path('users/login/', users_login, name='login'),
    path('users/logout/', users_logout, name='logout'),
    path('login/', users_login, name='login'),
    path('register/', users_register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='cats/users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cats/users/logout.html'), name='logout'),
    path('users/login/users/register/', users_register, name='register'),
    path('home/users/logout/', users_logout, name='logout'),
    path('home/cat/users/login/', users_login, name='login'),
    path('home/cat/add_cat/', add_cat, name='add_cat'),
   # path('home/cat/remove_cat/', remove_cat, name='remove_cat'),
    path('home/cat/edit_cat/', edit_cat, name='edit_cat'),
    path('remove_cat/<int:cat_id>/', remove_cat, name='remove_cat'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)