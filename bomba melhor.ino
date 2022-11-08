//Programa: Display LCD 16x2 e modulo I2C
//Autor: Arduino e Cia

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

//Inicializa o display no endereco 0x27
LiquidCrystal_I2C lcd(0x3F, 16, 2);
char cmd;
char resposta;
void setup() {
  Serial.begin(9600);
  lcd.init();
  pinMode(13, OUTPUT);
}

void loop() {
  lcd.clear();
  cmd = Serial.read();
  if (cmd == 's') {
    lcd.setBacklight(HIGH);
    lcd.setCursor(0, 0);
    lcd.print("Fire in the Hole!!");
    for (int i=60;i>=0;i--){
      cmd=Serial.read();
      lcd.setCursor(0, 1);
      lcd.print(i);
      //lcd.scrollDisplayLeft();
      delay(1000);
      lcd.clear();
      if (i==0){
        lcd.clear();
        lcd.setBacklight(HIGH);
        lcd.setCursor(0, 0);
        lcd.print("Bombaaa!!");
        lcd.setCursor(0, 1);
        lcd.print("Que pena, morreu... =X");
        digitalWrite(13, HIGH);
        delay(2000);
      }
      if (i==30){
        lcd.setCursor(0, 0);
        lcd.print("correee!!");
      }
      if (i==25){
        lcd.clear();
      }
      if (cmd == 'a'){
        lcd.clear();
        lcd.setBacklight(HIGH);
        lcd.setCursor(0, 0);
        lcd.print("Vivaaaa!!");
        delay(40000);
        i=-1;
      }     
    }
  }   
}