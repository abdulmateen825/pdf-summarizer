from pdf_loader import load_pdf


try:
    pages = load_pdf("uploads/Assignment 3 spm.pdf")

    print(f"Total pages: {len(pages)}")

    print("\nFirst page text:")
    print(pages[0].page_content)

    print("\nFirst page metadata:")
    print(pages[0].metadata)

except Exception as error:
    print(f"Error: {error}")