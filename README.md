# com-diag-hourglass

COPYRIGHT

Copyright 2017 by the Digital Aggregates Corporation, Arvada Colorado, USA.

LICENSE

Licensed under the terms of the FSF GPL v2.

ABSTRACT

Hourglass is my implementation of a stratum-1 NTP server based on a Raspberry
Pi 3 with a Uputronics GPS Board using the Ublox M8 chipset. Lots of people
have done this before, although perhaps not exactly the way I cobbled it
together. See the references below for pointers. I more or less followded
Eric Raymond's "Stratum-1-Microserver HOWTO" with a few changes here and
there to either customize it for my network or to fix a minor issue here
and there (e.g. his udev rule didn't work for me without modification).

Disclaimer: WORK IN PROGRESS!

REFERENCES

<https://www.ntpsec.org/white-papers/stratum-1-microserver-howto/>

<http://www.satsignal.eu/ntp/Raspberry-Pi-quickstart.html>

<http://ava.upuaut.net/?p=726>

<http://www.catb.org/gpsd/gpsd-time-service-howto.html>

<https://www.eecis.udel.edu/~mills/ntp/html/refclock.html>

<http://doc.ntp.org/4.1.0/ntpq.htm>

<http://www.linuxfromscratch.org/blfs/view/cvs/basicnet/ntp.html>

<https://git.savannah.gnu.org/git/gpsd.git>

<https://github.com/ntp-project/ntp>

<https://gitlab.com/NTPsec/ntpsec.git>

<https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi?view=all>

<http://www.elevendroids.com/2012/12/setting-up-hardware-rtc-in-raspbian/>

<https://blog.remibergsma.com/2013/05/08/adding-a-hardware-clock-rtc-to-the-raspberry-pi/>

<https://afterthoughtsoftware.com/products/rasclock>

<https://thepihut.com/blogs/raspberry-pi-tutorials/17209332-adding-a-real-time-clock-to-your-raspberry-pi>

<https://www.raspberrypi.org/forums/viewtopic.php?t=85683>

CONTACT

Chip Overclock  
<mailto:coverclock@diag.com>  
Digital Aggregates Corporation  
3440 Youngfield Street  
Suite 209  
Wheat Ridge CO 80033 USA  

NOTES

    sudo modprobe configs

    scons \
    	timeservice=yes \
        magic_hat=yes \
    	nmea0183=yes \
    	prefix="/usr" \
    	fixed_port_speed=9600 \
    	fixed_stop_bits=1 \
    	pps=yes \
    	ntpshm=yes

    ./configure \
        --prefix=/usr \
        --enable-all-clocks \
        --enable-parse-clocks \
        --enable-SHM \
        --disable-debugging \
        --sysconfdir=/var/lib/ntp \
        --with-sntp=no \
        --with-lineeditlibs=edit \
        --without-ntpsnmpd \
        --disable-local-libopts \
        --enable-ntp-signd \
        --disable-dependency-tracking \
        --enable-ATOM \
        --enable-linuxcaps

    sudo /usr/sbin/gpsd -b -n -N -D 5 /dev/gps0 /dev/pps0

    ntpq -c peer -c as -c rl

    ntpq -p hourglass

    sudo ntpd -gdn

    sudo date -u $(ssh jsloan@mercury bin/dateu)

    sudo raspi-config

    sudo apt-get install i2c-tools

EXAMPLE

    jsloan@mercury:~$ !ntpq
    ntpq -c peer -c as -c rl hourglass
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    *SHM(1)          .PPS.            0 l    3   64  377    0.000  -76.235   5.814
    xSHM(0)          .GPS.            0 l    2   64  377    0.000  -206.32   9.439
    +ha82.smatwebdes 200.98.196.212   2 u   61   64  377   33.869  -78.555 100.580
    +clockb.ntpjs.or 97.164.73.162    3 u    5   64  377   51.931  -78.499   5.904
    -leeloo.scurvyne 128.4.1.1        4 u   49   64  373   64.860  -72.514   5.731
    +mirror          216.93.242.12    3 u   53   64  377   44.566  -80.662   8.004
    -unlawful.id.au  131.188.3.220    2 u   19   64  377   61.163  -68.225  30.522
    +chl.la          216.218.254.202  2 u  125   64   32   46.733  -77.483  54.361
    +195.21.152.161  193.62.22.74     2 u   43   64  377   62.572  -79.654   6.920
    
    ind assid status  conf reach auth condition  last_event cnt
    ===========================================================
      1 36480  961a   yes   yes  none  sys.peer    sys_peer  1
      2 36481  911a   yes   yes  none falsetick    sys_peer  1
      3 36482  8811   yes  none  none    reject    mobilize  1
      4 36483  141a    no   yes  none candidate    sys_peer  1
      5 36484  1414    no   yes  none candidate   reachable  1
      6 36485  1314    no   yes  none   outlyer   reachable  1
      7 36486  1424    no   yes  none candidate   reachable  2
      8 36487  1324    no   yes  none   outlyer   reachable  2
      9 36488  1414    no   yes  none candidate   reachable  1
     10 36489  1424    no   yes  none candidate   reachable  2
    associd=0 status=0415 leap_none, sync_uhf_radio, 1 event, clock_sync,
    version="ntpd ntpsec-0.9.6+4149 2017-03-15T10:30:25-0400",
    processor="armv7l", system="Linux/4.4.50-v7+", leap=00, stratum=1,
    precision=-20, rootdelay=0.000, rootdisp=80.878, refid=PPS,
    reftime=dc73e663.dea6cac5  Wed, Mar 15 2017 10:12:19.869,
    clock=dc73e666.9f2621b9  Wed, Mar 15 2017 10:12:22.621, peer=36480, tc=6,
    mintc=0, offset=-76.723, frequency=230.470, sys_jitter=3.189739,
    clk_jitter=3.096846, clk_wander=5.393056
