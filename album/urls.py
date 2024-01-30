from django.urls import path
from .import views
urlpatterns = [
    path('adda/', views.add_album.as_view(),name = 'add_album'),
    path('edita/<int:id>', views.edit_album.as_view(),name = 'edit_album'),
    path('dela/<int:id>', views.delete_album.as_view(),name = 'del_album'),
]