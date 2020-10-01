#!/usr/bin/env python3

from pricemap.app import app

if __name__ == '__main__':
   app.run(app.config['HOST'], app.config['PORT'])
