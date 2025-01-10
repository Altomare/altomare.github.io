---
weight: 330
title: "Software"
description: "Otrona disk dumps"
icon: "save"
date: "2024-04-22T13:09:11+02:00"
lastmod: "2024-04-22T13:09:11+02:00"
---

## Disk dumps

This page contains unorganized notes about all the disk images I came across and their contents.

Source    | Name                                     | OS         | Notes
--------- | ---------------------------------------- | ---------- | ------
Alto      | FS_OTRONA_MASTER_V3_Mailmerge__Spellstar | CP/M 2.2.3 |
Alto      | attache_software_cpm_225H                | CP/M 2.2.5 |
Alto      | cpm_system_master                        | CP/M 2.2.5 |
Alto      | system_master_cpm                        | CP/M 2.2.5 |
Alto      | wordstar_cpm                             | CP/M 2.2.5 |
Bitsavers | Attache_Boot_2.2.5                       | CP/M 2.2.5 |
Maslin    | oattache                                 | CP/M 2.2.5 |
Alto      | attache_msdos                            | MS-DOS     |
Alto      | msdos_multiplan                          | MS-DOS     |
Alto      | multiplan_msdos                          | MS-DOS     |
Alto      | otrona_msdos_system_master               | MS-DOS     |
Alto      | otrona_system_master                     | MS-DOS     |
Maslin    | oatt8086                                 | MS-DOS     |
Alto      | gwbasic                                  |            | Otrona 2001
Maslin    | otr-util                                 |            |
Maslin    | otr-srce                                 |            |

### Misc commands

```bash
cpmrm -f otr1 -T imd Attache_Boot_2.2.5.IMD 0:ATTACHE.BAS
cpmcp -f otr1 -T imd Attache_Boot_2.2.5.IMD ATTACHE.BAS 0:ATTACHE.BAS
hxcfe -finput:Attache_Boot_2.2.5.IMD -foutput:test.otrona.img -conv:RAW_LOADER
```
