import csv
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Đường dẫn đến file CSV chứa danh sách các mã MAC và barcode
csv_path = 'B:/noname/Finance/Datafile/PClaptop.csv'

# Đường dẫn để lưu các ảnh QR code được tạo ra
output_path = 'B:/noname/Finance/'

# Font chữ và kích cỡ cho văn bản được vẽ lên QR code
font = ImageFont.truetype('arial.ttf', size=20)

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        mac_address = row[0]   # Lấy giá trị từ cột đầu tiên (index=0)
        name = row[1]          # Lấy giá trị từ cột thứ hai (index=1)
        text_to_draw = row[2]  # Lấy giá trị từ cột thứ ba (index=2)

        # Tạo mã QR code cho MAC address
        qr_mac = qrcode.make(mac_address)
        output_filename_mac = f"{name}.jpg"   # Sử dụng giá trị của biến name làm tên file QR code
        output_full_path_mac = output_path + output_filename_mac

        # Vẽ chữ lên QR code cho MAC address
        img_mac = Image.open(output_full_path_mac)
        draw_mac = ImageDraw.Draw(img_mac)
        draw_mac.text((10, 10), text_to_draw, font=font)   # Vẽ chữ lên hình ảnh QR code
        img_mac.save(output_full_path_mac)
