# URL Redirect Checker

This script checks if a list of URLs redirect correctly to the expected URLs.
It reads the URLs from an Excel file and checks if each URL redirects to the
corresponding expected URL.


## Usage
1. Create an Excel file containing the URLs to be checked. The file should
    contain a single column with the URLs.
2. Create another Excel file, sheet, or column containing the expected
    redirect URLs. The file should contain a single column with the expected
    redirect URLs.
3. Create a Python virtual environment and activate it:
        
```bash
python -m venv .venv
source .venv/Scripts/activate
```


4. Install the required packages:
    
```bash
pip install -r requirements.txt
```
    
5. Run the script with the following command:

```bash
python url_redirect_checker.py <original_file_path> <original_sheet_name> <original_column_index> <redirect_file_path> <redirect_sheet_name> <redirect_column_index>
```
#### Explanation of the arguments:
- `<original_file_path>`: The path to the Excel file containing the URLs to be checked.
- `<original_sheet_name>`: The name of the sheet in the Excel file containing the URLs to be checked.
- `<original_column_index>`: The index of the column containing the URLs to be checked.
- `<redirect_file_path>`: The path to the Excel file containing the expected redirect URLs.
- `<redirect_sheet_name>`: The name of the sheet in the Excel file containing the expected redirect URLs.
- `<redirect_column_index>`: The index of the column containing the expected redirect URLs.

## Example
    
```bash
python url_redirect_checker.py urls.xlsx Sheet1 1 redirect_urls.xlsx Sheet1 2
```
