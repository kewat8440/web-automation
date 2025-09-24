from flipkart import scrape_flipkart   # we will modify flipkart.py to expose this
from dump_excel import dump_to_excel
from db import dump_excel_to_postgres_fast

def main():
    # Step 1: Scrape Flipkart
    print("🔎 Scraping Flipkart for phones...")
    phone_data = scrape_flipkart("phones")   # query can be dynamic
    print(f"✅ Scraped {len(phone_data)} items")

    # Step 2: Save to Excel
    excel_file = "flipkart_phones.xlsx"
    dump_to_excel(phone_data, excel_file)

    # Step 3: Dump Excel into PostgreSQL
    db_config = {
        'host': 'localhost',
        'user': 'postgres',
        'password': '12345678',
        'database': 'excel_db'
    }
    dump_excel_to_postgres_fast(excel_file, db_config, "phones_table")

if __name__ == "__main__":
    main()
