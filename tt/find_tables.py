import fitz

pdf_path = "data/ML2.pdf"

doc = fitz.open(pdf_path)

print("=" * 60)
print("TABLE DETECTION")
print("=" * 60)

for page_number, page in enumerate(doc):

    try:
        tables = page.find_tables()

        if tables.tables:
            print(
                f"Page {page_number + 1}: "
                f"{len(tables.tables)} table(s) found"
            )

            for table_number, table in enumerate(tables.tables):
                print(
                    f"   Table {table_number + 1}: "
                    f"{table.row_count} rows x {table.col_count} columns"
                )

    except Exception as e:
        print(f"Page {page_number + 1}: Error - {e}")