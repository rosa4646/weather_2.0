from bs4.element import TemplateString
from bs4 import BeautifulSoup
import requests
import yagmail
from win10toast import ToastNotifier
import schedule
import time 

toast = ToastNotifier()

def weather_func():
    global temp
    global temperature  
    url = f"https://www.google.com/search?q=weather+city+state"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    temp = soup.find_all('div', attrs={"class": "BNeawe iBp4i AP7Wnd"})
    temperature = int(temp[0].text.strip("°F"))
    if temperature <=32:
        snow_func() 
        print(temperature)

yag = yagmail.SMTP('email', 'password')

def snow_func():
    toast.show_toast(
    "Snow Warning",
    "Temperature outside is at 32 or lower :(",
    duration = 20,
)
    yag.send('email', "weather report", str(temperature))

schedule.every().day.at("1:00").do(weather_func)
while True:
    schedule.run_pending()
    time.sleep(1)
