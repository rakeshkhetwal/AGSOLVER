from django.shortcuts import render

# Create your views here.
from .models import data

from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,ListView,DetailView
# Create your views here.
import paho.mqtt.client as mqtt
import urllib, json, pprint
url = "http://api.openweathermap.org/data/2.5/forecast?q=Jaipur,In&APPID=441b16598b36d83ef8f3aece908b37e1"
#url = "http://api.openweathermap.org/data/2.5/weather?q=Jaipur,In&APPID=441b16598b36d83ef8f3aece908b37e1"

response = urllib.urlopen(url)
datas = json.loads(response.read())
#data=datas['list'][0]['main']['humidity'] #one time period day data it shows temp,  humidity, pressure
#pprint.pprint(data);
xyz=datas['list'][0]['weather'][0]['description']  # description
pprint.pprint(xyz)

def on_message(client, userdata, msg):
    dataa = msg.payload
    print("msg.paylod:", str(data))

    form = data(name="Ramu",  moisture_content=dataa, land_size="4000",
    place="jaipur", cropgrown="Arhar")
    #print("aaygayes")
    form.save()

#print("msg.paylod:",str(data))

def on_connect(client, userdata, flags, rc):
	'''
		Handles the response generated when client successfully
		connects with the data provider
	'''
	print("connected %s" % (str(rc)))
	client.subscribe("moisture")




def index(request):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("iot.eclipse.org", 1883, 60)
    client.loop_forever()
    return render(request,"dashboard.html")




def indexs(request):
    form = data.objects.all()
    return render(request,"dashboard.html", {"data":form, "humidity":datas['list'][0]['main']['humidity'],
    "temperature":datas['list'][0]['main']['temp'] ,"pressure" : datas['list'][0]['main']['pressure'],
     "climate":datas['list'][0]['weather'][0]['description'],

    "humidityone" : datas['list'][8]['main']['humidity'], "temperatureone":datas['list'][8]['main']['temp'] ,
    "pressureone" : datas['list'][8]['main']['pressure'], "climateone":datas['list'][8]['weather'][0]['description'],

    "humiditytwo": datas['list'][16]['main']['humidity'],"temperaturetwo": datas['list'][16]['main']['temp'],
    "pressuretwo": datas['list'][16]['main']['pressure'], "climatetwo":datas['list'][16]['weather'][0]['description'],

    "humiditythree": datas['list'][24]['main']['humidity'], "temperaturethree": datas['list'][24]['main']['temp'],
     "pressurethree": datas['list'][24]['main']['pressure'], "climatethree":datas['list'][24]['weather'][0]['description'],

                                        })





'''
if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("iot.eclipse.org", 1883, 60)
    client.loop_forever()
'''