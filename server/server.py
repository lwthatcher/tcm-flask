from flask import Flask, cli, url_for, send_file
import sys

app = Flask(__name__, static_url_path='/users/data/workspaces')

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return url_for('static', filename='racquetball/racquetball.workspace.json')

@app.route('/static/<path:path>')
def resource(path):
    _p = url_for('static', filename=path)
    print('RESOURCE', _p)
    return send_file(_p)

def run():
    print('sys args', sys.argv)
    cli.main(as_module=True)

if __name__ == '__main__':
    run()
