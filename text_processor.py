from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(pages):
    if not pages:
        raise ValueError("No PDF pages were provided.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300,
    )

    chunks = text_splitter.split_documents(pages)

    if not chunks:
        raise ValueError("Could not create text chunks.")

    return chunks
    