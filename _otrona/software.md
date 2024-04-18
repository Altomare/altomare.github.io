---
title: Otrona Software
layout: post
---

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

<div class="table-wrapper" markdown="block">

| Boot message                    | Source                 | Board        | Drive  | Notes               |
| --------------------------------| ---------------------- | ------------ | ------ | ------------------- |
| CP/M 2.2.3 Otrona ATTACHE <56K> | Own dump               | Rev C, ROM D | 48 TPI |                     |         |
| CP/M 2.2.5/48 Otrona 8:16 <56K> | Bitsavers & Don Maslin | ???          |        |                     |
| CP/M 2.2.5 Otrona ATTACHE <56K> | Sources                | ???          | 96 TPI | No CCP & BDOS       |
| CP/M 2.2.5 Otrona ATTACHE <56K> | Own dump               | Rev E, ROM H | 48 TPI |                     |

</div>
