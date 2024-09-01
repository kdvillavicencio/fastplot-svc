from fastapi import APIRouter, UploadFile;
from img2table.document import Image
from img2table.ocr import TesseractOCR

router = APIRouter(
    prefix="/data"
)

tesseract_ocr = TesseractOCR(n_threads=1, lang="eng")

@router.get("/")
async def ping_data():
    return { "message":"Hello from data!" }

@router.post("/extract_from_image")
async def get_table_data(image_file: UploadFile):
    """
    Returns extracted data

    """
    print(image_file)
    data = {}

    # with open(image_file, 'rb') as  f:
    # img_bytes = await image_file.read()
    img_bytes = image_file.file.read()

    img = Image(src=img_bytes)
    extracted_tables = img.extract_tables(ocr=tesseract_ocr,
                                      implicit_rows=True,
                                      borderless_tables=True,
                                      min_confidence=50)

    for idx, table in enumerate(extracted_tables):
        result = table.df.to_numpy()
        print(result)
        data[idx] = result.tolist()
    
    return { "data":data }