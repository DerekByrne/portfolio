# Portfolio project 

### Project overview
This project is for me to demonstrait my skills as a fullstack and IOT developer. 

To get this project to work:
- Clone the repo 
- Install docker desktop 
- Run the mqtt5 container
- Interact with the container 
```
docker compose exec mqtt5 sh
```
- Add a username
```
mosquitto_passwd -c /mosquitto/config/pwfile <USERNAME>
```
- Add password 
```
Password:
Reneter password:
```
- Exit the container 
```
exit
```
- add file to python-mqtt-ingest folder called 
```
mqtt_config.py
```
with your username and password

```
MQTT_USERNAME = <USERNAME>
MQTT_PASSWORD = <PASSWORD>
```

- In your terminal in the portfolio page run 
```
docker compose up --build
```

### Done 
 - Make docker compose file
 - Added Mosquitto for MQTT messages 
 - Added python script to sub to the mesages

 ### WIP
 - Add Postress to Docker compose
 - Add Prisma to the python MQTT ingester

 ### Next Todo 
 - set up Nextjs with prisma
 - Build simple frontend to chart IOT device values
