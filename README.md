<div id="top"></div>

<h1 align="center">Self-Parking</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    <img src="images\UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>MAE148 Final Project</h3>
<p>
Team 5 Winter 2024
</p>

![image](https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/6929f160445d6561245db45c150a4be29c21ca07/images/The%20Car1.jpg)
</div>

# Members
- Kaustubh Kanagalekar (MAE)
- Yingxiao Dai (ECE)
- Songyuan Lu (MAE)
- Zongyu Gao (MAE)


## The Plan: What We Promised
The goal of our group was to develop a self parking feature for an autonomous car using the knowledge and techniques learned in MAE 148. Our planned features included parking space recognition and self-parking capability. 

### Must-Have Features:
- Parking space recognition: recognizes parking signs and lines.
- Self parking feature: parks into a detected parking spot.

### Nice-to-Have Features:
We were planning to implement the following after we had successfully implemented our primary goals of the project (time permitting)
- Barrier avoidance: stops when collision risk is detected.
- Automatic search for available parking spaces.


## The Result: What We Have Done
- Successfully trained a custom parking space model using Roboflow YOLO (You Only Look Once) 
- Successfully ran the parking recognition node
- Callibrated the existing lane following node to maintain a centered path throughout the parking space 

## Hardware Components
- CAD, 3D printed, and laser cut parts
- Parking spot
### CAD Parts

#### Custom Designed Parts
| Part | CAD Model | Designer |
|------|--------------|------------|
| Baseboard | <img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/761f4fbad7697aade6f82330b155216b09f7b4f9/images/Baseboard.jpg" width="300" height="300" /> | Zhongyu Gao
| Camera Stand | <img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/761f4fbad7697aade6f82330b155216b09f7b4f9/images/Camera%20Stand.jpg" width="300" height="400" /> | Zhongyu Gao and Songyuan Lu
| Camera Mount Case | <img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/761f4fbad7697aade6f82330b155216b09f7b4f9/images/Camera%20Mount%20Case.jpg" width="300" height="300" /> | Songyuan Lu
| GPS Stand | <img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/435cf3ad5e03ad05f420351e6aab87ea520d4244/images/GPS%20Stand.jpg" width="300" height="300" /> | Songyuan Lu


#### Open Source Parts
| Part | CAD Model |
|------|--------|
| Jetson Nano Case (https://www.thingiverse.com/thing:3518410/files)| <img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/df742d72a3439a81e6644fc7235f817b851dae68/images/Jetson%20case.jpg" width="400" height="300" /> |


### Electronic Hardware
Below is a circuit diagram of the electronic hardware setup for the car.

<img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/5054c2fe5a73bdfd244b4e41bc6ad95910b975a2/images/MAE_148_Circuit_Diagram.png" width="800" height="400" />

### Handmade Parking Spot
Below is our simple parking space made out of cardboard and tape.

<img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/5a36feaa16d6065728c84d80c65d331129db72b5/images/Parking%20Spot.jpg" width="800" height="400" />

## Software Components 
### Embedded Linux (using Jetson Nano)
- We accessed the Jetson Nano using remote ssh connections to program and run our files. We were provided a ROS docker image that contained all dependencies needed to run ROS2, and we used that to simplify our workflow environment.
 
### OpenCV
- Parking sign recognition and parking line recognition:
  >
  >We took ~250 images of our parking spot from different angles and lighting conditions and uploaded it to Roboflow. In Roboflow, we manually classified our images and distinguished between the parking sign and the parking lines. Then, we trained all the images using Roboflow YOLO.
> 

- Roboflow model integration with Jetson:
  >
  > We were provided our model's code, which we later integrated into our Jetson for preliminary testing. 

### Docker and ROS2
- UCSD Robocar
  >
  > We used the ROS2 image pulled from Docker Hub and implemented the UCSD Robocar module created by Dominic Nightingale. This module provided access to the Lane Following node, which was used in our final project
  >
- Roboflow Model Integration into ROS Node
  >
  > We used the provided Docker containers (that contained the ROS software) to create a new directory called `selfparking` in the `/home/projects/ros2_ws/src` file path. In `selfparking`, we created a new ROS node called `parking_recog.py`, where we established a node framework and implemented our trained model from Roboflow. We also adjusted our code in the `launch` files and `setup.py` to account for the addition of our node.
  > 
- Lane Following into ROS Node
  >
  > We calibrated an existing Lane Following node to match the lines of our parking spot. We changed our HSV (Hue Saturation Values), Masked values, and our PID values to successfully navigate across the parking spot. Our primary objective was to ensure that the car would traverse through the spot until it would lose track of the parking lines (after which it would stop).
  >
  >PID values control the car's steering, stability, and speed. P incidates proportial, which is used to make a faster reaction to steering. I indicates integral, which is used to balance out any errors. D is derivative, which is used to smoothen the path. The optimal PID values that we found were P = 0.8, I = 0.0, D = 0.1.
  >
- Programming using ROS
  >
  > We added a condition that would try to deploy the lane following node after a certain confidence criteria was met (if confidence was greater than 0.3).

### Roboflow
- Data collection
  > We took 128 pictures include different angles and lighting of parking sign and parking lines at a paralle level to the camera on the car, annotated and used as a training data base in Roboflow.
- Training and Testing
  > We trained the model with the following method: Roboflow 3.0 Object Detection (Fast) and tested with OAK-D Lite directly connects to our laptop.
<img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/7d6fb97ff5de9c96c4a43c693b99dbebe13fcd04/images/Robo.jpg" width="800" height="400" />
<img src="https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/71a4162488d268de207e538d79c5aaefbf4ff053/images/Roboflow.jpg" width="800" height="400" />

## Challenges Faced:

1. Failing to start the lane following node after successfully completing the lane recognition node.
   - Potential Reason:
     Two nodes trying to connect to one camera simultaneously.
     >
     > We found that trying to run two nodes simultaneously in one file was problematic because of camera calibrations. For some reason, our parking recognition node was not disconnecting the camera after the detection was successful, which then propagated when the lane following node ran.
     > 
   - Actions Taken:
     1. Attempted to stop the lane recognition node from accessing the OAK-D Lite Camera.
        > We tried to break the node before starting the lane following node.
        
     3. Manually provided access to OAK-D Lite in our code for the lane following node.

2. Difficult to regonize the parking sign with a set distance.
   - Potential Reason:
    > We could not make sure the distance that the camera captured the parking sign is constant with different starting points. This created difficulties for the car to park into the spot accurately.
   
     


## Future Improvements If Given More Time:

1. Implementing another node that would subscribe to the parking recognition node, and then run the lane following node (instead of having two nodes in one)
2. Improving our understanding of ROS to solve current problems.
3. Adding lidar for automatic obstacle avoidance functionality.

Presentation (https://docs.google.com/presentation/d/1O7GzlUYajRHGXAjfatCKQfCSyGZsMRoO2xx1VeOBMCA/edit?usp=sharing)

**Speical thanks to Prof. Silberman, our TA Arjun Naageshwaran, Triton AI, and our amazing classmates for supporting and guiding us throughout the course and final project!**
