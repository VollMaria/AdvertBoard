from django.urls import path
from .views import AdvList, AdvDetail, AdvCreate, AdvEdit, AdvDelete, AddResponse


urlpatterns = [
    path('', AdvList.as_view(), name='adv_list'),
    path('<int:pk>', AdvDetail.as_view(), name='adv_detail'),
    path('add/', AdvCreate.as_view(), name='adv_create'),
    path('<int:pk>/edit/', AdvEdit.as_view(), name='adv_edit'),
    path('<int:pk>/delete/', AdvDelete.as_view(), name='adv_delete'),
    path('response/', AddResponse.as_view(), name='add_response'),

]
