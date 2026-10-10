I am going to be making a transport controller/macro pad to be used in all my favourite creative apps. 
The project will be on a single board. An array of 8 buttons will be available to perform different functions. 
For Ableton (DAW), it will output MIDI signals via USB and Ableton will read those as signals to record, or play, or solo a track, or undo, etc etc. One rotary encoder will scroll sideways through the timeline, and the other will zoom in/zoom out. Then, a toggle button will be able to switch between apps, and send keyboard signals instead. It will send both at once for cmd+z to undo. 3 LEDs will give a binary output of the number of the app mode I am in.

For the microcontroller, I'm going with a Rapsberry Pi Pico H (the variant with headers, so I can mount it in some sockets). I will therefore be able to program this in CircuitPython (Python is my main). Not as fast as some custom C epicness but never mind! 

Here is a render of the PCB!
<img width="804" height="599" alt="image" src="https://github.com/user-attachments/assets/11a3da5d-cae1-44b6-b33b-7965f253c2ed" />

And my original sketch:
<img width="1022" height="768" alt="Week 1 Plan to Scale" src="https://github.com/user-attachments/assets/215499f9-3015-418f-b306-d7924abaa59b" />
