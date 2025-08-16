# Stress-Monitoring-Cap---Raaspberry-Pi
A DIY wearable stress monitoring system built into a cap that tracks your physiological stress indicators in real-time. Perfect for students, gamers, or anyone curious about their stress levels!
# Stress Monitoring Cap

Hey everyone! 👋 I built this really cool stress monitoring system that uses a wearable cap to track your stress levels in real-time. The idea came to me when I noticed how stressed I was getting during exams and wanted a way to actually measure and monitor it objectively.

## What It Does

So basically, this system reads four different body signals that are known to change when you're stressed:
- *Heart Rate (BPM)* - Your pulse gets faster when stressed
- *EEG Signals* - Brain wave patterns that show mental state  
- *GSR (Skin Conductance)* - Your skin gets more conductive when you sweat from stress
- *ECG* - Heart rhythm patterns that can indicate stress

All this data gets sent to a Blynk app on your phone so you can see your stress levels in real-time! Pretty neat, right?

## What You'll Need

### The Main Stuff
- Raspberry Pi (I used a Pi 4, but any model with GPIO should work)
- MCP3008 chip (converts analog sensor signals to digital)
- Pulse sensor (the heart rate one)
- EEG electrodes (for brain signals - got mine from Amazon)
- GSR electrodes (these go on your fingers)
- ECG electrodes (chest placement for heart signals)
- A cap or headband to mount everything on
- Some jumper wires and a breadboard

### How I Wired It Up
I connected everything through the MCP3008 chip using SPI:
- Channel 0: Pulse sensor 
- Channel 5: EEG electrodes
- Channel 6: GSR finger sensors
- Channel 7: ECG chest electrodes

The wiring was probably the trickiest part, but there are tons of tutorials online for connecting MCP3008 to Raspberry Pi.

## Setting Everything Up

### Getting the Pi Ready
First things first, you need to enable SPI on your Raspberry Pi:
bash
# Open the config menu
sudo raspi-config
# Go to Interface Options > SPI > Enable

# Update everything (this takes a while, grab some coffee ☕)
sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip

# Don't forget to reboot!
sudo reboot


### Installing Python Stuff
bash
# This one's easy
pip3 install requests

# This one's a bit more involved - needed for talking to the MCP3008
wget https://github.com/doceme/py-spidev/archive/master.zip 
unzip master.zip
cd py-spidev-master
sudo python3 setup.py install


## Getting It Running

### Step 1: Download the Files
You'll need these Python files I wrote:
- main.py - This is the main program that reads all the sensors
- get_data.py - Use this to check what data is being uploaded
- MCP3008.py - Handles talking to the ADC chip
- pulsesensor.py - Does all the math to calculate your heart rate

### Step 2: Set Up Blynk (The Phone App Part)
This was actually pretty cool to figure out:
1. Download the Blynk app and create a new project
2. You'll get an auth token - replace mine in the code with yours
   (Mine is m8h5qpc75E6CtgeFv6BCYpof-3y_fg29 but obviously don't use that!)
3. Add some gauges to your app for:
   - V0: Heart Rate
   - V1: EEG Data  
   - V2: Stress Level (GSR)
   - V3: Heart Rhythm (ECG)

### Step 3: Put It All Together
Connect all your sensors to the cap/headband, wire everything up, and you're ready to go!

## Usage

### Data Collection
Run the main data collection script:
bash
python3 main.py


This script will:
- Initialize all sensors
- Start continuous BPM monitoring in background thread
- Read analog sensor values (EEG, GSR, ECG)
- Upload data to Blynk cloud every 0.5 seconds
- Display real-time sensor readings in console

### Data Monitoring
Run the data retrieval script to monitor uploaded data:
bash
python3 get_data.py


This script continuously fetches and displays the latest sensor values from Blynk cloud.

## File Descriptions

### main.py
Main application script that:
- Initializes MCP3008 ADC and pulse sensor
- Starts asynchronous BPM monitoring
- Reads analog sensor data in continuous loop
- Uploads sensor data to Blynk cloud via HTTP API
- Provides status feedback for successful uploads

### get_data.py
Data monitoring script that:
- Retrieves real-time sensor data from Blynk cloud
- Displays BPM, EEG, GSR, and ECG values
- Runs in continuous loop for real-time monitoring

### MCP3008.py
Hardware abstraction layer for MCP3008 ADC:
- Configures SPI communication
- Provides channel-based analog reading interface
- Supports 10-bit ADC resolution (0-1023)
- Configurable SPI bus and device selection

### pulsesensor.py
Advanced pulse detection and BPM calculation:
- Implements real-time signal processing algorithms
- Detects heartbeat peaks and troughs
- Calculates accurate BPM using Inter-Beat Interval (IBI)
- Filters noise and handles signal artifacts
- Runs in background thread for non-blocking operation

## Configuration

### Sensor Calibration
- *Pulse Sensor*: Adjust threshold values in pulsesensor.py for optimal detection
- *EEG/GSR/ECG*: Calibrate analog sensors based on your specific hardware
- *Sampling Rate*: Modify time.sleep(0.5) in main loop for different update frequencies

### Blynk Configuration
1. Create new Blynk project
2. Add gauge/display widgets for each sensor
3. Configure virtual pins (V0-V3)
4. Update auth token in both Python scripts

## Troubleshooting

### Common Issues
- *SPI Not Enabled*: Run sudo raspi-config and enable SPI interface
- *Permission Errors*: Run scripts with sudo if accessing GPIO
- *Connection Timeout*: Check internet connection and Blynk server status
- *Sensor Readings*: Verify hardware connections and sensor power supply

### Debug Tips
- Check console output for sensor readings and upload status
- Verify Blynk virtual pin configuration matches code
- Test individual sensors before running complete system
- Monitor network connectivity for cloud uploads

## Safety Considerations

⚠ *Important*: This system is designed for educational and research purposes only. It should not be used for medical diagnosis or treatment. Always consult qualified medical professionals for health-related concerns.

- Ensure proper electrical isolation when working with physiological sensors
- Use appropriate medical-grade sensors for human monitoring
- Follow all safety protocols when handling biomedical equipment
- Regularly calibrate and validate sensor readings

## Future Enhancements

- Data logging to local storage
- Advanced signal processing and filtering
- Web-based dashboard for data visualization
- Alert system for abnormal readings
- Integration with additional sensor types
- Machine learning for pattern recognition

## License

This project is open-source and available for educational and research purposes. Please ensure compliance with medical device regulations if used in clinical applications.
