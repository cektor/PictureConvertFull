# GNU License | Fatih ÖNDER - https://fatihonder.org.tr - https://github.com/cektor

from PIL import Image
import os

def convert_image_format(input_image, output_image, format):
    try:
        # Resmi aç ve formatını dönüştür
        image = Image.open(input_image)
        image.save(output_image, format=format)
        print(f"{input_image} formatı {format} olarak dönüştürüldü.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Dönüştürmek istediğiniz resimlerin bulunduğu klasörün adını burada belirtin
input_folder = "input_folder"

# Klasörü oluştur
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"{input_folder} klasörü oluşturuldu.")

# Dönüştürmek istediğiniz formatları burada belirtin (örneğin: "PNG", "JPEG", "GIF" vb.)
output_formats = ["PNG", "JPEG", "GIF"]

# Klasördeki tüm resimleri dönüştür
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        input_image_path = os.path.join(input_folder, filename)
        image_name, image_ext = os.path.splitext(filename)
        for output_format in output_formats:
            output_image_path = os.path.join(input_folder, f"{image_name}.{output_format.lower()}")
            convert_image_format(input_image_path, output_image_path, output_format)

