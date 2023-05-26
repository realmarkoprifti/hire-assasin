from django.shortcuts import render
from .serializers import AssasinSerializer, HitSerializer
from .models import User, Hit, AssasinProfile
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.decorators import api_view
from random import choice
import requests

# Create your views here.

RECAPTCHA_SECRET = '6LfPPj0mAAAAAO1DKiNEDWurdxM8EziRRjttDEdD'

def check_captcha(captcha_value):
    recaptcha_request = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': RECAPTCHA_SECRET,
        'response': captcha_value
    })
    
    return recaptcha_request.json()


@api_view(["GET"])
def get_assasins(request):
    model = AssasinProfile.objects.all()
    serializer = AssasinSerializer(model, many=True)
    
    return Response(serializer.data, HTTP_200_OK)


@api_view(["GET"])
def get_hits(request):
    hits = Hit.objects.filter(status="completed")
    serializer = HitSerializer(hits, many=True)
    
    return Response(serializer.data, HTTP_200_OK)


@api_view(["POST"])
def track_assasination(request):
    token_status = check_captcha(request.data["captcha_token"])
    
    if token_status["success"]:
        #try:
        model = Hit.objects.get(track_number=request.data["track_number"])
        
        return Response({"status": model.status}, HTTP_200_OK)

        #except:
        #    return Response({"message": "Something went wrong!"}, HTTP_400_BAD_REQUEST)
        
    return Response({"message": "reCaptcha token is invalid"}, HTTP_403_FORBIDDEN)

@api_view(["POST"])
def place_order(request):
    def generate_track_number():
        code = ""
        
        for i in range(5):
            code += choice("1234567890")
            
        return int(code)
        
        
    token_status = check_captcha(request.data['captcha_value'])
    if token_status["success"]:
        
        try:
            code = generate_track_number()
            hitman = AssasinProfile.objects.get(user=request.data["assasin"])
            hit = Hit.objects.create(track_number=code, hitman=hitman, price=hitman.starting_price, target=request.data["target"])
            hit.save()

            return Response({"track_number": code}, HTTP_200_OK)

        except:
            return Response({"message": "Something went wrong!"}, HTTP_400_BAD_REQUEST)
    
    return Response({"message": "reCaptcha token is invalid"}, HTTP_200_OK)