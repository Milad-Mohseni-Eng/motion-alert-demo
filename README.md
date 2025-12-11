# motion-alert-demo
"MicroPython motion alert demo - LED blink + buzzer pulse(buttom trigger).


# Motion Alert Demo

A minimal, reproducible demo that triggers an LED blink + buzzer pulse pattern when a trigger input is asserted.  
This repository contains the MicroPython script for running the demo on a Raspberry Pi Pico (or similar RP2040 board).

---

## What this repo contains

- main.py — MicroPython program: reads a trigger input and produces LED blink + buzzer pulses.
- media/ — optional: include demo.mp4 (30–60s) and wiring photos.
- LICENSE — MIT License (suggested).

---

## Hardware (tested)

- Raspberry Pi Pico or compatible RP2040 board  
- LED + resistor (220Ω recommended)  
- Piezo buzzer (passive or active — tested with passive)  
- Push button (or jump wire as trigger)  
- Breadboard and jumper wires
- Power: USB from PC (3.3V/5V as required by board)

### Pin wiring (as used in main.py)

| Signal  | GPIO  | Physical pin |
|--------:|:-----:|:------------:|
| LED     | GP14  | 19           |
| Buzzer  | GP16  | 21           |
| Button  | GP28  | 34           |
| GND     | —     | 38           |
| 3V3     | —     | 36           |

*Button wiring (two-pin):* one leg → GP28, other leg → GND. (If you use internal pull-up/pull-down adjust code accordingly.)

---

## Usage

1. Open Thonny (or any MicroPython IDE) and connect your Pico.
2. Copy main.py to the Pico filesystem (save as /main.py on the device if you want it to run on boot).
3. Wire hardware exactly as above.
4. Press the button (or short the trigger pin to 3.3V if you are using a jump-wire trigger) — the LED will blink and the buzzer will pulse.

---

## Results / Measurements (add your numbers)

- Example latency (button → LED on): ____ ms  
- Example buzzer pattern duration: 10 pulses @ 50 ms  
- Notes about reliability: Add anything you measured here

---

## Troubleshooting

- If the button reads always 1 or always 0, verify wiring and GPIO choice. Try using a known-good GPIO (GP0–GP5).
- If buzzer is too quiet: lower series resistor (if present), increase pulse frequency or use an active buzzer.
- If LED is too dim: check resistor value and connection to GND.

---

## Adding demo video & images

- Put a short demo.mp4 (30–60s) in media/. If the video is large, add it as a GitHub Release or host externally (YouTube/GDrive) and link here.
- Add wiring photos in media/images/.

---

## License

MIT — see LICENSE.

---

## How to cite / use

Simple educational demo for teaching microcontroller I/O and prototyping. Feel free to fork and adapt.
