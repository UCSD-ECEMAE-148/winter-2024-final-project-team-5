import rclpy
from rclpy.node import Node
from roboflowoak import RoboflowOak
import cv2
from cv_bridge import CvBridge
import time
import numpy as np

NODE_NAME = "parking_recog"

class RoboflowOakNode(Node):
    def __init__(self):
        super().__init__('parking_recog')

        # Instantiate an object (rf) with the RoboflowOak module
        self.rf = RoboflowOak(model="mae-148-self-parking", confidence=0.05, overlap=0.5,
                               version="2", api_key="ssA9Dj7MBjdiKIswWG6v", rgb=True,
                               depth=True, device=None, blocking=True)
        self.run()

    def run(self):
        # Running the model and displaying the video output with detections

        while rclpy.ok():
            t0 = time.time()
            # The rf.detect() function runs the model inference
            result, frame, raw_frame, depth = self.rf.detect()
            predictions = result["predictions"]
            self.get_logger().info("ran predictions")
            # timing: for benchmarking purposes
            t = time.time() - t0

            # setting parameters for depth calculation
            # comment out the following 2 lines if you're using an OAK without Depth
            max_depth = np.amax(depth)
            cv2.imshow("depth", depth/max_depth)

            # displaying the video feed as successive frames
            cv2.imshow("frame", frame)
            self.get_logger().info("FPS: {:.2f}".format(1/t))
            self.get_logger().info("PREDICTIONS: {}".format([p.json() for p in predictions]))


            # how to close the OAK inference window / stop inference: CTRL+q or CTRL+c
            if cv2.waitKey(1) == ord('q'):
                break

def main(args=None):
    rclpy.init(args=args)
    parking_recog = RoboflowOakNode()
    try:
        rclpy.spin(parking_recog)
        parking_recog.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        parking_recog.get_logger().info(f'Shutting down {NODE_NAME}...')

        # Kill cv2 windows and node
        cv2.destroyAllWindows()
        parking_recog.destroy_node()
        rclpy.shutdown()
        parking_recog.get_logger().info(f'{NODE_NAME} shut down successfully.')

if __name__ == '__main__':
    main()