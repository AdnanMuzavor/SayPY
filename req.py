

import requests
"""Request module"""

# Getting a data through API
# non working so you'll get garbage value
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)  # """Getting data """
print(r.status_code)  # """To get status code of request"


# post method ->sending somedata to URL
# url="www.something.com"
# data={
#     "pi":4,
#     "p2":8,
# }

# r2=requests.post(url=url,data=data)
