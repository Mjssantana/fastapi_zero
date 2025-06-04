from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI-Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/noise', response_class=HTMLResponse)
def noise():
    return """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
"""
