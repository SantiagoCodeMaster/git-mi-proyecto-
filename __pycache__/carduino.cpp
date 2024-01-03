// declaramos las variables del buzz para su OUTPUT y declaramos la salida INPUT del analogwrite  declaramos potVal y buzz que utilizaremos mas adelante tambien tenemos a dt que repite el codigo void loop
int buzzPin = 8;
int potPin = A0;
int potVal;
int buzz;
int ledPin = 7;

void setup() {
  // put your setup code here, to run once:
  //damos void setup para dar funcion a pinMode tanto a INPUT como OUTPUT y el parametro 9600 para leer 
  pinMode(potPin,INPUT);
  pinMode(buzzPin, OUTPUT);
  pinMode(ledPin,HIGH);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // declaramos la variable potVal como analogWrite de potpin y asi podemos leer la informacion de nuestro pocientometro , imprimimos potVal para leer en el monitor serial , declaramos la variable buzz con la funcion map que nos ayuda a establecer un parametro nuemrico donde su maximo es 1023  y el minimo es 0, y por otro lado  0,255
  potVal = analogRead(potPin);
  Serial.println(potVal);
   
  while (potVal > 1000){
    digitalWrite(buzzPin,HIGH);
    potVal = analogRead(potPin);
    digitalWrite(ledPin,HIGH);
  }
  digitalWrite(buzzPin,LOW);
  digitalWrite(ledPin,LOW);


}
