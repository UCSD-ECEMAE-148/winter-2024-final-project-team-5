<div id="top"></div>

<h1 align="center">Self-parking</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    <img src="images\UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>MAE148 Final Project</h3>
<p>
Team 4 Winter 2024
</p>

![image](https://github.com/UCSD-ECEMAE-148/winter-2024-final-project-team-5/blob/4deec9ce180e4f91449cba1c78bae674d76b20a8/images/The%20car.jpg)
</div>
# Winter-2024-Final-Project-Team-5
# MAE 148 Final Project Team 5

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

## Current Result: Live Demonstration

## The Result: What We Have Done
- Successfully trained a custom parking space model using Roboflow YOLO (You Only Look Once) 
- Successfully ran the parking recognition node
- Callibrated the existing lane following node to maintain a centered path throughout the parking space 

## Hardware Components
- CAD, 3D printed, and laser cut parts
- Parking spot

## Software Components - OpenCV
- Parking sign recognition and parking line recognition:
  >
  >We took ~250 images of our parking spot from different angles and lighting conditions and uploaded it to Roboflow. In Roboflow, we manually classified our images and distinguished between the parking sign and the parking lines. Then, we trained all the images using Roboflow YOLO.
> 

- Roboflow model integration with Jetson:
  >
  > We were provided our model's code, which we later integrated into our Jetson for preliminary testing. 

## Software Components - ROS
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

## Challenges Faced:

1. Failing to start the lane following node after successfully completing the lane recognition node.
   - Potential Reason:
     Two nodes trying to connect to one camera simultaneously.
   - Actions Taken:
     1. Attempted to stop the lane recognition node from accessing the OAK-D Lite Camera.
     2. Manually provided access to OAK-D Lite in our code for the lane following node.

## Actual Result: Live Demonstration

## Future Improvements If Given More Time:

1. Implementing another node that would subscribe to the parking recognition node, and then run the lane following node (instead of having two nodes in one)
2. Improving our understanding of ROS to solve current problems.
3. Adding lidar for automatic obstacle avoidance functionality.


**Speical thanks to Prof. Silberman, our TA Arjun Naageshwaran, Triton AI, and our amazing classmates for supporting and guiding us throughout the course and final project!**
