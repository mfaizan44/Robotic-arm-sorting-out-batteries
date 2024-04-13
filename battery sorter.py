import cv2
import os
import torch
import torchvision.transforms as transforms
from PIL import Image

def create_directory(directory_path):
   
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
        print(f"New directory created: {directory_path}")

def load_model(model_path, device):
    """Load the YOLO model from the specified path."""
    model = torch.load(model_path)
    model.to(device)
    model.eval()
    return model

def process_image_with_yolo(image_path, model, device):
    """Process an image with the YOLO model to detect objects."""
    # Load image with PIL
    image = Image.open(image_path)
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    image = transform(image).unsqueeze(0).to(device)

    # Perform inference
    with torch.no_grad():
        predictions = model(image)

    return predictions

def capture_and_save_image(camera_id=1, directory="Battery Sorter", image_file="battery.jpg"):
    """Capture an image from the specified camera and save it to a directory."""
    # Verify and prepare the storage directory
    create_directory(directory)

    # Initialize the camera
    camera = cv2.VideoCapture(camera_id)
    if not camera.isOpened():
        print("Failed to access the camera.")
        return

    # Capture a single image
    success, image = camera.read()
    if success:
        # Show the captured image in a window
        cv2.imshow('Preview', image)

        # Construct the file path
        file_path = os.path.join(directory, image_file)
        # Save the image to the disk
        cv2.imwrite(file_path, image)
        print(f"Image has been saved at: {file_path}")

        # Wait for any key to be pressed before exiting
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Load and use the model
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = load_model("path_to_yolo_v8_model.pth", device)
        results = process_image_with_yolo(file_path, model, device)
        print(results)
    else:
        print("No image was captured from the camera.")

    # Release the camera resources
    camera.release()

if __name__ == "__main__":
    # Execute the function with default parameters
    capture_and_save_image(camera_id=1, directory="Battery Sorter", image_file="battery.jpg")


