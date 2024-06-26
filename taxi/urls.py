from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarUpdateView,
    CarDeleteView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer_list",
    ),
    path("cars/", CarListView.as_view(), name="car_list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("manufacturer/create", ManufacturerCreateView.as_view(),
         name="manufacturer-create"),
    path("manufacturer/<int:pk>/update/", ManufacturerUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturer/<int:pk>/delete/", ManufacturerDeleteView.as_view(),
         name="manufacturer-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi_service"
