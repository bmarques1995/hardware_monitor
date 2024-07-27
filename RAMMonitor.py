import psutil
import uuid
import paho.mqtt.client as paho
import paho.mqtt.enums as paho_enums

class RAMMonitor:
    def __init__(self, machine_id: uuid.UUID):
        self.machine_id: uuid.UUID = machine_id
        self.mqtt_client = paho.Client(callback_api_version = paho_enums.CallbackAPIVersion.VERSION2)
        self.mqtt_client.connect("localhost", 1883, 60)
        self.mqtt_client.publish(f"sensor/{self.machine_id}/RAM_Usage", payload="hot", qos=1)
        print(f"Audit broker on `sensor/{self.machine_id}/RAM_Usage`")
        self.max_avaliable_ram : int = psutil.virtual_memory().total
        self.used_ram : int = 0

    def get_ram_limit(self) -> int :    
        return self.max_avaliable_ram
    
    def get_ram_usage(self) -> int :
        return self.used_ram
    
    def trace_sensor(self) -> None:
        memory_avaliable = psutil.virtual_memory().available
        self.used_ram = self.max_avaliable_ram - memory_avaliable
        
