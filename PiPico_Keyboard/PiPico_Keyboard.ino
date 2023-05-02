/*
* RaspberryPi Pico Keyboard code for use with "PiPico Jamma":
* https://github.com/ninomegadriver/PiPicoJamma
*
* Nino MegaDriver, 2022
* nino@nino.com.br
* http://www.megadriver.com.br
*
* Key mappings according to Mame's default keys.
* Bear in mind that Mame dosen't have default keys
* for Player2 button 6 and Advance Mame dosen't have
* defaults for Player2 buttons 4, 5 and 6.
* 
* You'll have to configure these on Mame according
* to this Code
*
* Use the "arduino pico" board core.
* Add this to your File->Preferences->"Additional Boards Manager URLs":
* https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
*
*/

#include <Keyboard.h>

// Raspberry Pi Pico GPIOs
uint8_t pins[] = {
    0,    // GPIO0:  Service
    1,    // GPIO1:  Test
    2,    // GPIO2:  COIN2
    3,    // GPIO3:  COIN1
    4,    // GPIO4:  P2 START
    5,    // GPIO5:  P1 START
    6,    // GPIO6:  P2 UP
    7,    // GPIO7:  P1 UP
    8,    // GPIO8:  P2 DOWN
    9,    // GPIO9:  P1 DOWN
    10,   // GPIO10: P2 LEFT
    11,   // GPIO11: P1 LEFT
    12,   // GPIO12: P2 RIGHT
    13,   // GPIO13: P1 RIGHT
    14,   // GPIO14: P2 BTN1
    15,   // GPIO15: P1 BTN1
    16,   // GPIO16: P2 BTN6
    17,   // GPIO17: P2 BTN5
    18,   // GPIO18: P2 BTN4
    19,   // GPIO19: P1 BTN6
    20,   // GPIO20: P1 BTN5
    21,   // GPIO21: P1 BTN4
    22,   // GPIO22: P1 BTN3
    26,   // GPIO23: P2 BTN3
    27,   // GPIO24: P1 BTN2
    28    // GPIO25: P2 BTN2
};

// Keys correspondent to each GPIO:
const uint8_t keys[] = {
    KEY_F2,               // F2:           SERVICE
    '9',                  // 9:            TEST 
    '6',                  // 6:            COIN2
    '5',                  // 5:            COIN1
    '2',                  // 2:            P2 START
    '1',                  // 1:            P1 START
    'r',                  // R:            P2 UP
    KEY_UP_ARROW,         // ARROW UP:     P1 UP
    'f',                  // F:            P2 Down
    KEY_DOWN_ARROW,       // ARROW DOWN:   P1 Down
    'd',                  // D:            P2 LEFT
    KEY_LEFT_ARROW,       // ARROW LEFT:   P1 LEFT
    'g',                  // G:            P2 RIGHT
    KEY_RIGHT_ARROW,      // ARROW RIGHT:  P1 RIGHT
    'a',                  // A:            P2 BTN1
    KEY_LEFT_CTRL,        // LEFT CONTROL: P1 BTN1
    'h',                  // H:            P2 BTN6
    'e',                  // E:            P2 BTN5
    'w',                  // W:            P2 BTN4
    'x',                  // X:            P1 BTN6
    'z',                  // Z:            P1 BTN5
    KEY_LEFT_SHIFT,       // LEFT SHIFT:   P1 BTN4
    ' ',                  // SPACE:        P1 BTN3
    'q',                  // Q:            P2 BTN3
    KEY_LEFT_ALT,         // LEFT ALT:     P1 BTN2
    's',                  // S:            P2 BTN2
};


void setup() {
  Keyboard.begin(); // Initialize the Keyboard

  // Set all GPIO to inputs with pullups
  for(uint8_t i=0;i<sizeof pins;i++) pinMode(pins[i], INPUT_PULLUP);

}

void loop() {
  // Loop within the loop for maximum speed
  while(true){
    // Check each GPIO
    for(uint8_t i=0;i<sizeof pins;i++){
       // if low, press, otherwise, release!
       if(digitalRead(pins[i]) == LOW) Keyboard.press(keys[i]);
       else Keyboard.release(keys[i]);  
    }
  }
}
