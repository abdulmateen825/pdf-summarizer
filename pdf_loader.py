from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The provided file is not a PDF.")

    loader = PyPDFLoader(str(path))
    pages = loader.load()

    if not pages:
        raise ValueError("No pages were found in the PDF.")

    extracted_text = "".join(page.page_content.strip() for page in pages)

    if not extracted_text:
        raise ValueError(
            "No readable text was found. The PDF may be scanned or image-based."
        )

    return pages