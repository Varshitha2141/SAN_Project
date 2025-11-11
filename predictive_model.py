def predict_idle_times(history, threshold):
    """Predict idle disks based on past access frequency."""
    predicted_idle = []
    for disk_id, access_times in history.items():
        if len(access_times) > 1:
            avg_gap = sum(
                access_times[i+1] - access_times[i]
                for i in range(len(access_times)-1)
            ) / (len(access_times) - 1)
            if avg_gap > threshold:
                predicted_idle.append(disk_id)
    return predicted_idle
