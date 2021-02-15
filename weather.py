import requests
import json

city = "Asan"
apikey = "16f4744e358c6e07141f0b7b646d2e36"  # 보안으로 #처리
lang = "kr"

api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
data = json.loads(result.text)

print(f'{data["name"]}의 날씨입니다.')
print(f'날씨는 {data["weather"][0]["description"]} 입니다.')
print(f'현재 온도 : {data["main"]["temp"]}')
print(f'체감 온도 : {data["main"]["feels_like"]}')
print(f'최저 기온 : {data["main"]["temp_min"]}')
print(f'최고 기온 : {data["main"]["temp_max"]}')
print(f'습도 : {data["main"]["humidity"]}')
print(f'기압 : {data["main"]["pressure"]}')
print(f'풍향 : {data["wind"]["deg"]}')
print(f'풍속 : {data["wind"]["speed"]}')



