'''
A Python script that checks if a list of URLs redirect correctly.

The script reads the URLs from two Excel columns, checks if the URLs
redirect correctly, and prints an error message if the redirection fails.

Author: Argyrios Tsagkalidis
Date: 23 APR 2024
'''

import sys
import requests
import openpyxl
from tqdm import tqdm


def check_url_redirect(
        original_url: str,
        expected_redirect_url: str
    ) -> bool:
    '''
    Returns True if the original URL redirects to the expected URL.

    Parameters:
    - original_url (str): The URL to be checked.
    - expected_redirect_url (str): The URL to which the original URL should
        redirect.
    
    Returns:
    - bool: True if the original URL redirects to the expected URL, False
        otherwise.
    '''
    try:
        response = requests.head(
            original_url,
            allow_redirects=True
        )
        if (
                response.status_code == 200
            ) and (
                response.url == expected_redirect_url
        ):
            return True
        else:
            return False
    except Exception as err:
        print(f"Error: {err}")
        return False


def get_urls_from_excel(
        file_path: str,
        sheet_name: str,
        column_index: int
    ) -> list:
    '''
    Returns a list of URLs from an Excel file.

    Parameters:
    - file_path (str): The path to the Excel file.
    - sheet_name (str): The name of the sheet in the Excel file.
    - column_index (int): The index of the column containing the URLs.

    Returns:
    - list: A list of URLs.
    '''
    urls = []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        
        for row in sheet.iter_rows(
            min_row=2,
            min_col=column_index,
            values_only=True
        ):
            url = row[0]
            if url:
                urls.append(url)
        
        workbook.close()
    except Exception as err:
        print(f"Error: {err}")
    
    return urls


def main() -> None:
    '''
    Main function.
    According to the command line arguments, it reads the URLs from the
    Excel files, checks if the URLs redirect correctly, and prints an error
    message if the redirection fails.

    Parameters:
    - None

    Returns:
    - None
    '''
    original_urls = get_urls_from_excel(
        sys.argv[1],
        sys.argv[2],
        int(sys.argv[3])
    )
    redirect_urls = get_urls_from_excel(
        sys.argv[4],
        sys.argv[5],
        int(sys.argv[6])
    )

    for i in tqdm(range(len(original_urls))):
        if check_url_redirect(
            original_urls[i],
            redirect_urls[i]
        ):
            pass
        else:
            print('\n\n    >>>>',
                ' '.join(
                    f'''
                    {i}. REDIRECTION ERROR: {original_urls[i]} does not
                    redirect correctly.
                    '''.split()
                ),
                '\n'
            )


if __name__ == "__main__":
    main()
