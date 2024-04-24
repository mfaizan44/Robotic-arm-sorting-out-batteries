# Robotic arm sorting out batteries

This project uses an Epson VT6 robot with YOLOv8 for differentiating AA, D, and 9V batteries. YOLOv8 helps the robot identify and categorize batteries in real-time, enhancing sorting efficiency. The study also integrates an electromagnet into the robotic arm for better battery handling, showcasing potential for sustainable battery management and recycling.

## Introduction

The goal of this project is to develop a robotic system capable of accurately sorting different types of batteries, including AA, D, and 9V batteries, in an industrial setting. The system uses an Epson VT6 robot equipped with an electromagnetic gripper, along with yolov8, to detect and classify batteries.

## Features

- Automated sorting of AA, D, and 9V batteries.
- Utilizes visual and depth sensors for object detection.
- Yolov8 - from scratch trained model for differentiating three types of batteries 
- Real-time sorting and classification of batteries.
- Improved efficiency and accuracy compared to manual sorting methods.

## Flow Chart


## Code

- Code to train yolov8 model : 'Sorting_batteries_yolov8.ipynb'
- Code to run in epsonrc7+ : 'main.prg'
- Code to integrate to real robot or epsonRC simulation : 'Epson_batterysorter.ipynb'
- YoloV8 batterysorter model weight : 'best.pt'

## Dataset

The dataset used for training and testing the system is available at [Train Data & Test Data](https://drive.google.com/drive/folders/1BnLuf_FTUME0__BmJJTMBvCkZ9AJFn8p?usp=sharing). The dataset includes images of AA, D, and 9V batteries in various orientations and lighting conditions.

We assembled a comprehensive dataset comprising 1581 training images, each containing up to 9 batteries, and 194 validation images to develop and evaluate our models. Additionally, we created a separate test set of 109 new images to assess the model's performance in novel environments. This diverse dataset is crucial for training and validating robust deep learning models tailored for battery classification tasks.


## Requirements

- Epson VT6 robot
- Electromagnetic gripper.
- Camera
- YOLOv8 object detection model.
- Python programming language.
- EpsonRC+ Software
- Batteries : AA, D type, 9v

## Usage

To use the system, follow these steps:


1.Establish connection and setup between the robot and electromagnetic gripper.
2.Ensure communication between the robot and your PC using appropriate protocols.
3.Use Epson RC+ simulation software to check or teach pickup and drop-off points.
4.Connect the camera to your PC.
5.Clone the GitHub repository to your local machine.
6.Download the dataset and place it in the appropriate directory.
7.Install required dependencies as specified in the repository.
8.Connect the gripper to the Epson VT6 robot.
9.Open the Python program in your editor (e.g., VSCode/Jupyter Notebook).
10.Run the main program on Epson RC+ software, ensuring it's connected to the robot.

## Demo Video

A demo video showcasing the project in action : https://drive.google.com/file/d/1I7iv5gXTgrSRGcimD6vkMtcWSzNzqXBR/view?usp=sharing

## Github Link

https://github.com/mfaizan44/Robotic-arm-sorting-out-batteries

## Final setup

![WhatsApp Image 2024-04-24 at 22 48 51_a9c69827](https://github.com/mfaizan44/Robotic-arm-sorting-out-batteries/assets/131945639/a7011b6e-3a78-4c85-b224-02141d0870d9)



