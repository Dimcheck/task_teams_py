from users.views import (
    HumanCreate,
    HumanList,
    HumanRetrieve,
)

from django.urls import path


app_name = 'users'

urlpatterns = [
    path('human/', HumanCreate.as_view(), name='human_create'),
    path('human/<int:pk>', HumanRetrieve.as_view(), name='human_get_one'),
    path('humans/', HumanList.as_view(), name='human_get'),
]