# Message to QR Code to SSTV Encoder
This Python script allows you to convert text data into a QR code, then encode the QR code into an SSTV (Slow Scan Television) signal using the Robot36 format. The SSTV signal is saved as a .wav file, which can be transmitted and decoded back into the original QR code.

# Features
- Generate QR Codes: Convert any text input into a QR code image.
- SSTV Encoding: Encode the generated QR code into an SSTV signal using the Robot36 format.
- Save as WAV: The SSTV signal is saved as a .wav file for easy transmission or storage.

# Requirements
- Python 3.x
- qrcode library
- pysstv library
- PIL (Python Imaging Library)

You can install the required libraries using pip:
```
pip install qrcode pysstv pillow
```
