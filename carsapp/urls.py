from django.urls import path
from carsapp import views

app_name="cars"

urlpatterns = [
    path('',views.CarListView.as_view(), name='car_list'),
    path('<int:car_id>/', views.CarDetailsView.as_view(), name='car_details'),
    path('<int:car_id>/edit', views.CarEditView.as_view(), name='car_edit'),
    path('<int:car_id>/delete', views.CarDeleteView.as_view(), name='car_delete'),
    path('new/', views.CarNewView.as_view(), name='car_new'),
    path('search/', views.CarListSearch.as_view(), name='car_search'),
]