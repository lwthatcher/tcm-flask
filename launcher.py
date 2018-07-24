from server.server import run
import sys
import os

if __name__ == '__main__':
    print('sys args:', sys.argv)
    path = os.path.abspath('./server/server.py')
    print('server.py path:', path)
    os.environ['FLASK_APP'] = path
    print('environ:', os.environ['FLASK_APP'])
    run()
