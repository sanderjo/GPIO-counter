GPIO-counter
============

Counts pulses on specified GPIO pin and writes to a logfile. I use this to count the pulses from my electric power meter (DDS-238), where each pulse is 1 Wh (as 1000 pulses per kWh).

Prerequisites
-------------
- Raspberry Pi (tested on Raspbian)
- GPIO python library installed: "sudo apt-get install RPi.GPIO"
Advice:
- make gpio-counter.py executable with "chmod +x gpio-counter.py"


Usage
-----
<pre><code>
$ sudo ./gpio-counter.py 23 /home/pi/mylogfile-gpio23.txt debug
Verbose is On
GPIO is 23
Logfile is /home/pi/mylogfile-gpio23.txt
Current value is 320
New value is 321
New value is 322
New value is 323
New value is 324
New value is 325
New value is 326
New value is 327
New value is 328
New value is 329
New value is 330
</code></pre>

Contents of the resulting logfile
---------------------------------

<pre><code>
$ cat gpio-counter 
228
2014-10-18 11:03:34.814608
</code></pre>

You can feed this info into MRTG

Start at boot / Run a daemon
----------------------------

To start the counter automatically start at boot time, do this:

<pre><code>
sudo crontab -e
</code></pre>
and fill out:
<pre><code>
@reboot         /path/to/gpio-counter.py 23 /home/pi/mylogfile-gpio23.txt &
</code></pre>
