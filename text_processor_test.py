from pdf_loader import load_pdf
from text_processor import split_documents


try:
    pages = load_pdf("uploads/Assignment 3 spm.pdf")
    chunks = split_documents(pages)

    print(f"Total pages: {len(pages)}")
    print(f"Total chunks: {len(chunks)}")

    print("\nFirst chunk:")
    print(chunks[0].page_content)

    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

except Exception as error:
    print(f"Error: {error}")