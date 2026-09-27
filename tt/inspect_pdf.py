import fitz

pdf_path = "data/ML2.pdf"

doc = fitz.open(pdf_path)

print("Number of pages:", len(doc))

for page_number, page in enumerate(doc):
    text = page.get_text()

    print(f"\n--- Page {page_number + 1} ---")
    print("Characters extracted:", len(text))
    print(text[:500])