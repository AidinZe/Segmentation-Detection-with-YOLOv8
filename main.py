import cv2
import sys
from libs import YOLOSeg
import mimetypes

# Initialize YOLO Instance Segmentator
model_path = "models/yolov8m-seg.onnx"

try:yoloseg = YOLOSeg(model_path, conf_thres=0.3, iou_thres=0.3)
except: raise Exception('''copy yolov8m-seg.onnx file after create with colab link 
You can convert the Pytorch model to ONNX using the following Google Colab notebook: https://colab.research.google.com/drive/1oDEKz8FUCXtW-REhWy5N__PgTPjt3jm9?usp=sharing
''')
mimetypes.init()
if sys.argv[(sys.argv).index('--input')+1] == 'camera':format='camera'
else:format = mimetypes.guess_type(sys.argv[(sys.argv).index('--input')+1])[0].split('/')[0]

match format:
    case 'image':
        img = cv2.imread(sys.argv[(sys.argv).index('--input')+1])
        # Detect Objects
        boxes, scores, class_ids, masks = yoloseg(img)
        # Draw detections
        combined_img = yoloseg.draw_masks(img)
        cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
        cv2.imshow("Detected Objects", combined_img)
        try:
            if sys.argv[(sys.argv).index('--output')+1] != None:
                cv2.imwrite(sys.argv[(sys.argv).index('--output')+1], combined_img)
        except:
            if '--output' in sys.argv :cv2.imwrite("detected_objects.jpg", combined_img)
        # except:pass
        cv2.waitKey(0)
    case 'video':
        cap = cv2.VideoCapture(sys.argv[(sys.argv).index('--input')+1])
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        if '--output' in sys.argv :
            try:out = cv2.VideoWriter(sys.argv[(sys.argv).index('--output')+1], fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
            except: out = cv2.VideoWriter('detected_objects.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
        frame_countdown = 10
        while cap.isOpened():
            # Press key q to stop
            if cv2.waitKey(1) == ord('q'):
                break
            # Read frame from the video
            ret, frame = cap.read()
            if not ret:
                break
            # Update object localizer
            boxes, scores, class_ids, masks = yoloseg(frame)
            combined_img = yoloseg.draw_masks(frame, mask_alpha=0.4)
            if '--output' in sys.argv : out.write(combined_img)
            cv2.imshow("Detected Objects", combined_img)
        cap.release()
        if '--output' in sys.argv :out.release()
    case 'camera':
        # Initialize the webcam
        cap = cv2.VideoCapture(0)
        cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        if '--output' in sys.argv :
            try:out = cv2.VideoWriter(sys.argv[(sys.argv).index('--output')+1], fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
            except: out = cv2.VideoWriter('detected_objects.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        while cap.isOpened():
            # Read frame from the video
            ret, frame = cap.read()
            if not ret:
                break
            # Update object localizer
            boxes, scores, class_ids, masks = yoloseg(frame)
            combined_img = yoloseg.draw_masks(frame)
            if '--output' in sys.argv : out.write(combined_img)
            cv2.imshow("Detected Objects", combined_img)
            # Press key q to stop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        if '--output' in sys.argv :out.release()
    case _ :
        print('''
Yolo8 object detector:
Help: -h
--input: input file location like image or video or camera 
--output: for save result to file 
              
click on q to exit

examples:
    [python --input img.jpg]
    [python --input vid.mp4]
    [python --input camera ]
    [python --image img.jpg --output resultfile]
            ''')
