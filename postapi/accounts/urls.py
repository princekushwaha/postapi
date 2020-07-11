from django.urls import path, include

urlpatterns = [
     path('', include('rest_auth.urls')), 
    path('', include('rest_auth.registration.urls')), 
    path('', include('allauth.account.urls')),
]