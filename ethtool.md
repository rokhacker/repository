***ethtool usage***


1. View to nego setting
```bash
# ethtool eth0
Settings for enp0s25:
        Supported ports: [ TP ]
        Supported link modes:   10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Supported pause frame use: No
        Supports auto-negotiation: Yes
        Supported FEC modes: Not reported
        Advertised link modes:  Not reported
        Advertised pause frame use: No
        Advertised auto-negotiation: No
        Advertised FEC modes: Not reported
        Speed: 100Mb/s
        Duplex: Half
        Port: Twisted Pair
        PHYAD: 1
        Transceiver: internal
        Auto-negotiation: off
        MDI-X: on (auto)
        Supports Wake-on: pumbg
        Wake-on: g
        Current message level: 0x00000007 (7)
                               drv probe link
        Link detected: yes
#
```

2. How to turn on for autoeng
```bash
# ethtool -s enp0s25 autoneg on
```


3. Have to turn off autoeng for manual setting of speed or duplex
```bash
# ethtool -s eth0 speed 100 duplex half autoneg off
```
