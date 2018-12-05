#include <Servo.h>

Servo MiServo;

void setup() {
  // put your setup code here, to run once:
  MiServo.attach(13); //Asociar el servo al pin digital 13
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<181; i++){
    MiServo.write(i); // Mover el eje a la posición "i" grados  
    delay(100);
  }
}
