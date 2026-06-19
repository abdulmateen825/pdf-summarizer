from llm import summarize_text



sample_text = """
FastAPI is a modern Python framework used for creating APIs.
It supports automatic API documentation, type validation,
asynchronous request handling, and dependency injection.
"""

try:
    summary = summarize_text(sample_text)
    print(summary)

except Exception as error:
    print(f"Error: {error}")