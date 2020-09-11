# CarProject
This project allows the user to:
* Assemble a smart car
* Wiring up your car and raspberry pi
* Run an object detection model in raspberry pi
* Wire up an ultra sonic sensor

## Credits:
This project is a compilation of 3 different tutorials on the internet:
1. Object Detection on Raspberry Pi [EdjeElectronics](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git)
2. Motor Control Raspberry Pi [Sentdex Series](https://www.youtube.com/watch?v=LlFkybEQFFA&t=330s)
3. Ultrasonic sensor w/ Raspberry Pi [ThePiHut](https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)


## EQUIPMENT:
1. [Raspberry Pi](https://www.amazon.com/gp/product/B07V5JTMV9/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)
2. [Rapberry Pi Camera](https://www.amazon.com/gp/product/B01ER2SKFS/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1)
3. [Smart Car Chassis](https://www.amazon.com/gp/product/B06VTP8XBQ/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
4. [L298N Motor Controller](https://www.amazon.com/gp/product/B014KMHSW6/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
5. [Ultrasonic Sensor](https://www.amazon.com/WMYCONGCONG-HC-SR04-Ultrasonic-Distance-Measuring/dp/B07JJHCVRG/ref=sr_1_1_sspa?crid=WOVIM2MQMKG5&dchild=1&keywords=ultrasonic+sensor&qid=1599608113&s=hi&sprefix=ultrasonic+sen%2Ctools%2C188&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFZMFZDWE1IWkgyN0smZW5jcnlwdGVkSWQ9QTAwMTQwNTgzSkQxQ001U0RFNkNSJmVuY3J5cHRlZEFkSWQ9QTA2NTEyMTQzNFgzQjM4RUE0M0tCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
6. [Breadboard & Jumper Wires](https://www.amazon.com/FTCBlock-Breadboards-Arduino-Distribution-Connecting/dp/B07H326BFQ/ref=sr_1_10?crid=YCA8NIITP1S&dchild=1&keywords=breadboard+jumper+wires&qid=1599608180&s=hi&sprefix=bread%2Ctools%2C184&sr=1-10)
7. [Coral TPU](https://www.amazon.com/Google-G950-01456-01-Coral-USB-Accelerator/dp/B07S214S5Y/ref=sr_1_2?dchild=1&keywords=coral+tpu&qid=1599608247&sr=8-2)

## Usage
(First run)
Open up a terminal and type:

``` 
git clone {this_repo_url}
cd carProject
python3 -m venv carProject-venv
source carProject-venv/source/bin/activate
bash get_pi_requirements.sh
python3 TFLite_detection_webcam.py --modeldir= Sample_TFLite_model 
```
(Every other time after that)
Open up a terminal and type:
``` 
cd carProject 
source carProject-venv/source/bin/activate
python3 TFLite_detection_webcam.py --modeldir= Sample_TFLite_model 
```

If you have an edgetpu
``` 
cd carProject 
source carProject-venv/source/bin/activate
python3 TFLite_detection_webcam.py --modeldir= Sample_TFLite_model --edgetpu
```


## Custom Model
I trained a custom traffic sign model using transfer learning 
The model is available in the custom folder. To run it instead of the generic .tflite
``` 
cd carProject 
source carProject-venv/source/bin/activate
python3 TFLite_detection_webcam.py --modeldir= custom_model --graph=road_signs_quantized_edgetpu.tflite --labels=label_map.txt --edgetpu 
```
If you dont have a tpu you'd just run
``` 
python3 TFLite_detection_webcam.py --modeldir= custom_model --graph=road_signs_quantized_edgetpu.tflite --labels=label_map.txt  
```

## The Tabby-Car
<img src="https://user-images.githubusercontent.com/50864401/92965349-41a80680-f43b-11ea-97ee-28422588765a.jpg" height="50%" width="50%">

## Future Plans:
1. Make a schematic for the entire project (At the moment you'll have to review all 3 tutorials)
2. Clean-up and upload the transfer learning python script 
3. Make a demo of the car in motion
