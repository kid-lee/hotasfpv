   #!/usr/bin/env python
import time
import PPM
import pigpio

pi = pigpio.pi()

if not pi.connected:
   exit(0)

pi.wave_tx_stop() # Start with a clean slate.

#ppm = PPM.X(pi, 3, frame_ms=20)
ppm = PPM.X(pi, 4, frame_ms=22.5)
#ppm = PPM.X(pi, 4)
updates = 0
start = time.time()
for chan in range(8):
   for pw in range(1000, 2000, 5):
         ppm.update_channel(chan, pw)
         updates += 1
end = time.time()
secs = end - start
print("{} updates in {:.1f} seconds ({}/s)".format(updates, secs, int(updates/secs)))
   
ppm.update_channels([1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000])

time.sleep(2)
ppm.cancel()
pi.stop()