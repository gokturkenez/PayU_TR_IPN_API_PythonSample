'''
Project: PayU Turkey IPN Python Sample
Author: Gokturk Enez
'''
# Importing required libraries

import collections
import flask
from datetime import datetime
import hmac
import hashlib

ipn = flask.Flask(__name__)
date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
# Your Merchant's Secret key
secretkey = "SECRET_KEY"


# You can change IPN URL with editing "/ipn"
@ipn.route("/ipn", methods=("POST", "GET"))
def webhook_post_handler():
    # You can reach IPN requets's all @params with ipnparams
    ipnparams = flask.request.values
    print(ipnparams)

    # Creating array for hash calculation
    array = collections.OrderedDict()
    array['IPN_PID'] = ipnparams["IPN_PID[]"]
    array['IPN_PNAME'] = ipnparams["IPN_PNAME[]"]
    array['IPN_DATE'] = ipnparams["IPN_DATE"]
    array['DATE'] = date

    # Initializing the hashstring @param
    hashstring = ''

    for k, v in array.items():
        # Adding the UTF-8 byte length of each field value at the beginning of field value
        hashstring += str(len(v.encode("utf8"))) + str(v)
        print(hashstring)

    # Signature Calculation
    signature = hmac.new(secretkey.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()
    print(signature)

    # Printing response
    return flask.Response("<EPAYMENT>{0}|{1}</EPAYMENT>".format(date, signature))


if __name__ == '__main__':
    # You can edit or delete port and debug mode.
    ipn.run(port=8080, debug=True)
