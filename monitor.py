import uuid
import machineid
import RAMMonitor
import StorageMonitor
from threading import Thread
import paho.mqtt.client as paho
import paho.mqtt.enums as paho_enums
import json
import time

def info_loop(delta_time: int):
    while(True):
        start : float = time.time()
        result = {
            "machine_id": f"{uuid.UUID(machineid.id())}",
            "sensors":[
                {
                    "sensor_id": "ram_usage",
                    "data_type": "float",
                    "data_interval": 100
                },
                {
                    "sensor_id": "disk_usage",
                    "data_type": "float",
                    "data_interval": 100
                }
            ]
        }

        json_result = json.dumps(result)
        mqtt_client = paho.Client(callback_api_version = paho_enums.CallbackAPIVersion.VERSION2)
        mqtt_client.connect("localhost", 1883, 60)
        mqtt_client.publish("/sensor_monitors", payload=(json_result.encode()), qos=1)
        end = time.time()
        time.sleep( (delta_time/1000.0) - (end - start))
    

# Path 
path = "D:/"
machine_id = uuid.UUID(machineid.id())

t = Thread(target=info_loop, args=(200,))
t.run()

ram_monitor : RAMMonitor.RAMMonitor = RAMMonitor.RAMMonitor(machine_id)
storage_monitor : StorageMonitor.StorageMonitor = StorageMonitor.StorageMonitor(machine_id, path)

ram_monitor.trace_sensor()
storage_monitor.trace_sensor()

print(f"RAM Usage: {ram_monitor.get_ram_usage()}/{ram_monitor.get_ram_limit()}")
print(f"Disk: {storage_monitor.get_disk_path()} Usage: {storage_monitor.get_storage_usage()}/{storage_monitor.get_storage_limit()}")
