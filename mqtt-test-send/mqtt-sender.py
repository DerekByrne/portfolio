import paho.mqtt.client as mqtt
import time
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

def publish(client):
     msg_count = 1
     while True:
         time.sleep(1)
         msg = f"messages: {msg_count}"
         result = client.publish(topic, msg)
         # result: [0, 1]
         status = result[0]
         if status == 0:
             print(f"Send `{msg}` to topic `{topic}`")
         else:
             print(f"Failed to send message to topic {topic}")
         msg_count += 1
         if msg_count > 5:
             break

# Replace these with your broker's details
broker_address = "192.168.0.56"
broker_port = 1883  # Adjust if your broker uses a different port
topic = "python/mqtt_test"
username = MQTT_USERNAME
password = MQTT_PASSWORD

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set username and password if required by your broker
client.username_pw_set(username, password)



def run():
    client.connect(broker_address, broker_port)
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
