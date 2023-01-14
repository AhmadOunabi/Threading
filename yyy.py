import requests
import time
import threading

api_key = '174dbc5ceb98a1c550c522ea836f4e2a'

def weather(lat,lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    temp=response.json()
    temp=list(temp.values())[3]
    temp=list(temp.values())[0]
    temp=temp-273.15
    print('{:.1f}'.format(temp)+'C')

start=time.time()
th1=threading.Thread(target=weather, args=['33.5138','36.2765']).start()
#th2=threading.Thread(target=weather, args=['Berlin']).start()
#th3=threading.Thread(target=weather, args=['Moscow']).start()
#th4=threading.Thread(target=weather, args=['Minsk']).start()
#th5=threading.Thread(target=weather, args=['Barcelona']).start()
end=time.time()
