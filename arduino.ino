// MOTOR1 PINS
int ena = 5;
int in1 = 6;
int in2 = 7;
int in3 = 8;
int in4 = 9;
int enb = 10;

void setup() {
  Serial.begin(9600);

  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enb, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  stopMotors(); // Ensure motors are stopped at startup
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');

    if (input == "FORWARD") {
      moveForward();
    } else if (input == "STOP") {
      stopMotors();
    } else if (input == "BACKWARD") {
      moveBackward();
    } else if (input == "TURN_RIGHT") {
      turnRight();
    } else if (input == "TURN_LEFT") {
      turnLeft();
    }
  }
}

void moveForward() {
  // Start Motor A and B (Clockwise)
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(ena, 255);

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enb, 255);
}

void moveBackward() {
  // Start Motor A and B (Counter-Clockwise)
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(ena, 255);

  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enb, 255);
}

void turnRight() {
  // Motor A CW and Motor B CCW
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(ena, 255);

  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enb, 255);
}

void turnLeft() {
  // Motor A CWW and Motor B CW
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(ena, 255);

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enb, 255);
}

void stopMotors() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}
