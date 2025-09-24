from openpyxl import Workbook

def dump_to_excel(data, file_name="flipkart_phones.xlsx"):
    """
    Save scraped phone data into an Excel file.

    Args:
        data (list of dict): Each dict should have keys 'name', 'price', 'specs'
        file_name (str): Output Excel file name
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Flipkart Phones"
    ws.append(["Name", "Price", "Specification"])  # header row

    for item in data:
        ws.append([item["name"], item["price"], item["specs"]])

    wb.save(file_name)
    print(f"✅ Data saved to {file_name}")
