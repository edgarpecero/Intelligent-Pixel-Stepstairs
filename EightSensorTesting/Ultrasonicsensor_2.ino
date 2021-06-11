#define trigPinx 2
/*#define trigPin1 2*/
#define echoPin0 3
#define echoPin1 5
#define echoPin2 6
#define echoPin3 7
#define echoPin4 8
#define echoPin5 9
#define echoPin6 10
#define echoPin7 11

long duration, distance, s0,s1,s2,s3,s4,s5,s6,s7,d1,d2,d3,d4,d5;

void setup()
{
Serial.begin (9600);
pinMode(trigPinx, OUTPUT);
pinMode(echoPin0, INPUT);
pinMode(echoPin1, INPUT);
pinMode(echoPin2, INPUT);
pinMode(echoPin3, INPUT);
pinMode(echoPin4, INPUT);
pinMode(echoPin5, INPUT);
pinMode(echoPin6, INPUT);
pinMode(echoPin7, INPUT);
}

void loop() {
SonarSensor(echoPin0);
s0 = distance;
d1 = duration;
SonarSensor(echoPin1);
s1 = distance;
d2 = duration;
SonarSensor(echoPin2);
s2 = distance;
d3 = duration;
SonarSensor(echoPin3);
s3 = distance;
d4 = duration;
SonarSensor(echoPin4);
s4 = distance;
SonarSensor(echoPin5);
s5 = distance;
SonarSensor(echoPin6);
s6 = distance;
SonarSensor(echoPin7);
s7 = distance;
d5 = duration;
Serial.print(s0);
Serial.print(" - ");
Serial.print(s1);
Serial.print(" - ");
Serial.print(s2);
Serial.print(" - ");
Serial.print(s3);
Serial.print(" - ");
Serial.print(s4);
Serial.print(" - ");
Serial.print(s5);
Serial.print(" - ");
Serial.print(s6);
Serial.print(" - ");
Serial.print(s7);
Serial.print(" - ");
Serial.println(" ");
Serial.println(d1);
Serial.println(d2);
Serial.println(d3);
Serial.println(d4);
Serial.println(d5);

}

void SonarSensor(int echoPin)
{
digitalWrite(2, LOW);
delay(100);
digitalWrite(2, HIGH);
delay(100);
digitalWrite(2, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;
}
