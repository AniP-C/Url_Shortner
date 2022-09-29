from django.urls import path
from root.views import createUrl, routeToURL



urlpatterns = [
    path('', createUrl),
    path('<slug:key>', routeToURL)
]