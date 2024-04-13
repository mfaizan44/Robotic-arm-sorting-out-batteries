import cv2
import os

def create_directory(directory_path):
    """Create a directory if it doesn't already exist."""
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
        print(f"New directory created: {directory_path}")

def capture_and_save_image(camera_id=1, directory="Battery Sorter", image_file="Battery.jpg"):
    
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
    else:
        print("No image was captured from the camera.")

    # Release the camera resources
    camera.release()

if __name__ == "__main__":
    # Execute the function with default parameters
    capture_and_save_image(camera_id=1, directory="Battery Sorter", image_file="Battery.jpg")

