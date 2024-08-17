# Message to QR Code to SSTV Encoder
This Python script allows you to convert text data into a QR code, then encode the QR code into an SSTV (Slow Scan Television) signal using the Robot36 format. The SSTV signal is saved as a .wav file, which can be transmitted and decoded back into the original QR code.

## Features
- Generate QR Codes: Convert any text input into a QR code image.
- SSTV Encoding: Encode the generated QR code into an SSTV signal using the Robot36 format.
- Save as WAV: The SSTV signal is saved as a .wav file for easy transmission or storage.

## Requirements
- Python 3.x
- qrcode library
- pysstv library
- PIL (Python Imaging Library)

You can install the required libraries using pip:
```
pip install qrcode pysstv pillow
```
## Usage

1. Clone this repository or download the script.
```
git clone https://github.com/William2716057/QRtoSSTV.git
```
2. Run the script:
```
python QrSSTV.py
```
3. Enter the text you want to encode into a QR code.
4. Provide a filename for the resulting QR image (e.g., qrcode.png)
5. The script will generate the QR code, resize it to match the requirements of the Robot36 SSTV format, and then encode it into an SSTV signal. The SSTV signal will be saved as output.wav.

## Decoding the SSTV Signal
To retrieve the original QR code from the SSTV signal, you can use any SSTV decoding software. 
Please note that the decoding process may not always be perfect on the first attempt, and you may need to decode the SSTV signal repeatedly to achieve an accurate result.

## Example Workflow
1. Input:

- Enter text: Hello, World!
- Filename for QR code: qrcode.png

2. Output:

- The QR code image will be saved as qrcode.png.
- The SSTV signal will be saved as output.wav.

3. Decoding:
- Use SSTV decoding software to convert output.wav back into the QR code.
- Use a QR code scanner to decode the original text.

# Notes
- The QR code image is resized to 320x240 pixels to match the Robot36 SSTV format requirements.
- For best results, ensure your SSTV decoding software is properly calibrated and try multiple decodes if the first attempt is not accurate.
