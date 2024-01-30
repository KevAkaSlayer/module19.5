from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login.as_view(),name = 'login' ),
    path('logout/',views.user_logout,name = 'logout' ),
]
