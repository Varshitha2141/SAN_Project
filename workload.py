import random

def generate_workload(num_disks, num_requests):
    """Simulates read/write requests with random distribution."""
    requests = []
    for t in range(num_requests):
        disk_id = random.randint(0, num_disks - 1)
        requests.append((t, disk_id))
    return requests
