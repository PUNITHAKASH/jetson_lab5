import jetson.inference
import jetson.utils
import cv2
from ui_stark import draw_hud

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0") 
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
    img = camera.Capture()
    if img is None: continue

    detections = net.Detect(img)
    frame = jetson.utils.cudaToNumpy(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    for detection in detections:
        class_name = net.GetClassDesc(detection.ClassID)
        # 77 = Phone, 44 = Bottle
        is_anomaly = (detection.ClassID == 77 or detection.ClassID == 44)
        frame = draw_hud(frame, detection, class_name, is_anomaly)
        
        if is_anomaly:
            cv2.putText(frame, "!!! ANOMALY !!!", (50, 80), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0,0,255), 3)

    output = jetson.utils.cudaFromNumpy(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    display.Render(output)
