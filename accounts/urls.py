from django.urls import path
from .views import SignUpView, SignUpJadvalView, SignUp1L1View, SignUpSammuView, SignUpIndexiew

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('jadval/', SignUpJadvalView.as_view(), name='jadval'),
    path('sammu/', SignUpSammuView.as_view(), name='sammu'),
    path('index/', SignUpIndexiew.as_view(), name='index'),
    path('1L1/', SignUp1L1View.as_view(), name='1L1'),

]