import os
import argparse
import fitz
from PIL import Image
from datetime import datetime

# usually journals require tiff figures w 400dpi (default)

def pdf2tiff(folder_path, dpi=400):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_folder = os.path.join(folder_path, f"converted_tiffs_{timestamp}")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            output_base_name = os.path.splitext(file_name)[0]

            try:
                doc = fitz.open(pdf_path)
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    pix = page.get_pixmap(dpi=dpi)
                    temp_png_path = os.path.join(output_folder, f"{output_base_name}_{page_num + 1}.png")
                    pix.save(temp_png_path)

                    with Image.open(temp_png_path) as img:
                        tiff_path = os.path.join(output_folder, f"{output_base_name}_{page_num + 1}.tiff")
                        img.save(tiff_path, 'TIFF', dpi=(dpi, dpi)) 
                    
                    os.remove(temp_png_path)
                doc.close()
            except Exception as e:
                print(f"error converting {file_name}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert pdf to tiff')
    parser.add_argument('--folder_path', required=True, help='path to folder with pdf files')
    parser.add_argument('--dpi', type=int, default=400, help='define dpi (default=400)')
    args = parser.parse_args()

    pdf2tiff(args.folder_path, args.dpi)
