# MacroPad
This is my Hack Club Half Life Week 1: PCB Design Project.

This project is a transport controller/macro pad to be used in all my favourite creative apps. 

- Bill of Materials: [BOM.md](BOM.md)
- PCB Gerber File for Manufacture: [REAL ACTUAL Final GERBER.zip](https://github.com/TheWilliamGeorge/MacroPad/blob/main/REAL%20ACTUAL%20Final%20GERBER.zip)
- PCB Design (EasyEDA format): [Final_MacroPad_EasyEDA.json](https://github.com/TheWilliamGeorge/MacroPad/blob/main/Final_MacroPad_EasyEDA.json)
- .schdoc Format Schematic: [No-Matrix_2026-10-10.schdoc](https://github.com/TheWilliamGeorge/MacroPad/blob/main/No-Matrix_2026-10-10.schdoc)
- DXF format PCB Design: [PCB_Macro-Pad_2_2026-10-10.dxf](https://github.com/TheWilliamGeorge/MacroPad/blob/main/PCB_Macro-Pad_2_2026-10-10.dxf)
- Schematic Design (EasyEDA format): [SCH_Macro-Pad_2026-10-21.json](https://github.com/TheWilliamGeorge/MacroPad/blob/main/SCH_Macro-Pad_2026-10-21.json)
- Schematic Design (EasyEDA .epro2 raw source format): [PCB_MACRO PAD_2.epro2](https://github.com/TheWilliamGeorge/MacroPad/blob/main/PCB_Macro%20Pad_2.epro2)

I don't think I can export the schematic or PCB in any other format from EasyEDA, so you may have to open these in EasyEDA to see them.

*ONCE I'VE BUILT IT, AN IMAGE WILL GO HERE*

## What it is
The MacroPad will be comprised of a single PCB, which I have designed and will have printed by JLCPCB. An array of 8 Cherry MX-style key switches (brown) with MX-style keycaps will be available to perform different functions. A ninth button will be reserved for spacebar (play/pause), and a tenth for toggling between different app modes. 

## How it will work
For Ableton (DAW), it will output MIDI signals via USB and Ableton will read those as signals to record, or play, or solo a track, or undo, etc etc. One rotary encoder will scroll sideways through the timeline, and the other will zoom in/zoom out. 
In other apps like Final Cut Pro X (video editing), it will output keyboard signals. These will send presses of the common editing hotkeys I use. The encoders will do the same as in MIDI mode.

The current app mode will be denoted by a 3 LED binary display. These three LEDs will show the number of the app mode you are currently using, in binary. This way I can show up to 7 different app modes.

For the microcontroller, I'm going with a Rapsberry Pi Pico H (the variant with headers.) This means that I can use CircuitPython.

## Firmware
The firmware is programmed in CircuitPython using the KMK framework for the GPIO pin keypress detection/rotary encoder handling. KMK is also used to send the HDI keyboard/MIDI input signals via USB to the computer. I have written the entire firmware but will only be able to test whether it works once I get the actual hardware. So fingers crossed!

## The future
I will be building this in week 6 of Half Life. In Week 2, I designed an enclosure, which I will have 3D printed. In week 7, I will be assembling this enclosure and making it look nice and tidy! So that, in the end, I have a really sleek macro pad that I can use in my day-to-day computer use!

## Images
Here is a render of the PCB!
<img width="804" height="599" alt="image" src="https://github.com/user-attachments/assets/11a3da5d-cae1-44b6-b33b-7965f253c2ed" />

PCB full image:

<img width="396" height="316" alt="PCB_PCB_Macro-Pad_2_2026-10-21" src="https://github.com/user-attachments/assets/a5a9125e-a2f5-45cb-ad8d-cf1b805fb821" />

And my original sketch:
<img width="1022" height="768" alt="Week 1 Plan to Scale" src="https://github.com/user-attachments/assets/215499f9-3015-418f-b306-d7924abaa59b" />
