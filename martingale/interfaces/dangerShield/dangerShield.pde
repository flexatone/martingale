
const byte ledCharSet[10] = {  B00111111,B00000110,B01011011,B01001111,B01100110,B01101101,B01111101,B00000111,B01111111,B01101111
};

// Pin definitions
#define SLIDER1  0
#define SLIDER2  1
#define SLIDER3  2
#define BUTTON1  10
#define BUTTON2  11
#define BUTTON3  12
#define LED1 5
#define LED2 6
#define BUZZER 3
#define TEMP 4
#define LIGHT 3
#define KNOCK 5
#define LATCH 7
#define CLOCK 8
#define DATA 4

void setup() {
    Serial.begin(9600);
}

void loop () {

    // sliders 3, 2, 1 from left to right
    Serial.print('A', BYTE); // char 65
    //Serial.print(analogRead(SLIDER1)); 
    Serial.print(map(analogRead(SLIDER3), 0, 1023, 2000, 1000));
    Serial.print('\n', BYTE); // char 10

    Serial.print('B', BYTE); // char 66
    Serial.print(map(analogRead(SLIDER2), 0, 1023, 2000, 1000));
    Serial.print('\n', BYTE); // char 10

    Serial.print('C', BYTE); // char 67
    Serial.print(map(analogRead(SLIDER1), 0, 1023, 2000, 1000));
    Serial.print('\n', BYTE); // char 10


    Serial.print('D', BYTE); // char 68
    Serial.print(map(digitalRead(BUTTON1), 0, 1, 2000, 1000));
    Serial.print('\n', BYTE); // char 10

    Serial.print('E', BYTE); // char 69
    Serial.print(map(digitalRead(BUTTON2), 0, 1, 2000, 1000));
    Serial.print('\n', BYTE); // char 10

    Serial.print('F', BYTE); // char 70
    Serial.print(map(digitalRead(BUTTON3), 0, 1, 2000, 1000));
    Serial.print('\n', BYTE); // char 10


    //from 190 to 1000
    Serial.print('G', BYTE); // char 71
    Serial.print(map(analogRead(LIGHT), 190, 1000, 1000, 2000));
    Serial.print('\n', BYTE); // char 10

    // from 150 to 170 seem useful indoors
    Serial.print('H', BYTE); // char 72
    //Serial.print(analogRead(TEMP)); 
    Serial.print(map(analogRead(TEMP), 150, 170, 1000, 2000));
    Serial.print('\n', BYTE); // char 10

    Serial.print('I', BYTE); // char 73
    if (analogRead(KNOCK) > 10) {
        Serial.print(2000);
    }
    else {
        Serial.print(1000);
    }
    Serial.print('\n', BYTE); // char 10

    delay(30);

}


