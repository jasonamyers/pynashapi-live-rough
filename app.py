import os

from pynashapi import create_app

app = create_app(os.environ.get('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run()
