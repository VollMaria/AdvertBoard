from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', AdvList.as_view(), name='adv_list'),
    path('<int:pk>', AdvDetail.as_view(), name='adv_detail'),
    path('add/', AdvCreate.as_view(), name='adv_create'),
    path('<int:pk>/edit/', AdvEdit.as_view(), name='adv_edit'),
    path('<int:pk>/delete/', AdvDelete.as_view(), name='adv_delete'),
    path('<int:pk>/response/', AddResponse.as_view(), name='add_response'),
    path('profile/', Profile.as_view(), name='profile'),
    path('responses/', ResponseList.as_view(), name='responses'),
    path('responses/<int:pk>/', ResponseDetail.as_view(), name='response'),
    path('<int:advertisement>/<int:response>/', views.response_good, name='response_good'),
    path('<int:advertisement>/<int:response>/', views.response_bad, name='response_bad'),
    path('responses/<int:pk>/delete/', RespDelete.as_view(), name='resp_delete'),

]
