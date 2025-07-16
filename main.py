from motor_control import move_forward, stop
from ultrasonic_sensor import is_obstacle_detected
from waste_detection import detect_waste
import time

def main():
    try:
        while True:
            if is_obstacle_detected():
                stop()
                print("Obstacle detected! Stopping...")
                time.sleep(2)
            elif detect_waste():
                print("Waste detected! Slowing down for collection...")
                move_forward(speed=30)
                time.sleep(3)
            else:
                move_forward()
            time.sleep(0.1)
    except KeyboardInterrupt:
        stop()
        print("Program stopped.")

if __name__ == "__main__":
    main()
