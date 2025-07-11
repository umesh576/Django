from django.urls import path
from . import views

urlpatterns = [
    path('', views.allChai, name='allChai'),
    path('<int:chai_id>/', views.chaiDetails, name='chai_details'),
    path('chai_store/' , views.chai_store_view, name='chai_store_view')
]
