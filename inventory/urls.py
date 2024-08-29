from django.urls import path

from .views import InventoryListView, InventoryDetailView

urlpatterns = [
    path("", InventoryListView.as_view(), name="inventory_list"),
    path("<uuid:pk>/", InventoryDetailView.as_view(), name="inventory_detail"),
]
