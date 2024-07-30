import uuid
import paho.mqtt.client as paho
import paho.mqtt.enums as paho_enums
import paho.mqtt.subscribe as subscribe

class SensorEndpoint:
    def __init__(self, machine_id : uuid.UUID, topic: str):
        self.machine_id = machine_id
        self.sensor_type = topic
        self.topic : str = f"sensor/{self.machine_id}/{self.sensor_type}"
        subscribe.callback(callback=self.fill_data, topics=self.topic, hostname="localhost", port=1883)
        self.active = True
        self.client_data: str = ""

    def fill_data(self, client : paho.Client, userdata: any, msg: paho.MQTTMessage) -> None:
        self.client_data = msg.payload.decode()
        print(f"msg received on topic: {self.sensor_type}")
        self.received_data = True

    def shutdown(self):
        self.active = False

    def get_message(self) -> str:
        return self.client_data
