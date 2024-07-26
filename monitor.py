import uuid
import machineid
import RAMMonitor
import StorageMonitor

# Path 
path = "D:/"
machine_id = uuid.UUID(machineid.id())

ram_monitor : RAMMonitor.RAMMonitor = RAMMonitor.RAMMonitor(machine_id)
storage_monitor : StorageMonitor.StorageMonitor = StorageMonitor.StorageMonitor(machine_id, path)

ram_monitor.trace_sensor()
storage_monitor.trace_sensor()

print(f"RAM Usage: {ram_monitor.get_ram_usage()}/{ram_monitor.get_ram_limit()}")
print(f"Disk: {storage_monitor.get_disk_path()} Usage: {storage_monitor.get_storage_usage()}/{storage_monitor.get_storage_limit()}")
