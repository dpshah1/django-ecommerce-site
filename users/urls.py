from django.urls import path
from users import views 

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('verify_login', views.verify_login, name='verify_login'),
    path('logout', views.logout_user, name='logout_user')
]