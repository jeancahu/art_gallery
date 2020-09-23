from django.urls import path

from . import views

urlpatterns = [
    path('<number>', views.collection, name='collection')
]
