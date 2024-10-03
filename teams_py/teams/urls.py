from teams import views
from django.urls import path

app_name = 'teams'

urlpatterns = [
    path('team/', views.TeamCreate.as_view(), name='personal_comp_create'),
    path('team/<int:pk>', views.TeamManage.as_view(), name='personal_comp_manage'),
    path('team/append/<int:pk>', views.TeamAppend.as_view(), name='personal_comp_append'),
    path('teams/', views.TeamList.as_view(), name='personal_comp_get'),
]

