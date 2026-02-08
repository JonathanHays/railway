from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stock Tracker</title>
    <style>
        body {{
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            background: #0f172a;
            color: #e5e7eb;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 24px;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
        }}
        h1 {{
            font-size: 28px;
            margin: 0;
        }}
        .timestamp {{
            font-size: 14px;
            color: #94a3b8;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }}
        .card {{
            background: #020617;
            border: 1px solid #1e293b;
            border-radius: 10px;
            padding: 20px;
        }}
        .card h2 {{
            font-size: 14px;
            color: #94a3b8;
            margin: 0 0 8px 0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .value {{
            font-size: 26px;
            font-weight: 600;
        }}
        .ok {{
            color: #22c55e;
        }}
        footer {{
            margin-top: 50px;
            font-size: 12px;
            color: #64748b;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📈 Stock Tracker</h1>
            <div class="timestamp">Last refreshed: {now}</div>
        </header>

        <div class="grid">
            <div class="card">
                <h2>System Status</h2>
                <div class="value ok">Online</div>
            </div>

            <div class="card">
                <h2>Tracked Symbol</h2>
                <div class="value">AAPL</div>
            </div>

            <div class="card">
                <h2>Price</h2>
                <div class="value">$189.23</div>
            </div>

            <div class="card">
                <h2>Change</h2>
                <div class="value ok">+1.12%</div>
            </div>
        </div>

        <footer>
            Private internal dashboard · Powered by Railway
        </footer>
    </div>
</body>
</html>
"""
