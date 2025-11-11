def calculate_total_energy(disks):
    total_energy = sum(disk.energy_used for disk in disks)
    return total_energy
