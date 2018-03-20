#include<ESP8266WiFi.h>
#include<PubSubClient.h>
#include<SoftwareSerial.h>
#include<String.h>
// for the rain sensor

int inPin = 12;   // choose the input pin (for a pushbutton)
int val = 0;    // variable for reading the pin status

const char* ssid = "i";
const char* password = "fivestar";
const char* mqtt_server = "iot.eclipse.org"; //broker.mqtt-dashboard.com




WiFiClient espClient;
PubSubClient client(espClient);


int sensor_pin = A0;

int output_value ;

void setup() {
  pinMode(D3,OUTPUT);
  pinMode(D4,OUTPUT);
   Serial.begin(115200);    
  setup_wifi();
  client.setServer(mqtt_server, 1883);

   Serial.println("Reading From the Sensor ...");

   delay(2000);

   }



void setup_wifi() 
  {
    delay(10);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) 
    {
      delay(500);
      Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
  }

void reconnect() {
  while (!client.connected()) 
  {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP8266Client")) 
    {
      Serial.println("connected");
    }
    else 
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

   void moisture()
   {
    
   output_value= analogRead(sensor_pin);

   output_value = map(output_value,550,0,0,100);

   Serial.print("Mositure : ");

  

   client.publish("moisture", String(output_value).c_str(),true);
    Serial.print(output_value);
    if(output_value < -70){
      digitalWrite(D4, HIGH);
    }
    else{
      digitalWrite(D4, LOW);
    }
   
   Serial.println("%");
    delay(2000);

   

   }


   void rain(){
    val = digitalRead(inPin);  // read input value
  if (val == LOW){ 
    char msgs[25]="rainnot";
     digitalWrite(D3, LOW);
   
   // client.publish("raindata", msgs);

   
     Serial.println(msgs);
    delay(2000);
   // check if the input is HIGH (button released) CONNCECTION BREAK 
    //digitalWrite(ledPin, HIGH);  // turn LED OFF
    
  } else {
   char msgs[25]="rain";
     digitalWrite(D3, HIGH);
    //client.publish("raindata", msgs);
    Serial.println(msgs);
    delay(2000);
    
    //digitalWrite(ledPin, LOW);  // turn LED ON RAIN HAPPENING 
   
  }

   }

void loop() {

    if (!client.connected()) {
    reconnect();
  }


  rain();
  moisture();

   }
