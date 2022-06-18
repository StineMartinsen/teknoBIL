//Motorshield
#include <AFMotor.h> 

//Motors 
AF_DCMotor rightMotorFront(1); 
AF_DCMotor rightMotorBack(4); 

AF_DCMotor leftMotorFront(2);
AF_DCMotor leftMotorBack(3);

//INPUT PINS
int drive = A3;
int reverse = A5;
int leftTurn = 2;
int rightTurn = 13;

//BOOLS
int go = 0;
int back = 0;
int left = 0;
int right = 0;


//SPEEDS
int drivingSpeed = 1000;
int turningSpeed = 1000;
//int turningBot = 100;

void setup() {
  Serial.begin(9600); // set up Serial library at 9600 bps
  Serial.println("4 motors!");
  
  //SET PINS 
  pinMode(drive,INPUT);
  pinMode(reverse, INPUT);
  pinMode(leftTurn, INPUT);
  pinMode(rightTurn, INPUT);
  
  //TURN ON MOTORS
  speedSet("both", drivingSpeed);
  speedSet("both", 0);
}

//DRIVE FORWARD FUNCRION
void forward(){
    speedSet("both", drivingSpeed);
    rightMotorFront.run(BACKWARD);
    rightMotorBack.run(BACKWARD);

    leftMotorFront.run(FORWARD);
    leftMotorBack.run(FORWARD);
    Serial.println("GO");
}

//Function for settin drivingspeed
void speedSet(String motors, int whichSpeed){
  if(motors == "right"){
    rightMotorFront.setSpeed(whichSpeed);
    rightMotorBack.setSpeed(whichSpeed);
  }
  else if(motors == "left"){
  leftMotorFront.setSpeed(whichSpeed);
  leftMotorFront.setSpeed(whichSpeed);
  }
  else if(motors = "both"){
    rightMotorFront.setSpeed(whichSpeed);
    rightMotorBack.setSpeed(whichSpeed);
    
    leftMotorFront.setSpeed(whichSpeed);
    leftMotorFront.setSpeed(whichSpeed);

    if(whichSpeed == 0){
      rightMotorFront.run(RELEASE);
      rightMotorBack.run(RELEASE);
      
      leftMotorFront.run(RELEASE);
      leftMotorBack.run(RELEASE);
    }
  }
}


//RUNNING LOOP
void loop() {
  //UPDTAING THE BOOLS
  go = digitalRead(drive);
  back = digitalRead(reverse);
  left = digitalRead(leftTurn);
  right = digitalRead(rightTurn);


 //FORWARD DRIVE
  if(go && !back){    
    //FORWARD WITH A RIGHT TURN
    if(right){
      speedSet("right",turningSpeed);
    }
    //FORWARD WITH A LEFT TURN
    else if(left){
      speedSet("left",turningSpeed);
    }
    else{
      forward();
    }
  }

  
  //REVERSE
  else if(back && !go){
    //REVERSE WITH RIGHTTURN
    if(right){
      speedSet("right",turningSpeed);
    }
    //REVERSE WITH LEFTTURN
    else if(left){
      speedSet("left", turningSpeed);
    }
    else{
      speedSet("both", drivingSpeed);
    
      rightMotorFront.run(FORWARD);
      rightMotorBack.run(FORWARD);
      
      leftMotorFront.run(BACKWARD);
      leftMotorBack.run(BACKWARD);
      
      Serial.println("REVERSE");
    }
  }



 //RIGHTTURN
  else if(right && !go && !back){
    speedSet("both", turningSpeed);
    if(!left){
      rightMotorFront.run(FORWARD);
      rightMotorBack.run(FORWARD);

      leftMotorFront.run(FORWARD);
      leftMotorFront.run(FORWARD);
      
      Serial.println("RIGHTTURN");
    }
    //IF YOU PRESS BOTH LEFT AND RIGHT
    else{
      forward();
    }
  }



  //LEFTTURN
  else if(left && !go && !back){
    speedSet("both", turningSpeed);
    if(!right){
      leftMotorFront.run(BACKWARD);
      leftMotorBack.run(BACKWARD);
      
      rightMotorFront.run(BACKWARD);
      rightMotorBack.run(BACKWARD);
      Serial.println("LEFTTURN");
    }
  
  //IF YOU PRESS BOTH LEFT AND RIGHT
    else{
      forward();
    }
  }

  //IF YOU DON'T PRESS ANYTHNIG
  else{
    speedSet("both", 0);
    Serial.println("STOP");
 }
}
