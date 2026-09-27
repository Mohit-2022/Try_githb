import fitz

pdf_path = "data/ML2.pdf"

doc = fitz.open(pdf_path)

print("=" * 80)
print("PAGES CONTAINING EMBEDDED IMAGE OBJECTS")
print("=" * 80)

for page_number, page in enumerate(doc):

    images = page.get_images(full=True)

    if images:
        print(
            f"Page {page_number + 1}: "
            f"{len(images)} embedded image object(s)"
        )