from django.urls import path
from .views import SignUpView, SignUpJadvalView, SignUp1L1View

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('jadval/', SignUpJadvalView.as_view(), name='jadval'),
    path('1L1', SignUp1L1View.as_view(), name='1L1'),

]