from pathlib import Path
ALLOWED_EXTENSIONS=[
    ".pdf",
    ".docx",
    ".txt"
]
def validate_file(filename:str):
    extension=Path(filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type:{extension}")
    return extension