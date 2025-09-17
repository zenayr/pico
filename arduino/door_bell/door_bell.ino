#include "pitches.h"
//#include<cstdarg>
//#include<list>
//using namespace std;

int melody[] = {NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4};
int buttonPin = 14;
int noteDurations[] = {4, 8, 8, 4, 4, 4, 4,4};
//Melody test = new Melody((Note_C4, 4));

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int buttonState = digitalRead(buttonPin);

  if(buttonState == 1){
    for (int i = 0; i < 8; i++){
      int noteDuration = 1000 / noteDurations[i];
      tone(15, melody[i], noteDuration);
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
    }
  }
  else{
    noTone(15);
  }
}

//class Note{
//  public:
//  int note;
//  int duration;
//
//  Note(int note, int duration){
//    note = note;
//    duration = duration;
//  }  
//};
//
//class Melody{
//  public:
//  list<Note> notes;
//
//  Melody(int args, ...){
//    va_list valist;
//    va_start(valist, args);
//    for(int i = 0; i < args; i++){
//      notes.push_front(va_arg(valist, Note));
//    }
//    va_end(valist);
//  }
//};
