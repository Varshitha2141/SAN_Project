class Disk:
    def __init__(self, disk_id, active_power=10, idle_power=2, spinup_time=5):
        self.id = disk_id
        self.active_power = active_power
        self.idle_power = idle_power
        self.spinup_time = spinup_time
        self.state = "idle"  # states: active, idle, spun_down
        self.last_access = 0
        self.energy_used = 0

    def access(self, time):
        """Simulate a disk access (read/write)."""
        if self.state == "spun_down":
            self.energy_used += self.active_power * self.spinup_time  # spin-up energy
            self.state = "active"
        self.last_access = time

    def update_state(self, time, idle_threshold):
        """Update the disk state based on inactivity time."""
        if self.state == "active" and time - self.last_access > idle_threshold:
            self.state = "idle"
        elif self.state == "idle" and time - self.last_access > idle_threshold * 2:
            self.state = "spun_down"

    def consume_energy(self):
        """Energy consumption per time unit."""
        if self.state == "active":
            self.energy_used += self.active_power
        elif self.state == "idle":
            self.energy_used += self.idle_power
        elif self.state == "spun_down":
            self.energy_used += 0.2  # minimal standby power
