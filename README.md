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
- Parking sign recognition and parking line recognition
- Roboflow model integration with Jetson

## Software Components - ROS
- Roboflow Model Integration into ROS Node
- Lane Following into ROS Node
- Debugging on Hardware

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


**Speical thanks to Prof. Silberman, our TA Arjun Naageshwaran, Triton AI, and our amazing classmates for supporting and guiding us throught the course and final project!**
