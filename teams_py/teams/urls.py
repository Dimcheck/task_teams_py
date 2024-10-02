from teams.views import (
    TeamCreate,
    TeamAppend,
    TeamList,
)

from django.urls import path


app_name = 'teams'

urlpatterns = [
    path('team/', TeamCreate.as_view(), name='personal_comp_create'),
    path('team/<int:pk>', TeamAppend.as_view(), name='personal_comp_append'),
    path('teams/', TeamList.as_view(), name='personal_comp_get'),
]

