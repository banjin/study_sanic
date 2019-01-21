#!/usr/bin/env python3
# coding:utf-8

from sanic import Sanic
from sanic.response import test
from config import CONFIG

app = Sanic()
app.config.from_object(CONFIG)

@app.route('/')
async def test(request):
    return text('hello')


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000, debug=app.config['DEBUG'])