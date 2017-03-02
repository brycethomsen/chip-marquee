# CHIP Marquee

## Features:
- Display custom messages via HTTP interface
- Change between local wifi and internet connected wifi by pressing the button
- Send messages via POST?



## Usage:
```
sudo -E bash -c ' /home/chip/chip_marquee/venv/bin/python -m flask run --host=0.0.0.0'
```

#### Equipment:
- Alpha PPD220GRN LED marquee
- RS-232 to TTL converter
- Next Thing C.H.I.P

#### Resources:
- http://docs.getchip.com/chip.html#pin-headers
- http://docs.getchip.com/chip.html#uart
- https://alphasign.readthedocs.io/en/latest/index.html
- somday:https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/install-software
