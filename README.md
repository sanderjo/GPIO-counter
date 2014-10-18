GPIO-counter
============

Counts pulses on specified GPIO pin and writes to a logfile. I use this to count the pulses from my electric power meter (DDS-238), where each pulse is 1 Wh (as 1000 pulses per kWh).


<pre><code>
$ sudo python gpio23-counter.py debug
Verbose is On
Logfile is ./gpio-counter
Current value is 0
New value is 221
New value is 222
New value is 223
New value is 224
New value is 225
New value is 226
New value is 227
New value is 228
</code></pre>

Contents of the resulting logfile

<pre><code>
$ cat gpio-counter 
228
2014-10-18 11:03:34.814608
</code></pre>

You can feed this info into MRTG

To start the counter automatically start at boot time, do this:

<pre><code>
sudo crontab -e
</code></pre>
and fill out:
<pre><code>
@reboot         /path/to/gpio23-counter.py &
</code></pre>
