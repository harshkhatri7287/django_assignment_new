from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/', views.ItemViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index page'),
    path('create/', views.create_view, name="create_view"),
    path('<str:item_name>/delete/', views.delete_view, name="delete view"),
    path('<str:item_name>/update/', views.update_view, name="update view")
]