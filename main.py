from disk import Disk
from workload import generate_workload
from energy_model import calculate_total_energy
from predictive_model import predict_idle_times
import matplotlib.pyplot as plt

# Parameters
NUM_DISKS = 5
NUM_REQUESTS = 100
IDLE_THRESHOLD = 10

# Initialize disks
disks = [Disk(i) for i in range(NUM_DISKS)]
history = {i: [] for i in range(NUM_DISKS)}

# Generate workload
requests = generate_workload(NUM_DISKS, NUM_REQUESTS)

for t, disk_id in requests:
    disk = disks[disk_id]
    disk.access(t)
    history[disk_id].append(t)

    # Update disk states
    predicted_idle = predict_idle_times(history, IDLE_THRESHOLD)
    for d in disks:
        if d.id in predicted_idle:
            d.update_state(t, IDLE_THRESHOLD)
        d.consume_energy()

# Compute results
total_energy = calculate_total_energy(disks)
print(f"Total Energy Consumed: {total_energy:.2f} units")

# Plot energy per disk
plt.bar([d.id for d in disks], [d.energy_used for d in disks])
plt.title("Energy Consumption per Disk")
plt.xlabel("Disk ID")
plt.ylabel("Energy (units)")
plt.show()
