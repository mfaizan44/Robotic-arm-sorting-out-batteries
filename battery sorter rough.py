import cv2
import torch
import socket
import argparse
from Camera import Cam  # This module should handle camera operations

# Robot Control Constants
ESPON_ROBOT_IP = "192.168.150.2"
HOME_POS = (0, 524, 546)
PICKUP_Z = 150
DROP_Z = 277
OUTPUT_ON_COMMAND = "SET_OUTPUT 1\r\n"  # Command to turn on output module, customize based on actual command
OUTPUT_OFF_COMMAND = "SET_OUTPUT 0\r\n" # Command to turn off output module, customize based on actual command
DROP_POINTS = {
    'AA': (738, -284, DROP_Z),
    'D': (459, -284, DROP_Z),
    '9V': (459, 77.5, DROP_Z)
}

# YOLO Model Setup
class ObjectDetector:
    def __init__(self, model_name='yolov8', pretrained=True):
        self.model = torch.hub.load('ultralytics/yolov8', model_name, pretrained=pretrained)

    def detect(self, image_path):
        img = cv2.imread(image_path)
        results = self.model(img)
        return results.pandas().xyxy[0]  # DataFrame of [xmin, ymin, xmax, ymax, confidence, class, name]

# Epson Robot Controller
class EpsonController:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((ESPON_ROBOT_IP, 2001))
        self.clientSocket.settimeout(5)

    def send_command(self, command):
        print(f"Sending command: {command}")
        self.clientSocket.sendall(command.encode())
        return self.clientSocket.recv(1024).decode()

    def goto(self, x, y, z):
        command = f"GO {x} {y} {z}\r\n"
        if z == PICKUP_Z:
            self.send_command(OUTPUT_ON_COMMAND)  # Turn on output when reaching pickup height
        elif z == DROP_Z:
            self.send_command(OUTPUT_OFF_COMMAND)  # Turn off output when reaching drop height
        return self.send_command(command)

    def goHome(self):
        return self.goto(*HOME_POS)

def main():
    parser = argparse.ArgumentParser(description="Automate Epson robot for sorting batteries using YOLOv8.")
    parser.add_argument("--camera_index", type=int, default=0, help="Index of the camera for capturing images.")
    args = parser.parse_args()

    camera = Cam(args.camera_index)
    detector = ObjectDetector(pretrained=True)
    robot = EpsonController()

    try:
        while True:
            # Capture an image
            image_path = "output/current_frame.jpg"
            camera.take_picture(filename=image_path)

            # Detect objects
            detections = detector.detect(image_path)
            for index, detection in detections.iterrows():
                x_center = (detection['xmin'] + detection['xmax']) / 2
                y_center = (detection['ymin'] + detection['ymax']) / 2

                # Simulate world coordinate transformation
                x_world, y_world = x_center * 0.1, y_center * 0.1

                # Get the drop point for the detected object
                object_type = detection['name']
                drop_point = DROP_POINTS.get(object_type, DROP_POINTS['AA'])

                # Move robot to pick and drop the object
                robot.goto(x_world, y_world, PICKUP_Z)
                robot.goto(*drop_point)
                robot.goHome()

    except KeyboardInterrupt:
        print("Interrupted by user, shutting down.")
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
