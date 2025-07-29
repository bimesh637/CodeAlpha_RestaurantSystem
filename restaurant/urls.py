from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MenuItemViewSet,
    TableViewSet,
    ReservationViewSet,
    OrderViewSet,
    InventoryItemViewSet,
)

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet, basename='menuitem')
router.register(r'tables', TableViewSet, basename='table')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'inventory', InventoryItemViewSet, basename='inventoryitem')

urlpatterns = [
    path('', include(router.urls)),
]
