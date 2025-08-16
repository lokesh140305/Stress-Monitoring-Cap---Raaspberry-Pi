import requests
from pulsesensor import Pulsesensor
import time
from mcp3008 import mcp3008
adc = mcp3008()
p = Pulsesensor()
p.startAsyncBPM()

while True:
    bpm = p.BPM
    print("BPM: %d" % bpm)
    EEG= adc.read(5)
    print("EEG: %d" % EEG)
    GSR= adc.read(6)
    print("GSR: %d" % GSR)
    ECG= adc.read(7)
    print("ecg: %d" % ECG)
    r=requests.get("https://blr1.blynk.cloud/external/api/update?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v0="+str(bpm))
    s=requests.get("https://blr1.blynk.cloud/external/api/update?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v1="+str(EEG))
    t=requests.get("https://blr1.blynk.cloud/external/api/update?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v2="+str(GSR))
    q=requests.get("https://blr1.blynk.cloud/external/api/update?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v3="+str(ECG))
    if((r.status_code == 200 and s.status_code == 200) and (t.status_code == 200 and q.status_code ==200)):
        print("value updated successfully")
    time.sleep(.5)
    
    