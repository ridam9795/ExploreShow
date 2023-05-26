
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('movies/', views.MovieApi.as_view(), name='movies'),
    path('filterMovies/', views.FilterMovieApi.as_view(), name='filterMovies'),
    path('events/', views.EventApi.as_view(), name='events'),
    path('filterEvents/', views.FilterEventApi.as_view(), name='filterEvents'),
    path('sports/', views.SportApi.as_view(), name='sports'),
    path('filterSports/', views.FilterSportApi.as_view(), name='filterSports'),
    path('activities/', views.ActivityApi.as_view(), name='activities'),
    path('filterActivities/', views.FilterActivityApi.as_view(), name='filterActivities'),
    path('search/', views.SearchApi.as_view(), name='search'),
    path('login/', views.LoginUser.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/',TokenVerifyView.as_view(),name="verify_token"),
    path('register/',views.RegisterUser.as_view(),name="registerUser")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
