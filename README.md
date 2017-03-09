# com-diag-hourglass

COPYRIGHT

Copyright 2017 by the Digital Aggregates Corporation, Arvada Colorado, USA.

LICENSE

Licensed under the terms of the FSF GPL v2.

ABSTRACT

Hourglass is my implementation of a stratum-1 NTP server based on a Raspberry
Pi 3 with a Uputronics GPS Board using the Ublox M8 chipset. Lots of people
have done this before, although perhaps not exactly the way I cobbled it
together. See the references below for pointers.

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

    systemctl disable hciuart
    systemctl stop hciuart
    systemctl disable gpsd.socket
    systemctl stop gpsd.socket
    systemctl enable gpsd.service
    systemctl start gpsd.service

    sudo /usr/sbin/gpsd -b -n -N -D 5 /dev/gps0 /dev/pps0

    ntpq -c peer -c as -c rl

    ntpq -p hourglass

    sudo ntpd -gdn
