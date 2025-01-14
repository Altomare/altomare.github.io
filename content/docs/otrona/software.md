---
weight: 330
title: "Software"
description: "Otrona system software"
icon: "save"
date: "2024-04-22T13:09:11+02:00"
lastmod: "2024-04-22T13:09:11+02:00"
---

## System ROMs

### Monitor

The Otrona boot ROM (U252) contains the following features:
* Read first floppy sector into 0xFE00 and attempt to boot on it
* Terminal mode
* System diagnostics

It is usually on a 2732 EPROM, but the socket also accepts 2764s.
These images should be compatible with every motherboard revision.

{{< table "table-striped table-bordered table-responsive" >}}
  
| Version | Notes                                                                         | Downloads                                              |
| ------- | ----------------------------------------------------------------------------- | ------------------------------------------------------ |
| Rev D   | Partial reverse-enginering available [here](https://github.com/fstark/anorto) | [ROM](/files/otrona/rom/Otrona_Attache_U252_Rev_D.BIN) |
| Rev E   | No dump available yet                                                         |                                                        |
| Rev F   | Reduce CRT overscan. Terminal mode improvements. Misc. changes \[1]           | [ROM](/files/otrona/rom/Otrona_Attache_U252_Rev_F.BIN) |
| Rev G   | Fixes CRT controller initialization issue, now conforms to RS-170 \[1]        | [ROM](/files/otrona/rom/Otrona_Attache_U252_Rev_G.BIN) |
| Rev H   | Adds 8:16 card diagnostics                                                    | [ROM](/files/otrona/rom/Otrona_Attache_U252_Rev_H.BIN) |
| Rev X   | Identical to H, except for one byte (revision display).                       | [ROM](/files/otrona/rom/Otrona_Attache_U252_Rev_X.BIN) / [Source (ZASM)](/files/otrona/source/MONX.ASM) / [Source (ZASM, cleaned)](files/otrona/source/MONX_CLEANED.ASM) |

{{< /table >}}

\[1]: See Technical Notes Manual for rev F & G changelogs

For Rev X, I recompiled from the source release using [ZASM](/files/cpm/compilers/tdl_assemblers.zip) on [RunCPM](https://github.com/MockbaTheBorg/RunCPM).

When reading sources, some characters may look corrupted. This is due to some CP/M editors adding page break markers by setting the most significant byte to 1.
The cleaned source file also linked is the same without trailing spaces, MSB page breaks and trailing EOFs.

### Character

The character ROM (U416) is the same on all the Otronas I've seen so far. From early Attachés to late 8:16s.
It is usually labeled "CG 500".

MD5: `346258b1cc3e3e88fa7e7e0b6a1984e7`

![Otrona Character ROM](/images/otrona/otrona_character_rom.png)

The above picture contains, in order:
* [Alternate-1] Forms ruling set
* [Standard] ASCII upper and lower case
* [Alternate-2] Greek lower case and math
* [Alternate-3] Greek upper case and math


## CP/M Operating System

The CP/M operating system is contained in the first 3 tracks (head 0) of a system diskette.
The first sector contains a bootloader, which will be loaded and executed by the system ROM.
This bootloader will then load all the remaining operating system from the floppy into memory.

From BIOS source:
> [Boot sector is] loaded into FE00h by PROM.
> Boot code will be saved in sector 1 of track 0 and is [...] one sector length ahead of the CCP.

Floppy layout:
```
0X0000 - 0x01FF (1 sector, 512)   = BIOS boot sector
0X0200 - 0x09FF (4 sectors, 2k)   = CCP
0X0A00 - 0x17FF (7 sectors, 3.5k) = BDOS
0x1800 - 0x3BFF (18 sectors, 9k)  = Rest of BIOS
```

Memory layout (64KB total):
```
0x0000 - 0x00FF = CP/M Buffers, registers & instructions
0x0100 - 0xC3FF = TPA: Transient Program Area
0xC400 - 0xCBFF = CCP: Console Command Processor
0xCC00 - 0xD9FF = BDOS: Basic Disk Operating System
0xDA00 - 0xFFFF = BIOS: Basic Input/Output System
```

### Versions

Below is a list of the OS versions I came across, along with the machine revision they came with:
{{< table "table-striped table-borderless table-responsive" >}}
| Boot message                    | Source                 | Board        | Drive  | Notes               |
| --------------------------------| ---------------------- | ------------ | ------ | ------------------- |
| CP/M 2.2.3 Otrona ATTACHE <56K> | Own dump               | Rev C, ROM D | 48 TPI |                     |
| CP/M 2.2.5/48 Otrona 8:16 <56K> | Bitsavers & Don Maslin | ???          |        |                     |
| CP/M 2.2.5 Otrona ATTACHE <56K> | Sources                | ???          | 96 TPI | No CCP & BDOS       |
| CP/M 2.2.5 Otrona ATTACHE <56K> | Own dump               | Rev E, ROM H | 48 TPI |                     |
{{< /table >}}
