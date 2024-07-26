import shutil
import uuid
import paho.mqtt.client as paho

class StorageMonitor:
    def __init__(self, machine_id: uuid.UUID, disk_path: str):
        self.machine_id: uuid.UUID = machine_id
        self.mqtt_client = paho.Client()
        self.mqtt_client.connect("localhost", 1883, 60)
        self.mqtt_client.publish(f"sensor/{self.machine_id}/Disk_Usage", payload=("hot".encode()), qos=1)
        print(f"Audit broker on `sensor/{self.machine_id}/Disk_Usage`")
        self.disk_path : str = disk_path
        self.max_avaliable_storage : int = shutil.disk_usage(self.disk_path).total
        self.used_storage : int = 0

    def get_storage_limit(self) -> int :    
        return self.max_avaliable_storage
    
    def get_storage_usage(self) -> int :
        return self.used_storage
    
    def get_disk_path(self) -> str:
        return self.disk_path

    def trace_sensor(self) -> None:
        self.used_storage = shutil.disk_usage(self.disk_path).used