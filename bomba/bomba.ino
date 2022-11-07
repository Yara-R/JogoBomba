//Programa: Display LCD 16x2 e modulo I2C
//Autor: Arduino e Cia

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

//Inicializa o display no endereco 0x27
LiquidCrystal_I2C lcd(0x3F, 16, 2);

int btnVerde = 4;
pinMode(btnVerde, INPUT_PULLUP);

pinMode(1, INPUT_PULLUP);
pinMode(2, INPUT_PULLUP);

void setup() {
  Serial.begin(9600);
  lcd.init();
}

void loop() {
  lcd.clear();
  if (iniciarBomba == 1) {
    lcd.setCursor(0, 0);
    lcd.print("Fire in the Hole!!");
    for (int i=0;i<10;i++){
      lcd.scrollDisplayLeft();
      delay(300);
    }
    lcd.print("Bombaaa!!");
    if (desafio1 == 1){
    lcd.setBacklight(HIGH);
    lcd.setCursor(0, 0);
    lcd.print("Bombaaa!!");
    lcd.setCursor(0, 1);
    lcd.print(iniciarBomba);
    delay(1000);
    //lcd.setBacklight(LOW);
    //a -= 1;
    }
  } 
}