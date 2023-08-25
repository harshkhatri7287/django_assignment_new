from django.contrib import admin
from django.urls import path, include
from items import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', include('items.urls')),
    path('', include('authentication.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest framework'))
]
