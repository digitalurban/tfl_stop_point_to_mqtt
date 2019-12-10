
import requests
import json
from pprint import pprint
import paho.mqtt.client as mqtt

#Set up MQTT


print("creating new instance")
client = mqtt.Client("Bus Times") #  Create new instance
print("connecting to broker")
client.username_pw_set("publish", "Rg413hw%Publish")
client.connect("YOUR MQTT", 1883) #  Your MQTT Broker and Port


#Get Bus Stop Arrivals  - Change Stop Point for Chosen Location - ours is Goodge Street

response = requests.get('https://api.tfl.gov.uk/StopPoint/490000089A/Arrivals')

data = json.loads(response.text)


#Create List for Sorting
busarrivals = []


#Add Json Entries to List  - Buses

for entry in data:

    buses = []

    buses.append(int(entry['lineId']))
    buses.append ('to')
    buses.append(entry['destinationName'])
    buses.append ('in')
    buses.append (int(round(entry ['timeToStation']/60)))
    buses.append ('minutes')
    
         
    busarrivals.append(buses)             
      
#Sort the data by timeToStation
    
bussorted = sorted(busarrivals, key=lambda x: x[4])

#Reduce the List to the First 5 buses

first5 = (bussorted[:5])

#Convert to a String

first5a = str(first5)

#Clean up Characters for Printing

first5b = first5a.replace("'","")
first5c = first5b.replace(",","")
first5d = first5c.replace("[","\n")
first5e = first5d.replace("]","\n")

#replace phases '0 mintues' with 'is due' in text and '1 minutes' to '1 minute'

first5f = first5e.replace("in 0 minutes", "is due ")
first5g = first5f.replace("in 1 minutes", "in 1 minute ")  

#Set Output Message 

output = "Bus Arrivals Goodge Street Station:" + first5g


# Send to MQTT and Print to Screen
    
print("Publishing message to topic")
print (output)

client.publish("led/messages", output) #Yout Topic to Publish To - ours was Led/Messages
