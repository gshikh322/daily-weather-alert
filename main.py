



# https://api.openweathermap.org/data/2.5/weather?q=Mumbai,%20India&appid=61a9a80ec2158c62c6d1dc084c84343a


import requests
import smtplib
from email.message import EmailMessage


smtp_id = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'gshaikh32@gmail.com'
smtp_password = 'fvkc tnze dpno nteh'
from_addr = 'gshaikh32@gmail.com'
to_addr = 'gshaikh322@gmail.com'

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = '61a9a80ec2158c62c6d1dc084c84343a'


parameters ={
    'lat':19.075983, 
    'lon':72.877655, 
    'appid' : api_key,
    "cnt": 6
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

is_raining = False
raining_details = []
for weather_data in data['list']:
    if weather_data['weather'][0] ['id'] < 600 and weather_data['rain']['3h'] >= 0.5 and weather_data['pop'] >= 0.6:
        is_raining = True
        raining_details.append([weather_data['dt_txt'],weather_data['rain']['3h'],weather_data['pop']])

if is_raining:
    message = ""
    for details in raining_details:
        message += f'🕒 Date & time: {details[0]}\n  🌧 Rain Amount : {details[1]}mm\n  ☔ Rain Chance : {details[2]*100:.2f}%\n\n' 
        
    msg = EmailMessage()
    msg['Subject'] = 'It is raining'
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg.set_content(message)
    
    with smtplib.SMTP(smtp_id, smtp_port) as connection:
        connection.starttls()
        connection.login(smtp_user, smtp_password)
        connection.send_message(msg)
    
    print('mail sent')
    
else:
    print('No rain')
        


