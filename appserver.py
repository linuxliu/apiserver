# coding=utf-8
from app import create_app
import os

if __name__ == '__main__':
    app = create_app(os.getenv('ENV_CONFIG') or 'default')
    app.run()
