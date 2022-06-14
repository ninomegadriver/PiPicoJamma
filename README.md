# PiPicoJamma
## A Jamma board all about Raspberry Pi  
  
"PiPico Jamma", a Raspberry Pi based arcade board.  
  
Inputs are handled using Raspbery PI Pico as keyboard emulator and keys mapped according to Mame / Advance Mame defaults.  
  
RGB output via VGA666 interface, with resistor values tunned for better contrast on legacy arcade monitors.  
  
Built-in slot for PAM8610 module with Volume pot. Audio can be mono via Jamma pins or stereo via external speaker connectors  
  
Link: [PiPico Jamma on PCBWay](https://www.pcbway.com/project/shareproject/PiPico_Jamma_d2a98783.html)
  
PCB Version 1.1:  
![PiPicoJamma 1.1 Front](https://github.com/ninomegadriver/PiPicoJamma/raw/main/PiPicoJamma_pcb-front.png)
![PiPicoJamma 1.1 Back](https://github.com/ninomegadriver/PiPicoJamma/raw/main/PiPicoJamma_pcb-back.png)
  
  
Acual 1.0. board picture:  
![PiPicoJamma 1.0 Actual picture](https://github.com/ninomegadriver/PiPicoJamma/raw/main/PiPicoJamma_pcb-1.0.jpg)  
  
  
## RPI4 Single Game Image  
  
A single game RPI4 image created with Buildroot 2022.02.1 with fully hardware accelation support and a custom optimized build of Advance Mame 3.9.  
  
Uncompress [rpi4_single_game.7z](https://github.com/ninomegadriver/PiPicoJamma/raw/main/rpi4_single_game.7z) and burn it to a 512mb or bigger sdcard. Remount the card and put your game rom in the "[boot]/rom" folder. Open config.txt and uncomment the "hdmi_timings" according to your game's resolution. Unmount, plug the sdcard to your RPI4 and have fun.  
  
  
