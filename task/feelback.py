from paho import mqtt
import paho.mqtt.client as paho
from ..config import MQTTConfig
from ..schemas import UpdateFeelback
from ..cruds.feelback import CrudFeelback


class OPTIONS:
    CRUD: CrudFeelback = CrudFeelback()


class MqttClient:

    def __init__(self):

        self.client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
        # calback
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # confiuration
        self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        self.client.username_pw_set(MQTTConfig.USERNAME, MQTTConfig.PASSWORD)
        self.client.connect(MQTTConfig.BROKER_URL, MQTTConfig.BROKER_PORT)

        self.loop: bool = True

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print(f"[{flags['session present']}]-> broker feelback [mqtt] connecte. status: {rc}")
        # S'abonner au topic "hey" lors de la connexion
        client.subscribe("#", qos=2)

    def on_message(self, client, userdata, msg):
        content = msg.topic.split("/")
        OPTIONS.CRUD.update(
            feelback=UpdateFeelback(
                user_id=content[1], topic=content[0], message=msg.payload.decode()
            )
        )
        
    def publish(self, topic: str):
        self.client.publish(topic=topic)

    def loopMqttServerListener(self):
        self.client.loop_start()

    def stop(self):
        self.loop = False
        self.client.loop_stop()
        self.client.disconnect()


clientMq = MqttClient()
