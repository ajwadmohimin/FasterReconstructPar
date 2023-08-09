import subprocess
import numpy as np


nProcs = 16
TimeStep_start = 1.6
TimeStep_stop = 2.41
deltaT = 0.01
tPrcs = 5 # timesteps per processor

precision = 6
t=np.arange(TimeStep_start, TimeStep_stop, deltaT).round(precision) # rounding is required.
# print("Timesteps are:", t) # to check the timesteps if they are okay or not.

print(f"Starting {nProcs} reconstructPar processes. ")

for i in np.arange(nProcs):
    subprocess.run(f"reconstructPar -time {t[i*tPrcs]}:{t[i*tPrcs+tPrcs]} &", shell=True)
    # print(f"reconstructPar -time {t[i*tPrcs]}:{t[i*tPrcs+tPrcs]} &") # to check whether it has the timesteps and
                                                                     # commands properly
