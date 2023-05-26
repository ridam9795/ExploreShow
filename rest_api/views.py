from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Event,Sport,Activity
from .serializers import MovieSerializer, EventSerializer,SportSerializer,ActivitySerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib.auth.models import User
from django.middleware import csrf
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class MovieApi(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class EventApi(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SportApi(generics.ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = EventSerializer


class ActivityApi(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = EventSerializer

class SearchApi(APIView):
    def get(self,request):
        name=request.GET.get('name')
        movies=Movie.objects.filter(title__icontains=name)
        movieSerializer=MovieSerializer(movies,many=True)
        events=Event.objects.filter(title__icontains=name)
        eventSerializer=EventSerializer(events,many=True)
        sports=Sport.objects.filter(title__icontains=name)
        sportSerializer=SportSerializer(sports,many=True)
        activities=Activity.objects.filter(title__icontains=name)
        activitySerializer=ActivitySerializer(activities,many=True)
        
        return Response({'Status':200,'movies':movieSerializer.data,'events':eventSerializer.data,'sports':sportSerializer.data,'activities':activitySerializer.data})


class FilterMovieApi(APIView):
    query_set = Movie.objects.all()

    def get(self, request):
        languages = request.GET.get('languages')
        categories = request.GET.get('categories')
        genre = request.GET.get('genre')
        movies = Movie.objects.all()

        if languages:
            languages = languages.split("|")
            movies = movies.filter(
                languages__in=languages)
        
        if categories:
            categories = categories.split("|")
            movies = movies.filter(
                category__in=categories)
       
        if genre:
            genre = genre.split("|")
            movies = movies.filter(genre__in=genre)
      

        movieSerializer = MovieSerializer(movies, many=True)

        return Response({"status": 200, "filteredMovieData": movieSerializer.data})
    
class FilterEventApi(APIView):
    query_set = Event.objects.all()

    def get(self, request):
        languages = request.GET.get('languages')
        categories = request.GET.get('categories')
        events = Event.objects.all()

        if languages:
            languages = languages.split("|")
            events = events.filter(
                languages__in=languages)

        
        if categories:
            categories = categories.split("|")
            events = events.filter(category__in=categories)
        

        eventSerializer = EventSerializer(events, many=True)

        return Response({"status": 200, "filteredEventData": eventSerializer.data})
    
class FilterSportApi(APIView):
    query_set = Sport.objects.all()

    def get(self, request):
        prices = request.GET.get('prices')
        categories = request.GET.get('categories')
        sports = Sport.objects.all()

        if prices:
            prices = prices.split("|")
            sports = sports.filter(
                prices__in=prices)

        
        if categories:
            categories = categories.split("|")
            sports = sports.filter(category__in=categories)
        

        sportSerializer = SportSerializer(sports, many=True)

        return Response({"status": 200, "filteredSportData": sportSerializer.data})
    
class FilterActivityApi(APIView):
    query_set = Activity.objects.all()

    def get(self, request):
        prices = request.GET.get('prices')
        categories = request.GET.get('categories')
        activities = Activity.objects.all()

        if prices:
            prices = prices.split("|")
            activities = activities.filter(
                prices__in=prices)

        
        if categories:
            categories = categories.split("|")
            activities = activities.filter(category__in=categories)
        

        activitySerializer = ActivitySerializer(activities, many=True)

        return Response({"status": 200, "filteredActivityData": activitySerializer.data})


class RegisterUser(APIView):
    def post(self,request):
        print(">>>>>>>....",request.data)
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({"status":403,"error":serializer.errors})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,'payload':serializer.data,'refresh':str(refresh),'access':str(refresh.access_token),'message':"Registration Successfull"})

def get_token_for_user(user):
    refresh=RefreshToken.for_user(user)
    name=User.objects.get(username=user.username).first_name

    return {
        'name':str(name),
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }
class LoginUser(APIView):
    def post(self,request,format=None):
        data=request.data
        response=Response()
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                data=get_token_for_user(user)

                response.set_cookie(
                    key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                    value=data['access'],
                    expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                    )
                csrf.get_token(request)
                response.data={"Success":"Login Successfully","data":data}
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


                
