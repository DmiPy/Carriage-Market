from django.urls import path
from .views import WagonsView

urlpatterns = [
    path('wagons', WagonsView.as_view(), name='home'),
]