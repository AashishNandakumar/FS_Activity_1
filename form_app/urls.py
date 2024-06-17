from django.urls import path
from .views import handle_form_view

urlpatterns = [
    path('form', handle_form_view),
]
