import cv2
import jetson_inference # Use underscore instead of dot if the first way fails
import jetson_utils
def draw_hud(frame, detection, class_name, is_anomaly):
    # Blue for Safe, Red for Anomaly
    color = (0, 0, 255) if is_anomaly else (255, 200, 0)
    l, t, r, b = int(detection.Left), int(detection.Top), int(detection.Right), int(detection.Bottom)
    
    # Draw Corner Brackets
    len_ = 25
    cv2.line(frame, (l, t), (l + len_, t), color, 3) 
    cv2.line(frame, (l, t), (l, t + len_), color, 3)
    cv2.line(frame, (r, t), (r - len_, t), color, 3) 
    cv2.line(frame, (r, t), (r, t + len_), color, 3)
    cv2.line(frame, (l, b), (l + len_, b), color, 3) 
    cv2.line(frame, (l, b), (l, b - len_), color, 3)
    cv2.line(frame, (r, b), (r - len_, b), color, 3) 
    cv2.line(frame, (r, b), (r, b - len_), color, 3)

    cv2.putText(frame, class_name.upper(), (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    return frame
