---
weight: 330
title: "Hardware"
description: "Otrona system hardware"
icon: "save"
date: "2024-04-22T13:09:11+02:00"
lastmod: "2024-04-22T13:09:11+02:00"
---

## Motherboard

Model: 40-051201


Motherboard requires all power rails and the POK signal in order to boot.
For testing on the bench, you can use an ATX PSU to generate -12V, 5V and 12V. You will also need to put 5V on the POK line.

Luckily it uses no custom chips, all the custom logic is implemented with bipolar PROMs. These can be dumped and duplicated, albeit programmers are hard to come by...
So far the only hard to replace part I've seen is the 12.324 MHz crystal for the video clock

There is a RTC powered by 2 button cells, that tend to leak... On this board, it leaked but luckily the corrosion is minimal.

### ROMs

5 ROMs on the motherboard
* U110: MMI 6349-1J = Signetics 82S147
* U252: Fujitsu MBM2732A-30
* U413: MMI 6301-1J = Signetics 82S129
* U416: Fujitsu MBM2732A-30
* U603: MMI 6301-1J = Signetics 82S129

On early revisions, some legs are bent and soldered together on U603.

| Marking | Role          | Version | MD5                              |
| ------- | ------------- | ------- | -------------------------------- |
|   U110  | Addressing    | -       | 96c6dc408701904ad929c7ec9211a7ca |
|   U252  | Boot ROM      | D       | 2db2b51c07f2412b51531a3d4c3c21b1 |
|     ^   | ^             | F       | f9975873e30494aae32c8cb5385156a4 |
|     ^   | ^             | G       | fdb4e89990238beabdd423f8868203b9 |
|     ^   | ^             | H       | 29b42cb020ce64b4a7e7accb5bf182db |
|   U413  | Video logic   | 012 A   | 39c7f651cab979a9ec576608675d0c91 |
|   U416  | Character ROM | CG 500  | 346258b1cc3e3e88fa7e7e0b6a1984e7 |
|   U603  | Floppy logic  | ?       | 66bab56ccd7aeaba863f99ed0a2ede0c |
|     ^   | ^             | 011 A 2 | 32fdaa5a4f23d858cf3578df0564e145 |

## PSU

```
Model: 40-051202 REV A
```

**Usual caution regarding high voltages apply here.**
**Please be safe**

Contrary to most computers from the time period using an Astek PSU, this uses a fully custom PSU.
It supports multiple input voltages:
> Switching style power supply that operates from 95 to 135 volts or 190 to 27b volts, 48 to 440 Hz.

It is documented in the Otrona Attaché Technical Manuel (1983):
- 1-8: Setting input voltage
- 2-57: Theory of operations
- A-8: Schematics

Despite the sandwich construction, everything can be taken apart easily and has connectors you can unplug.

Output voltages:
- 15V for the CRT board
- 12V
- 5V
- -12V

### Pinouts

#### J8: Motherboard connector

Reference: Molex 09507121 (KK 396 Series)

|    1 |    2 |     3 |         4 |     5 |    6 |   7 |    8 |   9 |  10 |   11 |   12 |
| ---- | ---- | ----- | --------- | ----- | ---- | --- | ---- | --- | --- | ---- | ---- |
| HDRV | VSYN | VIDEO | AUDIO GND | AUDIO | POK* | +5V | key? | GND | GND | +12V | -12V |

> POK: The power supply provides a Power Okay (POK) signal to the processor to initialize the system only when power is properly stabilized.

#### J5: Connector for CRT module

Reference: Molex 26192051 (KK 396 Series). Not an exact match but compatible.

|    1 |   2 |   3 |     4 |    5 |
| ---- | --- | --- | ----- | ---- |
| VSYN | GND | +15 | VIDEO | HDRV |

#### J6: Floppy power connector

Reference: Molex 26192081 (KK 396 Series). Not an exact match but compatible.

|    1 |    2 |   3 |   4 |   5 |   6 |   7 |   8 |
| ---- | ---- | --- | --- | --- | --- | --- | --- |
| +12V | +12V | GND | GND | +5V | GND | GND | +5V |

## Display

### Capacitors

Electrolytic capacitor list:
| Marking | Volt | Cap    | Diameter | Pitch | Notes         |
| ------- | ---- | ------ | -------- | ----- | ------------- |
| C1      | 50V  | 100µF  | 10mm     | 5mm   |               |
| C4      | 16V  | 1000µF | 13mm     | 5mm   |               |
| C8      | 16V  | 1000µF | 13mm     | 5mm   |               |
| C9      | 100V | 47µF   | 10mm     | 5mm   |               |
| C10     | 63V  | 10µF   | 10mm     | 5mm   |               |
| C17     | 25V  | 10µF   | 16.2mm   | 7mm   | **Bipolar**   |
| C18     | 25V  | 10µF   | 16.2mm   | 7mm   | **Bipolar**   |
| C19     | 50V  | 100µF  | 13mm     | 7mm   | 25V in manual |
| C23     | 100V | 47µF   | 10mm     | 5mm   | 63V in manual |
| C24     | 100V | 47µF   | 10mm     | 5mm   | 63V in manual |

Values match the schematics in technical manual, section A-10

Here's a simple Mouser BOM. I have not checked ESR requirements

| Qt | Desc             | Mouser ref        |
| -- | ---------------- | ----------------- |
| 3  | 100V 47µF        | 647-UHE2A470MPD   |
| 2  | 16V 1000µF       | 647-UHE1C102MHD6  |
| 2  | 25V 10µF Bipolar | 667-ECE-A1HN100UB |
| 2  | 50V 100µF        | 647-UPM1H101MPD6  |
| 1  | 63V 10µF         | 647-UCS2C100MPD   |

## Keyboard

Identifiers:
- PCB id: 40-051206 REV A "512 KEYBOARD3"

Observations:
- C3 is not populated, matches schematics
- Slider holes have been manually enlarged

Uses only CMOS logic, gets 12V from the motherboard. Communication uses serial