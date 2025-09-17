const int switchPin = 14;
const int ledPin = 15;

int switchState = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(switchPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  switchState = digitalRead(switchPin);

  if(switchState == HIGH) {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
}
