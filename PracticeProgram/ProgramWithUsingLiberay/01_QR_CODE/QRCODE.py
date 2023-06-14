import qrcode
def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#6aff92", background_color="#fff")
    img.save(file_name)


text = input("Enter Website URL: ")
file_name = "PracticeProgram\ProgramWithUsingLiberay\QR_CODE\qr_code3.png"
generate_qr_code(text, file_name)
print(f"Qr Code saved as {file_name}")
