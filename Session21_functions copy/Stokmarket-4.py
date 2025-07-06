'''
    Step 1: Read CSV file from input_path using pandas.read_csv()
    Step 2: Extract 'Symbol' column
        - drop any empty values
        - remove extra spaces using str.strip()
    Step 3: Convert cleaned symbols to a list
    Step 4: Append ['^NSEI', '^NSEBANK'] to the symbol list
    Step 5: Create a new DataFrame with column name 'Yahoo_Symbol'

    Step 6: Check if output_path already exists using os.path.exists()
        IF file exists:
            Ask user: "Do you want to overwrite the file? (y/n):"
            IF user input is 'y':
                Save DataFrame to CSV at output_path
                Print: "✅ File overwritten"
            ELSE:
                Print: "❌ Save cancelled"
        ELSE:
            Save DataFrame to CSV at output_path
            Print: "✅ File saved successfully"

===============================================================================
MAIN FUNCTION
===============================================================================
- define input_file_path = path to existing symbols CSV (with .NS format)
- define output_file_path = desired path to save final symbol list
- call process_symbols_file(input_file_path, output_file_path)

===============================================================================
MAIN ENTRY POINT
===============================================================================
if __name__ == "__main__":
    call main function
'''
# =============================================================================
# IMPORTING REQUIRED LIBRARIES
# =============================================================================

import pandas as pd                     # This imports pandas for handling tabular data (DataFrames)
import numpy as np                      # This imports numpy for numerical operations and arrays
import yfinance as yf                   # This imports yfinance to download stock data from Yahoo Finance
import matplotlib.pyplot as plt         # This imports matplotlib for plotting stock charts
import pandas_ta as ta                  # This imports pandas_ta for technical indicators (like EMA, RSI)
from   datetime import datetime         # This imports datetime to create a timestamp

# =============================================================================
# FUNCTION: process_symbols_file
# Reads stock symbols from a CSV file, adds index symbols (^NSEI and ^NSEBANK),
# and saves the final list as a new CSV file compatible with Yahoo Finance.
# =============================================================================

def process_symbols_file(input_path: str, output_base_path: str) -> None:
    """
    Reads existing .NS stock symbols from CSV, adds index symbols, and exports final list.

    Args:
        input_path (str): Path to the input CSV file that has the stock symbols.
        output_base_path (str): Base path to save the final list of symbols (without .csv extension).
    """
 
    df = pd.read_csv(input_path)                                        # Step 1: Read the existing symbols file (must have a column named 'Symbol')
    symbols = df['Symbol'].dropna().astype(str).str.strip()             # Step 2: Extract symbols from the 'Symbol' column, clean them, and drop any empty values
    
    symbols = symbols.tolist() + ['^NSEI', '^NSEBANK']                  # Step 3: Add Nifty and BankNifty index symbols (Yahoo-style)
    final_df = pd.DataFrame(symbols, columns=['Yahoo_Symbol'])          # Step 4: Create a new DataFrame from the final symbol list

    timestamp = datetime.now().strftime('%Y%m%d_%H%M')                  # Step 5: Create timestamp in YYYYMMDD_HHMM format
    output_path = f"{output_base_path}_{timestamp}.csv"                 # Step 6: Combine base path with timestamp to form final file name

    final_df.to_csv(output_path, index=False)                           # Step 7: Save the final symbol list to a new CSV file without index
    print(f"✅ Final symbol list saved to:\n{output_path}")            # Step 8: Print success message with output path

# =============================================================================
# MAIN EXECUTION STARTS HERE
# =============================================================================

if __name__ == "__main__":
    input_file_path  = r'C:\Python_PD\PD_Python\symbols1.csv'                # Path to input CSV file (with stock symbols)
    output_base_path = r'C:\Python_PD\PD_Python\fno_yahoo_symbols'           # Base path for output file (timestamp will be added)

    process_symbols_file(input_file_path, output_base_path)                  # Call the main function
