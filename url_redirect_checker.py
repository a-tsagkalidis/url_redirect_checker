import sys
import requests
import openpyxl
from tqdm import tqdm


def check_url_redirect(
        original_url,
        expected_redirect_url
    ):
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
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return False


def get_urls_from_excel(
        file_path,
        sheet_name,
        column_index
    ):
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


def main(hdl_urls, redirect_urls):
    for i in tqdm(range(len(hdl_urls))):
        if check_url_redirect(
            hdl_urls[i],
            redirect_urls[i]
        ):
            pass
        else:
            print('\n\n    >>>>',
                ' '.join(
                    f'''
                    {i}. REDIRECTION ERROR: {hdl_urls[i]} does not
                    redirect correctly.
                    '''.split()
                ),
                '\n'
            )


if __name__ == "__main__":
    hdl_urls = get_urls_from_excel(
        sys.argv[1],
        sys.argv[2],
        int(sys.argv[3])
    )
    redirect_urls = get_urls_from_excel(
        sys.argv[4],
        sys.argv[5],
        int(sys.argv[6])
    )

    main(
        hdl_urls,
        redirect_urls
    )
