# Pi Pico Keyboard code for PiPico Jamma PCB
  
Here are provided two Raspberry Pi Pico keyboard codes for use with the "PiPico Jamma" project, one using CircuitPython and another using the Arduino IDE. I strongly recommend using the pre-build [PiPico_Keyboard.uf2](https://github.com/ninomegadriver/PiPicoJamma/raw/main/PiPico_Keyboard/PiPico_Keyboard.uf2) for better reliability and performance.  
  
<B>NOTE</B>: Key mappings according to Mame's default keys, but bear in mind that
Mame dosen't have default keys for Player2 button 6 and Advance Mame dosen't have
defaults for Player2 buttons 4, 5 and 6.  
  
  
## Pre-build .UF2

- While holding the "boot" button pressed on your Raspberry Pi Pico, connect it to your computer.  
- After a new removable drive appears, just copy the provided [PiPico_Keyboard.uf2](https://github.com/ninomegadriver/PiPicoJamma/raw/main/PiPico_Keyboard/PiPico_Keyboard.uf2) to it.  
  
## Arduino IDE Version   

- Install Arduino IDE 1.x and add this to your File->Preferences->"Additional Boards Manager URLs":
https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
- Select the right board for your in Tools->Board
- Open "PiPico_Keyboard.ino" compile and upload to your board
  
  
## CircuitPython Version:  
  
- Install CircuitPython 7.2 or higher in your Pi Pico and copy over all files in this package to your "CIRCUITPY" drive.  
  
  
