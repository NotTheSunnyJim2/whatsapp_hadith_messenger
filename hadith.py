import requests
import random

def get_hadith(api_key):
    url = "https://hadithapi.com/api/hadiths/"
    params = {
        "apiKey": api_key,
        "status": "sahih"
    }

    response = requests.get(url, params=params)
    data = response.json()
    total = data['hadiths']['total']
    targetId = random.randrange(1, total)
    hadith = None

    new_params = {
        "apiKey": api_key,
        "status": "sahih",
        "paginate": 1,
        "page": targetId
    }
    
    response = requests.get(url, params=new_params)
    data = response.json()
    hadith = data['hadiths']['data'][0]

    hadithEnglish = hadith['hadithEnglish']
    hadithNumber = hadith['hadithNumber']
    bookName = hadith['book']['bookName']
    status = hadith['status']

    return hadithEnglish, hadithNumber, bookName, status