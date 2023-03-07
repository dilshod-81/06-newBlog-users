from django.urls import path

from .views import (
    DarsjadvalListView,
    DarsjadvalUpdateView,
    DarsjadvalDeleteView,
    DarsjadvalDetailView,
    DarsjadvalCreateView,

)

urlpatterns = [
    path('<int:pk>/edit/', DarsjadvalUpdateView.as_view(), name='jadval_edit'),
    path('<int:pk>/', DarsjadvalDetailView.as_view(), name='jadval_detail'),
    path('<int:pk>/delete/', DarsjadvalDeleteView.as_view(), name='jadval_delete'),
    path('new/', DarsjadvalCreateView.as_view(), name='jadval_new'),
    path('', DarsjadvalListView.as_view(), name='jadval_list'),
]