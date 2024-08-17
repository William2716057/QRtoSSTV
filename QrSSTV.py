import qrcode
from pysstv.color import Robot36
from PIL import Image

def encode_to_qr_code(data, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

if __name__ == "__main__":
    text = input("Enter QR code input: ")
    filename = input("Enter resulting QR image filename: ")
    output_path = filename
    encode_to_qr_code(text, output_path)
    print(f"Saved as {output_path}")
    
    # Open QR image saved is output_path
    img = Image.open(output_path)
    
    # Resize image to 320x240 pixels to match Robot36 requirements
    img = img.resize((320, 240))
    
    # Convert image to an SSTV signal
    sstv = Robot36(img, 44100, 16)
    
    # Save SSTV signal as a WAV file
    with open('output.wav', 'wb') as f:
        sstv.write_wav(f)
    
    print("Wave file created successfully")