from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"first message" : "Hello World"}

@app.get('/contact-us')
def contact():
    return {"email" : "suyash@gmail.com"}