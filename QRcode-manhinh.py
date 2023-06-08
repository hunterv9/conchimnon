import csv
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Đường dẫn đến file csv
csv_path = 'B:/noname/Manufacturing Engineering/Datafile/manhinh1.csv'

# Đường dẫn đến file logo
logo_path = "B:/noname/date/logo.png"

# Đường dẫn đến font chữ
font_path = "B:/noname/date/1234.ttf"

# Màu sắc chữ và font size
text_color = (255, 0, 0)  # Đen
font_size = 41

# Đọc file csv 
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Tạo file csv mới để lưu mã QR code, tên và tên máy
    with open('B:/noname/Manufacturing Engineering/manhinh/pccname1.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)

        for row in csv_reader:
            barcode = row[0]
            name = row[1]
            model = row[2]

            # Tạo mã QR code với cấp độ sửa lỗi cao
            qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
            qr.add_data(barcode)
            qr.make(fit=True)

            # Tạo ảnh mã QR code với kích thước lớn
            qr_img = qr.make_image(fill_color="black", back_color="white", fit=True)

            # Đọc ảnh logo và tính toán kích thước
            logo_img = Image.open(logo_path)
            logo_size = int(qr_img.size[0] * 0.2), int(qr_img.size[1] * 0.2)
            logo_img = logo_img.resize(logo_size)

            # Tạo ảnh mới và dán mã QR code và logo
            new_img = Image.new('RGB', qr_img.size, color='white')
            new_img.paste(qr_img, (0, 0))

          

            # Vẽ chữ lên ảnh
            draw = ImageDraw.Draw(new_img)
            font = ImageFont.truetype(font_path, font_size)
            text_width, text_height = draw.textsize(model, font)
            text_position = ((qr_img.size[0] - text_width) // 2, (qr_img.size[1] - text_height) // 2 + text_height + 166)
            draw.text(text_position, model, font=font, fill=text_color)

            # Lưu ảnh mã QR code
            # Lưu ảnh mã QR code
            img_path = "B:/noname/Manufacturing Engineering/manhinh/"
            img_format = ".jpg"
            img_name = barcode + img_format
            img_full_path = img_path + img_name
            new_img.save(img_full_path, format='JPEG')
            # Ghi thông tin vào file csv
            csv_writer.writerow([f"{barcode}.png", name, model])

print("Done!")