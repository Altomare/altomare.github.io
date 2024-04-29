---
weight: 999
title: "Otrona_software"
description: ""
icon: "article"
date: "2024-04-22T13:09:11+02:00"
lastmod: "2024-04-22T13:09:11+02:00"
toc: true
---

## System ROMs

### Monitor

The Otrona boot ROM (U252) contains the following features:
* Read first floppy sector into 0xFE00 and attempt to boot on it
* Terminal mode
* System diagnostics

It is usually on a 2732 EPROM, but the socket also accepts 2764s.

| Version | Motherboard | MD5                                |
| ------- | ----------- | ---------------------------------- |
| D       | Rev C       | `2db2b51c07f2412b51531a3d4c3c21b1` |
| F       |             | `f9975873e30494aae32c8cb5385156a4` |
| G       |             | `fdb4e89990238beabdd423f8868203b9` |
| H       | Rev E       | `29b42cb020ce64b4a7e7accb5bf182db` |


### Character

The character ROM (U416) is the same on all the Otronas I've seen so far. From early Attachés to late 8:16s.
It is usually labeled "CG 500".

MD5: `346258b1cc3e3e88fa7e7e0b6a1984e7`

![Otrona Character ROM]({{ site.url }}/assets/images/otrona/otrona_character_rom.png)

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
{{< table "table-striped table-sm table-borderless" >}}
| Boot message                    | Source                 | Board        | Drive  | Notes               |
| --------------------------------| ---------------------- | ------------ | ------ | ------------------- |
| CP/M 2.2.3 Otrona ATTACHE <56K> | Own dump               | Rev C, ROM D | 48 TPI |                     |         |
| CP/M 2.2.5/48 Otrona 8:16 <56K> | Bitsavers & Don Maslin | ???          |        |                     |
| CP/M 2.2.5 Otrona ATTACHE <56K> | Sources                | ???          | 96 TPI | No CCP & BDOS       |
| CP/M 2.2.5 Otrona ATTACHE <56K> | Own dump               | Rev E, ROM H | 48 TPI |                     |
{{< /table >}}

## Software

Unsorted collection of dumps, likely contains duplicates.

### Disk Images

{{< table "table-striped table-sm table-bordered table-responsive" >}}

| File                                         | Source     | Description                      |
| -------------------------------------------- | ---------- | -------------------------------- |
| oatt8086.td0                                 | Don Maslin | Otrona Attache' w/ 8086 add-in board - MSDOS v2.1 |
| oattache.td0                                 | Don Maslin | Otrona Attache' system disk      |
| otr-srce.td0                                 | Don Maslin | Attache' ASM/BAS/MAC source code |
| otr-util.td0                                 | Don Maslin | Attache' Utilities               |
| Attache_Boot_2.2.5.IMD                       | Bitsavers  |                                  |
| attache_msdos.hfe                            | Altomare   |                                  |
| attache_software_cpm_225H.hfe                | Altomare   |                                  |
| cpm_system_master.hfe                        | Altomare   |                                  |
| FS_OTRONA_MASTER_V3_Mailmerge__Spellstar.hfe | Altomare   |                                  |
| gwbasic.hfe                                  | Altomare   |                                  |
| msdos_multiplan.hfe                          | Altomare   |                                  |
| multiplan_msdos.hfe                          | Altomare   |                                  |
| otrona_msdos_system_master.hfe               | Altomare   |                                  |
| otrona_system_master.hfe                     | Altomare   |                                  |
| system_master_cpm.hfe                        | Altomare   |                                  |
| wordstar_cpm.hfe                             | Altomare   |                                  |

{{< /table >}}


### Misc.

| File                      | Source       | Description                      |
| --------------------------| ------------ | -------------------------------- |
| bios225.asm               | Bitsavers    |                                  |
| bios225.zip               | Don Maslin   |                                  |
| mbasic.com                | Don Maslin   |                                  |
| ns-copy1                  | Don Maslin   |                                  |
| otr-asm.zip               | Don Maslin   |                                  |
| otr-bas.zip               | Don Maslin   |                                  |
| otr-dos.zip               | Don Maslin   |                                  |
| otr-mex.zip               | Don Maslin   | MEX communications               |
| otr-mp.zip                | Don Maslin   | MultiPlan for the Attache'       |
| otr-utl.zip               | Don Maslin   |                                  |
| otr-ws.zip                | Don Maslin   | Wordstar 3.0 for the Attache'    |
| otrnasrc.zip              | Don Maslin   |                                  |
| disk01-CPM-BOOT.tar       | Tom Jennings |                                  |
| disk02-MULTIPLAN-BOOT.tar | Tom Jennings |                                  |
| disk03-OTRONA-BOOT.tar    | Tom Jennings |                                  |
| disk04-CPM-WS-TELINK.tar  | Tom Jennings |                                  |
| disk05-CPM-WS-TELINK.tar  | Tom Jennings |                                  |
| disk06-ADVENTURE.tar      | Tom Jennings |                                  |
| disk07-DBASE-ZIP.tar      | Tom Jennings |                                  |
| disk08-ADVENTURE-MISC.tar | Tom Jennings |                                  |
| disk09-WS-BOOT.tar        | Tom Jennings |                                  |
| disk10-MBASIC.tar         | Tom Jennings |                                  |
| disk11-UNKNOWN-APP.tar    | Tom Jennings |                                  |
| disk12-CPM-ALL-WS.tar     | Tom Jennings |                                  |
| disk13-ADVENTURE.tar      | Tom Jennings |                                  |
| disk14-BASIC.tar          | Tom Jennings |                                  |
| disk15-UNKNOWN-APP2.tar   | Tom Jennings |                                  |
| disk16-UNKNOWN-APP3.tar   | Tom Jennings |                                  |


&nbsp;

About Tom Jennings' dumps:

> While working for Phoenix Software Associates I ported MSDOS to
> the Z80-based Otrona Attache 8:16 (Mike Aronson fit an 8086
> into the printer option slot!).
> Here's a copy of the floppies I had for mine.
>
> ------------------------------------------------------------------
>
> These are copies of the diskettes that remained with
> my original Otrona Attache. THe computer was sold on eBay, and the
> buyer copied all the diskette contents to CD-ROM for me. THe dates
> were lost (since CP/M did not keep them), but a few directories
> contain files with dated names. Also some of the ADVENTURE files
> are from 1980 (Eric's friend Keith, etc), which is odd since in
> 1980 in our rented house we had a PDOS machine (rack mount, what
> waws the brand?) with 8" floppies. Must have been backed up
> (likely).
> 
> .CPM == .COM CP/M-80 binary executables.
> 
> The BASIC files are mainly Otrona Attache, with many
> non-standard graphics extentions. The MBASIC stuff is likely plain
> old MBASIC.
> 
> Adventure is a Z80, TDL/Xitan FORTRAN-compiled version
> of the "original" 350 point version. A map exists in my papers
> somewhere.

