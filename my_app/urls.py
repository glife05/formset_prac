from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:programmer_id>',views.listing,name='listing'),
]
