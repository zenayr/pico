const int ledPins[] = {11, 12, 13, 14, 15};
const int photocellPin = A0;
int sensorValue = 0;
int Level = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int i = 0; i < 5; i++)
  {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(photocellPin);
  Level = map(sensorValue, 0, 1023, 0, 5);
  Serial.println(Level);
  delay(10);
  for(int i = 0; i < 5; i++)
  {
    if(i <= Level)
    {
      digitalWrite(ledPins[i], HIGH);
    }
    else
    {
      digitalWrite(ledPins[i], LOW);
    }
  }
}
