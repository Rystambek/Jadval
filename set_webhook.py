import requests
import os

url = 'https://darsjadvali2023.pythonanywhere.com/webhook'

Token = '6162217632:AAEnncQeDNHOnSCAlMw0PTxbkJpAQQdL2X4'

payload = {
    "url":url
}

r = requests.get(f"https://api.telegram.org/bot{Token}/setWebhook", params=payload)
r = requests.get(f"https://api.telegram.org/bot{Token}/GetWebhookInfo", params=payload)



print(r.json())