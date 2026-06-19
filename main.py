from pathlib import Path
import shutil
from typing import Annotated

from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()

UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)


@app.post("/upload-pdf")
async def upload_pdf(
    file: Annotated[UploadFile, File(description="Select a PDF file")]
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file was selected.")

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    safe_filename = Path(file.filename).name
    file_path = UPLOAD_DIRECTORY / safe_filename

    try:
        with file_path.open("wb") as output_file:
            shutil.copyfileobj(file.file, output_file)
    except Exception:
        raise HTTPException(status_code=500, detail="Could not save the PDF.")
    finally:
        await file.close()

    return {
        "message": "PDF uploaded successfully",
        "filename": safe_filename,
        "saved_path": str(file_path),
    }