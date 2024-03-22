# winter-2024-final-project-team-5
# MAE 148 Final Project Team 5

- Kaustubh Kanagalekar (MAE)
- Yingxiao Dai (ECE)
- Songyuan Lu (MAE)
- Zongyu Gao (MAE)

## Contents
1. What We Have Promised
2. Live Demonstration
3. What We Have Done

## The Plan: What We Promised
The goal of our group was to develop a self-parking feature for an electric car using the knowledge and techniques learned in MAE 148. Our planned features included parking space recognition, self-parking capability, barrier avoidance function, and automatic search for available parking spaces.

### Must-Have Features:
- Parking Space Recognition Function: Recognizes parking signs and lines.
- Self-Parking Feature: Parks into a detected parking spot.

### Nice-to-Have Features:
- Barrier Avoidance Function: Stops when collision risk is detected.
- Automatic Search for Available Parking Spaces.

## Current Result: Live Demonstration

## The Result: What We Have Done

## Hardware Components
- CAD & Laser Cutting Parts
- Parking Spot

## Software Components - OpenCV
- Parking Sign Recognition
- Parking Line Recognition
- Roboflow Model Integration with Jetson

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

1. Improve understanding of ROS to solve current problems.
2. Add lidar for automatic obstacle avoidance functionality.

## Future Improvements If Given More Time:

1. Improve understanding of ROS to solve current problems.
2. Add lidar for automatic obstacle avoidance functionality.

```

#Speical thanks to Prof. Silberman, our TA Arjun Naageshwaran, Triton AI, and our amazing classmates for supporting and guiding us throught the course and final project!#
