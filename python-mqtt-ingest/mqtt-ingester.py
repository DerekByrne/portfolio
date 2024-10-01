import paho.mqtt.client as mqtt
from mqtt_config import MQTT_USERNAME, MQTT_PASSWORD

def on_connect(client, userdata, flags, rc):
  # handle connection status
  if rc == 0:
    print("Connected!")
  else:
    print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
  # handle incoming messages
  print(f"Topic: {msg.topic}, Payload: {msg.payload}")

# Replace these with your broker's details
broker_address = "192.168.0.56"
broker_port = 1883  # Adjust if your broker uses a different port
username = MQTT_USERNAME
password = MQTT_PASSWORD

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set username and password if required by your broker
client.username_pw_set(username, password)

client.connect(broker_address, broker_port)

# Subscribe to topics
# Replace 'your_topic' with the topic you want to subscribe to
client.subscribe("#")

# Loop forever to keep the connection open
client.loop_forever()