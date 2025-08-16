import requests

while(True):
    a=requests.get("https://blr1.blynk.cloud/external/api/get?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v0=")
    print("BPM = ",a.text)
    b=requests.get("https://blr1.blynk.cloud/external/api/get?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v1=")
    print("EEg = ",b.text)
    c=requests.get("https://blr1.blynk.cloud/external/api/get?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v2=")
    print("GSR = ",c.text)
    d=requests.get("https://blr1.blynk.cloud/external/api/get?token=m8h5qpc75E6CtgeFv6BCYpof-3y_fg29&v3=")
    print("GSR = ",d.text)
    