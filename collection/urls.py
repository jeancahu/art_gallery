from django.urls import path

from . import views

urlpatterns = [
    path('<int:coll_numb>', views.collection, name='collection')
]
