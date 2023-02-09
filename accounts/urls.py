from django.urls import path
from .views import SignUpView, SignUpJadvalView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('jadval/', SignUpJadvalView.as_view(), name='jadval'),
]