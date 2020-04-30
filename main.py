# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Routes'))
import Api as Api
app = Api.app
if __name__ == '__main__':
 app.run()