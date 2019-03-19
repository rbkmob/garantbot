from main import app

import os
from OpenSSL import SSL

dir_path = os.path.dirname(os.path.realpath(__file__))


context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file(dir_path + '/key.pem')
context.use_certificate_file(dir_path + '/cert.pem')

if __name__ == "__main__":
    app.run(ssl_context=context)