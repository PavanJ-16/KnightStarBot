char t;
 int del=0;
 int spe=150;
void setup() {
pinMode(5,OUTPUT);   //left motors  forward
pinMode(6,OUTPUT);   //left motors reverse
pinMode(10,OUTPUT);   //right  motors forward
pinMode(11,OUTPUT);   //right motors reverse
//pinMode(9,OUTPU;   //Led
Serial.begin(9600);
 
}
 
 void forward()
{
  analogWrite(5,spe);
  analogWrite(6,0);
  analogWrite(10,spe);
  analogWrite(11,0);

  Serial.println("Forward");
  delay(del);
}

void backward()
{
  analogWrite(5,0);
  analogWrite(6,spe);
  analogWrite(10,0);
  analogWrite(11,spe);

  Serial.println("Backward");
  delay(del);
}

void right()
{
  analogWrite(5,spe);
  analogWrite(6,0);
  analogWrite(10,0);
  analogWrite(11,0);
  
  Serial.println("Right");
  delay(del);
}

void left()
{
  analogWrite(5,0);
  analogWrite(6,0);
  analogWrite(10,spe);
  analogWrite(11,0);

  Serial.println("Left");
  delay(del);
}

void stop()
{
  analogWrite(5,0);
  analogWrite(6,0);
  analogWrite(10,0);
  analogWrite(11,0);

  Serial.println("Stop");
}

void forwardright()
{
  analogWrite(5,spe);
  analogWrite(6,0);
  analogWrite(10,spe/4);
  analogWrite(11,0);

  Serial.println("Forward-right");
  delay(del);
}

void forwardleft()
{
  analogWrite(5,spe/4);
  analogWrite(6,0);
  analogWrite(10,spe);
  analogWrite(11,0);

  Serial.println("Forward-left");
  delay(del);
}

void backwardleft()
{
  analogWrite(5,0);
  analogWrite(6,spe);
  analogWrite(10,spe);
  analogWrite(11,0);

  Serial.println("Backward-left");
  delay(del);
}

void backwardright()
{
  analogWrite(5,spe);
  analogWrite(6,0);
  analogWrite(10,0);
  analogWrite(11,spe);

  Serial.println("Backward-right");
  delay(del);
}

void loop() {
if(Serial.available()){
  t = Serial.read();
  Serial.println(t);
}
 
if(t == 'F'){            //move  forward(all motors rotate in forward direction)
  forward();
}
 
else if(t == 'B'){      //move reverse (all  motors rotate in reverse direction)
  backward();
}
  
else if(t == 'L'){      //turn right (left side motors rotate in forward direction,  right side motors doesn't rotate)
  left();
}
 
else  if(t == 'R'){      //turn left (right side motors rotate in forward direction, left  side motors doesn't rotate)
  right();
}


 
else {      //STOP (all motors stop)
  stop();
}
}
