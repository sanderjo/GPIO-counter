GPIO-counter
============

Counts pulses on specified GPIO pin and writes to a logfile. I use this to count the pulses from my electric power meter (DDS238), where each pulse is 1 Wh (as 1000 pulses per kWh).

Prerequisites
-------------
- Raspberry Pi (tested on Raspbian)
- GPIO python library installed: "sudo apt-get install RPi.GPIO"

Install
-------
<pre><code>
cd
mkdir git
cd git
git clone https://github.com/sanderjo/GPIO-counter.git
cd GPIO-counter
chmod +x gpio-counter.py
</code></pre>

The GPIO-counter is now installed.

Usage
-----

To use gpio-counter from the commandline, do this:

<pre><code>
$ sudo /home/pi/git/gpio-counter.py 23 /var/log/gpio23-counter.log debug
Verbose is On
GPIO is 23
Logfile is /var/log/gpio23-counter
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
$ cat /var/log/gpio23-counter.log
764
2014-10-18 12:22:27.207244
</code></pre>

You can feed this info into MRTG

Start at boot / Run as daemon
----------------------------

To start the counter automatically start at boot time, do this:

<pre><code>
sudo crontab -e
</code></pre>
and fill out:
<pre><code>
@reboot			/home/pi/git/GPIO-counter/gpio-counter.py 23 /var/log/gpio23-counter.log &
</code></pre>

Don't forget the ampersand at the end

Reboot your Raspberry, and check the daemon is running:

<pre><code>

$ ps -ef | grep -i gpio | grep python
root      2136     1  0 12:22 ?        00:00:00 python /home/pi/git/GPIO-counter/gpio-counter.py 23 /var/log/gpio23-counter.log
</code></pre>

You should only see one line. If you see two lines, check that you filled out the ampersand at the end of the crontab line.

You can continously monitor the output to the log file with 'tail -f':

<pre><code>
$ tail -f /var/log/gpio23-counter.log 2> /dev/null
879
2014-10-18 15:02:25.868110
880
2014-10-18 15:19:35.624902
881
2014-10-18 15:19:38.109248
883
2014-10-18 15:19:42.162002
884
2014-10-18 15:19:44.190460
886
</code></pre>



