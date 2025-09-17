#include <Stepper.h> 

int speedRpm = 10;
Stepper myStepper(2048, 8, 10, 9, 11);

void setup() {
  // put your setup code here, to run once:
  myStepper.setSpeed(speedRpm);
}

void loop() {
  // put your main code here, to run repeatedly:
    myStepper.step(2048);
    delay(1000);
    myStepper.step(-2048);
    delay(1000);
}
