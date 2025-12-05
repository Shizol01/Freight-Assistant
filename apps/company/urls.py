from django.urls import path
from .views import (CarrierAddView, CarrierDetailView,
                      CarrierUpdateView, CarrierDeleteView,
                      CarrierListView)

urlpatterns = [
    path('carrier/add/',CarrierAddView.as_view(), name='carrier-add'),
    path('carrier/detail/<int:carrier_id>',CarrierDetailView.as_view(), name='carrier-detail'),
    path('carrier/update/<int:carrier_id>',CarrierUpdateView.as_view(), name='carrier-update'),
    path('carrier/delete/<int:carrier_id>',CarrierDeleteView.as_view(), name='carrier-delete'),
    path('carrier/all/',CarrierListView.as_view(), name='carrier-list'),
]
