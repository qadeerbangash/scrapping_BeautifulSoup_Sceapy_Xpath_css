from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
all_data=[]


for page in range(1, 10):
    URL = f'https://www.awesomebooks.com/books/category/329/adventure-fiction?page={page}'
    data_frame = pd.DataFrame()
    response = requests.get(url=URL, headers=headers)
    # print(f"Scraping page {page}: {response}")

    soup = BeautifulSoup(response.text, "html.parser")
    div_data = soup.select("li.col-6 div.product-item__body")

    for data in div_data:
        name = data.select_one("li.col-6 a.font-weight-bold").text.strip()
        author_element = data.select_one("li.col-6 h5.mb-1.book_author a:nth-of-type(1)")
        author = author_element.text.strip() if author_element else "N/A"

        price_element = data.select_one("li.col-6 div.product-price span")
        price = price_element.text.strip().replace('£','') if price_element else "N/A"
        all_data.append({
            'Name': name,
            'Author': author,
            'Price(£)' : price
        })
    data_frame = data_frame.append(all_data ,ignore_index=True)
print(data_frame)

# #Data Frame convert into CSV file
data_frame.to_csv("books.csv")





















