
#define BLYNK_PRINT Serial

/* Fill in information from Blynk Device Info here */
//#define BLYNK_TEMPLATE_ID           "TMPxxxxxx"
//#define BLYNK_TEMPLATE_NAME         "Device"
//#define BLYNK_AUTH_TOKEN            "YourAuthToken"


#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>


char ssid[] = "SSID";
char pass[] = "PASS";


BLYNK_WRITE(V0)
{   
  int r = param.asInt(); 

digitalWrite(14,r);

}

BLYNK_WRITE(V1)
{   
  int g = param.asInt();
digitalWrite(14,g);

}

BLYNK_WRITE(V2)
{   
  int b = param.asInt(); 
digitalWrite(14,b);

}

void setup()
{

  Serial.begin(9600);
pinMode(14,OUTPUT);
pinMode(12,OUTPUT);
pinMode(13,OUTPUT);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop()
{
  Blynk.run();
}


