# Segmentation Detection with YOLOv8 
 Python scripts performing instance segmentation using the YOLOv8 model in ONNX.

![! ONNX YOLOv8 Instance Segmentation](https://github.com/AidinZe/Segmentation-Detection-with-YOLOv8.git/doc/img/result.jpg)

*Original image:https://github.com/AidinZe/Segmentation-Detection-with-YOLOv8.git/doc/img/img.jpg*

# Important
- The input images are directly resized to match the input size of the model. I skipped adding the pad to the input image (image letterbox), it might affect the accuracy of the model if the input image has a different aspect ratio compared to the input size of the model. Always try to get an input size with a ratio close to the input images you will use.

# Requirements

 * Check the **requirements.txt** file.
 * For ONNX, if you have a NVIDIA GPU, then install the **onnxruntime-gpu**, otherwise use the **onnxruntime** library.

# Installation
```
git clone https://github.com/AidinZe/Segmentation-Detection-with-YOLOv8.git
cd Segmentation-Detection-with-YOLOv8
pip install -r requirements.txt
```
### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`


# How to Use

 * **Image inference**:
 ```
 python main.py --input {image}.jpg --output {result image}.jpg 
 ```

 * **Webcam inference**:
 ```
 python main.py --input camera --output {result video of camera}.mp4 
 ```

 * **Video inference**: 
 ```
 python main.py --input {video}.mp4 --output {result video}.mp4 
 ```
 ![!YOLOv8 instance segmentation video](https://github.com/AidinZe/Segmentation-Detection-with-YOLOv8.git/doc/vid/result.gif)
  *Original video:https://github.com/AidinZe/Segmentation-Detection-with-YOLOv8.git/doc/video/video.gif


# ONNX model
You can convert the Pytorch model to ONNX using the following Google Colab notebook:  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oDEKz8FUCXtW-REhWy5N__PgTPjt3jm9?usp=sharing)
- The License of the models is GPL-3.0 license: [License](https://github.com/ultralytics/ultralytics/blob/master/LICENSE)

# Original YOLOv8 model
The original YOLOv8 Instance Segmentation model can be found in this repository: [YOLOv8 Instance Segmentation](https://github.com/ultralytics/ultralytics)


# References:
* YOLOv8 model: https://github.com/ultralytics/ultralytics
* YOLOv5 model: https://github.com/ultralytics/yolov5
* YOLOv6 model: https://github.com/meituan/YOLOv6
* YOLOv7 model: https://github.com/WongKinYiu/yolov7
* yolov5-seg-opencv-onnxruntime-cpp: https://github.com/UNeedCryDear/yolov5-seg-opencv-onnxruntime-cpp
* PINTO0309's model zoo: https://github.com/PINTO0309/PINTO_model_zoo
* PINTO0309's model conversion tool: https://github.com/PINTO0309/openvino2tensorflow
