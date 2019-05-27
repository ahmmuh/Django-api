from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token 

from . import views


urlpatterns = [
    path('', views.AchievementList.as_view()),
    path('<int:pk>/', views.AchievementDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]