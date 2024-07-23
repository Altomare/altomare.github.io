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

Disk Parameter Block:
```
SPT = 40   ; 10 * 512 byte sectors per track 
BSH =  4
BLM = 15   ; BLS = 2048 bytes per block
EXM = 1    ; An extent contains 32k
DSM = 181  ; 182 * 2k = 360k capacity (excluding superblock)
DRM = 127  ; 128 directory entries
AL0 = 0xC0 ; 2 blocks used for superblock
AL1 = 0
CKS = 32
OFF = 3    ; 3 reserved system tracks
```
DIRENT  = 128

DIRALC  = 2

cpmtools diskdefs:
```
# Otrona Attaché, DSDD, 48 TPI, 5.25"
# First 3 tracks of side 0 contain the OS
# Last 4 tracks of side 1 are unused
diskdef otrona
  seclen 512
  tracks 80
  sectrk 10
  blocksize 2048
  maxdir 128
  skew 1
  boottrk 0
  offset 30720
  os 2.2
end
```

Note: when testing, I had issues with the boottrk parameter, hence the offset.

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
