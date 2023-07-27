from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from .utils import send_otp
from django.utils import timezone
from .pagination import *
import datetime
from rest_framework.filters import SearchFilter
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import BasePermission
@login_required(login_url='/login/')
class IsOwnerOrReadOnly(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in ['GET', 'HEAD', 'OPTIONS']:
			return True
		print(request.user)
		print(request.user.phone_number)
		for u in obj.user.all():
			if u.phone_number==request.user.phone_number:
				print("kuch bhi ")
				return True
		return False
class AlbumSongViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSongSerializer   
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
class AlbumOnlyViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	# print(queryset)
	serializer_class = AlbumOnlySerializer   
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
 #Playlist Things
class PlaylistOnlyViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistOnlySerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class PlaylistSongViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSongSerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class RegisterViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all().filter(verification_status=True)
	serializer_class = RegistrationSerializer
	pagination_class  = MyLimitOffsetPagination

# class UserLikeSongViewSet(viewsets.ModelViewSet):
#     queryset = User_Liked_Songs.objects.all()
#     serializer_class =User_Liked_SongsSerializer
class RegisterUser(APIView):
	def post(self,request):
		serializer = MainRegister(data = request.data)
		print(request.data)
		if not serializer.is_valid():
			print('***************************')
			print(serializer.errors)
			return Response({"insecure":serializer.errors}) 
		print('############################')
		serializer.save()
		# print(serializer.data)
		user = CustomUser.objects.get(phone_number=serializer.data['phone_number'])
		token_obj,_ = Token.objects.get_or_create(user =user)
		return Response(serializer.data, status=status.HTTP_200_OK) 

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated        
	


# Premium things
class PremiumViewSet(viewsets.ModelViewSet):
	queryset = Premium.objects.all()
	serializer_class = PremiumOnlySerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

	def create(self, request, *args, **kwargs):
		# Check if a premium entry already exists for the user
		user = request.data.get('user')
		if Premium.objects.filter(user=user).exists():
			return Response({"error": "User already has a premium entry."}, status=status.HTTP_400_BAD_REQUEST)

		return super().create(request, *args, **kwargs)
	def put(self, request, *args, **kwargs):
		premium = self.get_object()
		# Partially update the song with the data from the request
		serializer = self.get_serializer(premium, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK) 
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
class PremiumDetailsViewSet(viewsets.ModelViewSet):
	queryset = Premium.objects.all()
	serializer_class = PremiumDetailsSerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]

	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
	# def get_queryset(self):
	#     # Filter playlists by the current authenticated user
	#     user = self.request.user
	#     return Premium.objects.filter(user=user)
	
	
	
#Artist Things
class ArtistOnlyViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistOnlySerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
class ArtistSongViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSongSerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)

#Playlist Things
class PodcastOnlyViewSet(viewsets.ModelViewSet):
	queryset = Podcast.objects.all()
	serializer_class = PodcastOnlySerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
class PodcastArtistViewSet(viewsets.ModelViewSet):
	queryset = Podcast.objects.all()
	serializer_class = PodcastArtistSerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)


class PlaylistUserViewSet(viewsets.ModelViewSet):
	serializer_class = PlaylistOnlySerializer
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

	def get_queryset(self):
		# Filter playlists by the current authenticated user
		user = self.request.user
		return Playlist.objects.filter(user=user)
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
# ALBUM Things


class AlbumArtistViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumArtistSerializer  
	pagination_class  = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)

 # Song Detail
class SongOnlyViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongOnlySerializer 
	filter_backends = [SearchFilter]
	search_fields = [
		'^song_name'
	]
	pagination_class = MyLimitOffsetPagination
	permission_classes = [IsAuthenticated]
	def patch(self, request, *args, **kwargs):
		song = self.get_object()
		# Partially update the song with the data from the request
		serializer = self.get_serializer(song, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK) 
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
class SongDetailsViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongDetailsSerializer
	permission_classes = [IsAuthenticated]

	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
	def destroy(self, request, pk=None):
		response = {'message': 'Delete function is not offered in this path.'}
		return Response(response, status=status.HTTP_403_FORBIDDEN)
from datetime import datetime,timedelta

class UserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	pagination_class = MyLimitOffsetPagination
	@action(detail=True,methods=["PATCH"])
	def verify_otp(self,request,pk=None):
		instance = self.get_object()
		if(instance.verification_status):
			return Response(
				"You are alredy verified",
				status=status.HTTP_400_BAD_REQUEST
			)
		if(instance.otp == request.data.get("otp") and instance.otp_expiry  and timezone.now() < instance.otp_expiry):
			instance.is_active=True
			instance.otp_expiry = None
			instance.max_otp_expiry=settings.MAX_OTP_TRY
			instance.otp_max_out = None
			instance.verification_status = True
			instance.save()
			print(instance.is_active)
			print(instance.otp_expiry)
			print(instance.max_otp_expiry)
			print(instance.otp_max_out)
			print(instance.verification_status)
			serializers
			return Response(
				"Successfully verified user",status=status.HTTP_200_OK
			)
		return Response(
			"Please enter the correct OTP",
			status=status.HTTP_400_BAD_REQUEST
		)
	@action(detail=True,methods=["PATCH"])
	def regenerate_otp(self,request,pk=None):
		instance=self.get_object()
		if(instance.verification_status):
			return Response(
				"You are alredy verified",
				status=status.HTTP_400_BAD_REQUEST
			)
		if(int(instance.max_otp_try)==0 and timezone.now()<instance.otp_max_out):
			return Response(
				"MAX OTP LIMIT REACHED TRY AFTER SOME TIME",
				status=status.HTTP_400_BAD_REQUEST
			)
		otp  = random.randint(1000,9999)
		otp_expiry=timezone.now()+timedelta(minutes=10)
		max_otp_try = int(instance.max_otp_try)-1
		instance.otp =otp
		instance.otp_expiry = otp_expiry
		instance.max_otp_try = max_otp_try
		if max_otp_try == 0:
			instance.otp_max_out = timezone.now() +timedelta(hours=1)
		elif max_otp_try==-1:
			instance.max_otp_try = settings.MAX_OTP_TRY
		else:
			instance.max_otp_try=None
			instance.max_otp_try = max_otp_try
		instance.save()
		send_otp(instance.phone_number,otp)
		return Response(
			"succesfully regenerate otp ",
   			status=status.HTTP_200_OK
		)	
  	
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet
# from django.contrib.auth import authenticate
# from rest_framework.authentication import TokenAuthentication

# class LoginView(APIView):
#     authentication_classes = [TokenAuthentication]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             phone_number = serializer.validated_data['phone_number']
#             password = serializer.validated_data['password']

#             user = authenticate(request, phone_number=phone_number, password=password)

#             if user:
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LogoutView(viewsets.ModelViewSet):
#     def create(self, request):
#         # Simply delete the user's token to log them out
#         request.user.auth_token.delete()
#         return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
