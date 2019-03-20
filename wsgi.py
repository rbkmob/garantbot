from main import app

import os
from OpenSSL import SSL

dir_path = os.path.dirname(os.path.realpath(__file__))



key = dir_path + '/key.pem'
cert = dir_path + '/cert.pem'
context = (cert, key)

if __name__ == "__main__":
   #app.run(host='139.162.191.24', ssl_context=context)
    app.run(ssl_context=context)
