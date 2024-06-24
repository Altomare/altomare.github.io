---
weight: 330
title: "Floppy Format"
description: "Otrona floppy disk geometry"
icon: "save"
---

## CP/M

Physical disk layout:
* Total capacity: 360k
* 48 TPI, 40 tracks
* 10 sector per track
* 512 bytes per sector
* Skew factor: 2. Sector order: 1 6 2 7 3 8 4 9 10
* Gap 3 is 20 bytes long

Notes:
* First 3 tracks of side 0 are reserved for CP/M
* The 4 last tracks of side 1 are unused
  * On some disks, tracks 76/77/78 are formatted. Why?

Logical layout:
```
0X0000 - 0x01FF (1 sector, 512)   = BIOS boot sector
0X0200 - 0x09FF (4 sectors, 2k)   = CCP
0X0A00 - 0x17FF (7 sectors, 3.5k) = BDOS
0x1800 - 0x3BFF (18 sectors, 9k)  = Rest of BIOS
```

On some 8:16 models, the machine uses a 96 TPI drive. For these machines, CP/M is still on 48 TPI disks and the BIOS sets up the drive as if it was 48 TPI.

### Relevant documentation

* [Technical Notes Manual](</documents/otrona/92-05-1210 - Otrona Attache Technical Manual (1.1).pdf>): Diskette format described in section 6.1 (page 60) 
* [Sources: BIOS 2.2.5 for 96 TPI drives](</files/otrona/source/BIOS25.ASM>): Sources for CP/M BIOS targetting 96 TPI drive machines

## Drives

The following drives are used on the default config:
* Remex RFD480
* TEAC FD-55B
* Canon, probably MDD-210 (to be confirmed)

I'm not sure which model is used on the 98 TPI machines

Schematics for the Remex and TEAC drives are available in the Technical manual

The drives need to have a READY signal on pin 2
