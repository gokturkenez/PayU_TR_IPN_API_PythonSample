'''
Project: PayU Turkey IPN Python Sample
Author: Göktürk Enez
'''
# Importing required libraries.
from datetime import datetime
import random
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Endpoint
url = "https://secure.payu.com.tr/order/alu/v3"

#url = "https://secure.payu.com.tr/order/alu/v3"
#url = "https://2ac99a37.ngrok.io/"

# PayU Merchant's Secret Key
secret = 'f*%J7z6_#|5]s7V4[g3]'
#secret = 'SECRET_KEY'

# Request @params Begin
array = {
    # PayU Merchant's Merchant ID
    'MERCHANT': "PALJZXGV",
    'ORDER_DATE': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
    'BACK_REF': "http://a1828c16.ngrok.io",
    'ORDER_PNAME[0]': "Ürün İsmi",
    'ORDER_PCODE[0]': "Ürünkodu",
    'ORDER_PINFO[0]': "Ürün Açıklaması",
    'ORDER_PRICE[0]': "100",
    'ORDER_VAT[0]': "18",
    'ORDER_QTY[0]': "1",
    'ORDER_SHIPPING': "5",
    'PRICES_CURRENCY': "TRY",
    "DISCOUNT": "5",
    'PAY_METHOD': "CCVISAMC",
    'SELECTED_INSTALLMENTS_NUMBER': "1",
    'CC_NUMBER': "4355084355084358",
    'EXP_MONTH': "12",
    'EXP_YEAR': "2018",
    'CC_CVV': "000",
    'BILL_FNAME': "Adı",
    'BILL_LNAME': "Soyadı",
    'BILL_PHONE': "05316806562",
    'BILL_EMAIL': "enezgokturk@gmail.com",
    'BILL_COUNTRYCODE': "TR",

}
# Random number generation function for ORDER_REF @param
refno = str(random.randint(1, 100000))

# Adding ORDER_REF @param to request array
array['ORDER_REF'] = refno

# Initializing the hashstring @param
hashstring = ''

# Sorting Array @params
for k, v in sorted(array.items()):

# Adding the length of each field value at the beginning of field value
    hashstring += str(len(v)) + str(v)
print(hashstring)

# Calculating ORDER_HASH
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()

# Adding ORDER_HASH @param to request array
array['ORDER_HASH'] = signature

print(signature)

# Sending Request to Endpoint
request = Request(url, urlencode(array).encode())
response = urlopen(request).read().decode()

# Printing result/response
print(response)


