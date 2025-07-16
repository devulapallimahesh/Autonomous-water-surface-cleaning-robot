import random

def is_obstacle_detected():
    distance = random.uniform(10, 100)  # Simulated distance in cm
    print(f"[SIMULATION] Distance: {distance:.2f} cm")
    return distance < 20