---
title: Floppy Drives
layout: post
---

This is a collection of data about the floppy drives I own and use for dumping.

5.25:

<div class="table-wrapper" markdown="block">

| Brand                      | Model          | RPM | TPI | Sides | Max track | Height | Pin 2     | Pin 4  | Pin 34 |
| -------------------------- | -------------- | --- | --- | ----- |---------- | ------ | --------- | ------ | ------ |
| Shugart                    | SA-450         | 300 | 48  | 2     |  40       | 86mm   |   -       | In Use |   -    |
| Magnetic Peripherals (CDC) | BR8B1A (9049)  | 300 | 48  | 2     |  40       | 86mm   |   -       | In Use |   -    |
| Alps                       | FDD2124AM2     | 300 | 48  | 1     |  40       | 43mm   |   ?       |   ?    |   ?    |
| Micropolis                 | 1015 II S      | 300 | 100 | 1     |  80       | 86mm   | Head Load | Ready  |  DS4   |
| TEAC                       | FD-55BV-54-U   | 300 | 48  | 2     |  40       | 43mm   |   -       | In Use | Ready  |
| Remex                      | RFD480         | 300 | 48  | 2     |  40       | 57mm   |   -       |   -    | Ready  |
| YE Data                    | YD-380B (1736) | 360 | 96  | 2     |  82       | 43mm   |   ?       | In Use | Ready  |

</div>

3.5:
* Mitsumi D359M3D: 1M / 2M mode. Max track 82

Useful data:
* <https://retrocmp.de/fdd/general/floppy-bus.htm>

### Shugart SA-450

Jumpers:
* 1/2/3/4: drive select
* MX: Single drive configuration, disable drive select logic. See manual section 4.1.1.2
* MS: Spin motor on drive select
* MM: Only spin motor when MOTOR ON signal is high

Empty socket for a 150 Ohm terminator

**Note: very slow seek (20ms). When using a greaseweazle, adjust delays with `gw delays --step 25000`.**

Manual: [bitsavers.org]<http://bitsavers.org/pdf/shugart/SA450/39013-1_SA450_OEM_Manual_Oct80.pdf>

### CDC 9049

References:
* Intertec 4002045 (Part # 5002045)
* CDC 9409
* Magnetic Peripherals BR8B1A (Part # 77680001)

Jumpers description:
* H: Motor on & head load with select (HS)
* 1: Drive select 1
* 2: Drive select 2
* 3: Drive select 3
* X: Multiplex opt
* 4: Drive select 4
* M: Head load with 'motor on' signal only

Manual: [bitsavers.org](https://bitsavers.org/pdf/cdc/discs/floppy/77653379_Flexible_Disk_Drive_Model_9409_Product_Specification_Dec80.pdf)

### Alps FDD2124AM2

Single sided, used in the Olivetti ETV300 (CP/M based word processor).

I don't have much info and my drive needs maintenance.

### Micropolis 1015 MOD II

* Model #: 1015 II S
* P/N: 900040

My drive is an external one with a metal enclosure.

**Like the Shugart SA-450, it has very slow step time and requires delays adjustments when used with a greaseweazle.**
**Track-to-track access time = 30ms**

Manual: [bitsavers.org](http://www.bitsavers.org/pdf/micropolis/102001A_Micropolis_1015_1016_Maintenance_Manual_Dec79.pdf)

### Remex RFD480

These drives are used in the Otrona Attaché computers.

Jumpers:
Drive select: DS0 / DS1 / DS2 / DS3

RDY:
> On drives using Drive Control Card 114761-001, a OV static output can be provided on J1-6 as a Ready signal for those controllers that require this indication.
See manual section 2.3.3

Motor Control: select which signals control which motor

| A | B | C | D | Spindle      | Stepper      |
| - | - | - | - | ------------ | ------------ |
| x |   |   | x | Motor ON     | Drive Select |
| x |   | x |   | Motor ON     | Motor ON     |
|   | x | x |   | Drive Select | Drive Select |
| x |   |   |   | Motor ON     | Always       |
|   | x |   |   | Drive Select | Always       |

Otrona jumper setup: RDY, A, C

Manual: [bitsavers.org](http://bitsavers.org/pdf/remex/floppy/Remex_RFD480_RFD960_Product_Reference_Manual.pdf)

### TEAC FD-55BV-54-U

Jumpers:
- DS0, DS1, DS2, DS3: Drive select
- IU: enable In-Use signal on pin 4
- U1 / U2: front LED behavior
- RY / XT: Pin 34 behavior. Only set one, never both
  - RY: READY signal on pin 34
  - XT: keep pin 34 open
- FG: Frame grounding
- ML: motor spin condition
  - Open = only spin when motor On signal is received
  - Closed: spin when MOTOR ON or front LED is lit up
- RE: Automatically recalibrate on power on (takes 255ms at most)
- E0 / E2: INDEX/SECTOR and READ DATA pulses behavior
  - E0 open = only send INDEX/SECTOR when drive is ready
  - E0 closed: send INDEX/SECTOR independently of ready state
  - E2 open = only send READ DATA when drive is ready
  - E2 closed: send READ DATA independently of ready state
- HL: Unused, keep open

Front LED behavior:

| IU | U1 | U2 | Condition                        |
| -- | -- | -- | -------------------------------- |
|    |    |    | Drive select                     |
|  X |    |    | Drive select OR in use           |
|  X |  X |    | In use                           |
|    |  X |  X | Drive select & Ready             |
|  X |  X |  X | In use OR (drive select & ready) |

Manual: [bitsavers.org](http://bitsavers.org/pdf/teac/FD-55BV_Specification.pdf)

### Ye-Data YD-380B Model 1736

No documentation (yet) for this specific model. Information in the table above is extrapolated from the YD-380 manual

Pin 2 is wired to the drive controller, but it does not appear to control the speed.

The only soldered jumper headers are DS0 and DS1.

The PCB has 12 footprints for surface mount shunts, labeled JP1 to JP12.
Some are installed, but I assume these are for different hardware configurations...
