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

## Code

- Code to train yolov8 model : 'Sorting_batteries_yolov8.ipynb'
- Code to run in epsonrc7+ : 'main.prg'
- Code to integrate to real robot or epsonRC simulation : 'Epson_batterysorter.ipynb'
- YoloV8 batterysorter model weight : 'best.pt'

## Dataset

The dataset used for training and testing the system is available at [Train Data & Test Data](https://drive.google.com/drive/folders/1BnLuf_FTUME0__BmJJTMBvCkZ9AJFn8p?usp=sharing). The dataset includes images of AA, D, and 9V batteries in various orientations and lighting conditions.

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

1. Clone the GitHub repository to your local machine.
2. Download the dataset and place it in the appropriate directory.
3. Install the necessary dependencies as specified in the repository.
4. Run the main script to start the automated sorting process.

## Demo Video

A demo video showcasing the project in action : https://drive.google.com/file/d/1I7iv5gXTgrSRGcimD6vkMtcWSzNzqXBR/view?usp=sharing



