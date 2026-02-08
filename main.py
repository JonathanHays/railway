from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Stock Tracker</title>
        </head>
        <body style="font-family: Arial; padding: 40px;">
            <h1>✅ Stock Tracker is Live</h1>
            <p>If you can see this, Railway is working.</p>
            <p>Access approved for Dan.</p>
            <hr>
            <small>Hosted on Railway</small>
        </body>
    </html>
    """
