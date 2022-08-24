from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tx/<int:tx_id>', views.tx_view, name='tx'),
]
