from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index page'),
    path('create/', views.create_view, name="create_view"),
    path('<str:item_name>/delete/', views.delete_view, name="delete view"),
    path('<str:item_name>/update/', views.update_view, name="update view")
]