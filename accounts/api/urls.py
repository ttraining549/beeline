from django.urls import path
from dj_rest_auth import urls as dj_rest_auth_urls


urlpatterns = [
    path('login/', dj_rest_auth_urls.LoginView.as_view(),
         name='dj_rest_auth_login'),
    path('logout/', dj_rest_auth_urls.LogoutView.as_view(),
         name='dj_rest_auth_logout'),
]
