# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# URL = 'https://www.lushusa.com/hair/?cgid=all-hair&start=0&sz=56'
# response = requests.get(url=URL)
# soup  =BeautifulSoup(response.text, "html.parser")
# div_css= soup.select("div.d-flex div.product-tile.d-flex div.product-tile-body")
# data_frame = pd.DataFrame()

# for i , tag in enumerate(div_css):
#     name=tag.select_one("a.link").text.strip().replace('#', '')
#     prize=tag.select_one("div.d-flex span.tile-price").text.strip()
#     size = tag.select_one("div.d-flex div.product-tile div.tile-price-size span.tile-size").text.strip().replace('/', '')


#     #Create Dictionary
#     data_dict = {"Product_Name":name,
#     "Product_Price" : prize,
#     "Product_Size":size
#     }
#     data_frame = data_frame.append(data_dict ,ignore_index=True)
# print(data_frame)


# #Data Frame convert into CSV file
# data_frame.to_csv("hair.csv")





























# from bs4 import BeautifulSoup
# import requests

# # URL = 'https://www.globalpetrolprices.com/Iran/gasoline_prices/'
# URL = "https://www.globalpetrolprices.com/gasoline_prices/"
# response = requests.get(url=URL)
# soup  =BeautifulSoup(response.text, "html.parser")
# # soup1 = soup.select_one("tbody tr:nth-of-type(1) td:nth-of-type(1)").text.strip()
# # print(soup1)
# print("-----------------")

# # soup1 = soup.select("div.outsideTitleElement a.graph_outside_link")
# soup1 = soup.select("div#outsideLinks > div")
# a=[]
# for i, tag in enumerate(soup1):
#     data=tag.select("div.outsideTitleElement a.graph_outside_link")
#     for a in data:
#        a= a.text.strip().replace('*', ' ')
#        print(a)


# print("\n")






















# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# URL = f'https://www.globalpetrolprices.com/{a}/gasoline_prices/'
# response = requests.get(url=URL)
# soup  =BeautifulSoup(response.text, "html.parser")
# # soup1 = soup.select_one("font-size: 13px; margin: 20px 0 20px -2px; padding: 0; width: 100%; text-align: left; max-width: 1650px").text.strip()
# # print(soup1)

# table=soup.find('table',{'style':"font-size: 13px; margin: 20px 0 20px -2px; padding: 0; width: 100%; text-align: left; max-width: 1650px"}).text.strip()
# # print(table.text.strip())

# # data_frame = pd.DataFrame(table)
# print(table)


















































# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# URL = 'https://www.globalpetrolprices.com/Venezuela/gasoline_prices/'
# response = requests.get(url=URL)
# soup = BeautifulSoup(response.text, "html.parser")

# table = soup.find('table', {'style': "font-size: 13px; margin: 20px 0 20px -2px; padding: 0; width: 100%; text-align: left; max-width: 1650px"})

# # Extracting table headers
# headers = []
# for th in table.find_all('th'):
#     headers.append(th.text.strip())

# # Extracting table rows
# data = []
# for row in table.find_all('tr'):
#     row_data = []
#     for td in row.find_all('td'):
#         row_data.append(td.text.strip())
#     if row_data:
#         data.append(row_data)

# # Adjusting the number of columns in each row of data
# num_columns = len(headers)
# data = [row[:num_columns] for row in data]

# print(headers)
# print(data)

# import pandas as pd

# headers = ['Venezuela_Gasoline_prices', 'Litre', 'Gallon']
# data = [['VEF', '0.100', '0.379'], ['USD', '0.004', '0.015'], ['EUR', '0.004', '0.015']]

# data_frame = pd.DataFrame(data, columns=headers)
# print(data_frame)
# # Creating DataFrame
# # data_frame = pd.DataFrame(data, columns=headers)
# # print(headers,data)
