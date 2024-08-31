from img2table.document import Image
from io import BytesIO

### Read Image

img_path = "sample_img/tbl0.png"
img_from_path = Image(src=img_path)

with open(img_path, 'rb') as  f:
  img_bytes = f.read()

img_from_bytes = Image(src=img_bytes)
img_from_file_like = Image(src=BytesIO(img_bytes))

### OCR

from img2table.ocr import TesseractOCR

tesseract_ocr = TesseractOCR(n_threads=1, lang="eng")

### Extraction
img = Image(src=img_path)
extracted_tables = img.extract_tables(ocr=tesseract_ocr,
                                      implicit_rows=True,
                                      borderless_tables=True,
                                      min_confidence=50)

print(extracted_tables)

for idx, table in enumerate(extracted_tables):
  print(table.df.to_numpy())
# table_img = cv2.imread(img_path)

# for table in extracted_tables:
#   for row in table.content.values():
#     for cell in row:
#       cv2.rectangle(table_img, (cell))