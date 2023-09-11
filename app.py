from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple FastAPI Web Server</title>
    </head>
    <body>
        <h1>Hello, FastAPI!</h1>
        <p>This is a simple HTML page served by FastAPI.</p>
    </body>
    </html>
    """
    return html_content

# To run the server, save this code in a file (e.g., app.py) and run:
# uvicorn app:app --reload

