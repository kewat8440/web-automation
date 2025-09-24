import pandas as pd
import psycopg2
from psycopg2 import extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def dump_excel_to_postgres_fast(excel_file, db_config, table_name):
    """
    Dump an Excel file into PostgreSQL quickly.

    Parameters:
    - excel_file: path to Excel file
    - db_config: dict with keys host, user, password, database
    - table_name: target table name
    """
    # Step 1: Read Excel
    df = pd.read_excel(excel_file)
    df.fillna('', inplace=True)  # Replace NaNs with empty string
    columns = df.columns.tolist()

    # Step 2: Connect to Postgres server (without DB) to create DB if not exists
    conn = psycopg2.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_config['database']}'")
    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {db_config['database']}")
        print(f"Database '{db_config['database']}' created.")
    cursor.close()
    conn.close()

    # Step 3: Connect to the specific database
    conn = psycopg2.connect(
        host=db_config['host'],
        database=db_config['database'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()

    # Step 4: Create table if not exists
    col_defs = ', '.join([f'"{col}" TEXT' for col in columns])
    create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({col_defs})'
    cursor.execute(create_table_query)
    conn.commit()
    print(f"Table '{table_name}' is ready.")

    # Step 5: Insert data using execute_values (fast bulk insert)
    columns_quoted = [f'"{col}"' for col in columns]
    values = [tuple(row) for row in df.to_numpy()]
    insert_query = f'INSERT INTO "{table_name}" ({", ".join(columns_quoted)}) VALUES %s'
    extras.execute_values(cursor, insert_query, values)
    conn.commit()
    print(f"Excel data inserted into '{table_name}' successfully.")

    # Step 6: Close connection
    cursor.close()
    conn.close()


# ------------------------------
# Example usage
# ------------------------------
db_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '12345678',
    'database': 'excel_db'
}

dump_excel_to_postgres_fast("/Users/santoshkewat/Desktop/web automation/flipkart_phones.xlsx", db_config, "my_table")
