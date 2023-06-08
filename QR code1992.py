
import os
import csv
import qrcode
from PIL import Image, ImageDraw, ImageFont


# Đường dẫn đến file CSV chứa danh sách các mã MAC và barcode
csv_path = 'B:/noname/Manufacturing Engineering/Datafile/pclaptop1.csv'

# Đường dẫn để lưu các ảnh QR code được tạo ra
output_path = 'B:/noname/Manufacturing Engineering/pclaptop1/abc/'

# Đường dẫn đến font chữ
font_path = "B:/noname/date/1234.ttf"

# Màu sắc chữ và font size
text_color = int('000000', 0)  # màu đen
font_size = 30 

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Tạo file csv mới để lưu thông tin về các mã QR code và tên máy tính
    with open('B:/noname/Manufacturing Engineering/pclaptop1/pccname3.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)

        for row in csv_reader:
            value = row[0]   # Lấy giá trị từ cột đầu tiên (barcode hoặc MAC address)
            name = row[1]    # Lấy giá trị từ cột thứ hai (tên máy tính)
            text_to_draw = row[2]   # Lấy giá trị từ cột thứ ba (giá trị để vẽ lên hình ảnh QR code)

            # Tạo mã QR code cho barcode hoặc MAC address
            qr_code = qrcode.make(value, box_size=10)
            output_filename_qr_code = f"{name}.png"   # Sử dụng giá trị của biến name làm tên file QR code
            output_full_path_qr_code = output_path + output_filename_qr_code + ".png"

            # Lưu hình ảnh QR code vào file PNG
            qr_code.save(output_full_path_qr_code)

            # Vẽ chữ lên hình ảnh QR code cho barcode hoặc MAC address
            img_qr_code = Image.open(output_full_path_qr_code)
            draw_qr_code = ImageDraw.Draw(img_qr_code)
            font_qr_code = ImageFont.truetype(font_path, font_size)
            text_width, text_height = draw_qr_code.textsize(text_to_draw, font=font_qr_code)
            text_position_x = (img_qr_code.width - text_width) // 2   # Canh chỉnh văn bản theo chiều ngang của hình ảnh QR code.
            text_position_y = img_qr_code.height - text_height - 4  # Canh chỉnh văn bản để đẩy xuống dưới mã QR code.
            draw_qr_code.text((text_position_x, text_position_y), text_to_draw, fill=text_color, font=font_qr_code, antialias=True)
            img_qr_code.save(output_full_path_qr_code)

            # Ghi thông tin vào file CSV.
            csv_writer.writerow([f"{name}.png", name])

