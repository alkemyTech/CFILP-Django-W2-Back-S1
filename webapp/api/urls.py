from django.urls import path
from api.views import (ClienteListApiView,)

urlpatterns = [
    path('cliente', ClienteListApiView.as_view()),
]
