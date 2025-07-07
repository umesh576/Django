from django.urls import path
from . import views

urlpatterns = [
    path('', views.allChai, name='allChai'),
    path('<int:chai_id>/', views.chaiDetails, name='chai_details'),
]
