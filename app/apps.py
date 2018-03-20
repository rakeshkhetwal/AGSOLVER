from __future__ import unicode_literals

from django.apps import AppConfig

import paho.mqtt.client as mqtt



class AppConfig(AppConfig):
    name = 'app'


def on_connect(client, userdata, flags, rc):
	'''
		Handles the response generated when client successfully
		connects with the data provider
	'''
	print("connected %s" % (str(rc)))
	client.subscribe("raindata")


def on_message(client, userdata, msg, request):
	data = msg.payload
	print("msg.paylod:",str(data))
    return render(request, 'dashboard.html', {'data': data})


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("iot.eclipse.org", 1883, 60)
    client.loop_forever()