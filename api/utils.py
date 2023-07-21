import requests
from django.conf import settings




def send_otp(mobile,otp):
    url = f"https://2factor.in/API/V1/{settings.SMS_API_KEY}/SMS/{mobile}/{otp}/"
    payload=""
    headers={"content-type":
        "application/x-www-form-urlencoded"
        }
    response= requests.get(url,data=payload,headers=headers)
    print(response.json())
    return bool(response.ok)