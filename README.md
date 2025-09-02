
# PalmPilot
[![Demo Video](https://img.youtube.com/vi/qekNE9RpXIQ/0.jpg)](https://youtu.be/qekNE9RpXIQ)

PalmPilot is a computer vision-powered, hand gesture-controlled Arduino car. Using a webcam and AI, you can drive, steer, and stop the car with simple hand gestures—no physical remote required!

## Features

- Control car movement (forward, backward, left, right, stop) using hand gestures
- Real-time gesture recognition with computer vision (MediaPipe + OpenCV)
- Arduino-based motor control via serial communication
- Plug-and-play: just connect your Arduino and webcam

## How It Works

1. The Python script uses OpenCV and MediaPipe to detect hand gestures from your webcam.
2. Recognized gestures are mapped to car commands (e.g., open palm = forward, fist = stop).
3. Commands are sent to the Arduino over serial.
4. The Arduino receives commands and drives the motors accordingly.

## Getting Started

### Hardware

- Arduino board (Uno, Nano, etc.)
- Motor driver (L298N or similar)
- Webcam
- Motors and wheels
- USB cable

### Software

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- PySerial
- Arduino IDE

### Setup

1. **Clone the repository:**
	```sh
	git clone https://github.com/Rian-Sen/PalmPilot.git
	```
2. **Install Python dependencies:**
	```sh
	pip install opencv-python mediapipe pyserial
	```
3. **Connect your Arduino and upload `arduino.ino` using the Arduino IDE.**
4. **Update the serial port in `serial_connection.py` to match your system.**
5. **Run the Python script:**
	```sh
	python serial_connection.py
	```

## Hand Gestures

- **Open palm:** Move forward
- **Fist:** Stop
- **Middle finger up:** Move backward
- **Index finger up:** Turn right
- **Index + middle finger up:** Turn left

## File Structure

- `serial_connection.py` — Computer vision and gesture recognition logic
- `arduino.ino` — Arduino code for motor control
- `LICENSE` — MIT License
- `README.md` — Project documentation
- `Computer Vision Car Report.pdf` — Technical report

## License

MIT License © 2025 Rian Sen Majumder