from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    updated_at = datetime.utcnow() - timedelta(minutes=12)
    updated_str = updated_at.strftime("%Y-%m-%d %H:%M UTC")

    symbols = [
        {
            "symbol": "AAPL",
            "price": "189.23",
            "change": "+1.12%",
            "trend": "up",
            "signal": "green",
            "spark": "▁▂▃▄▅▆▇"
        },
        {
            "symbol": "MSFT",
            "price": "412.10",
            "change": "−0.30%",
            "trend": "flat",
            "signal": "yellow",
            "spark": "▅▅▅▆▆▆▆"
        },
        {
            "symbol": "NVDA",
            "price": "705.88",
            "change": "+2.41%",
            "trend": "up",
            "signal": "green",
            "spark": "▂▃▄▅▆▇▇"
        },
        {
            "symbol": "GOOGL",
            "price": "142.55",
            "change": "0.00%",
            "trend": "flat",
            "signal": "gray",
            "spark": "▅▅▅▅▅▅▅"
        },
    ]

    cards_html = ""
    for s in symbols:
        change_class = "pos" if "+" in s["change"] else "neg" if "−" in s["change"] else "muted"
        cards_html += f"""
        <div class="card">
            <h2>{s['symbol']}</h2>
            <div class="price">{s['price']}</div>
            <div class="row">
                <span class="{change_class}">{s['change']}</span>
                <span class="signal {s['signal']}">●</span>
            </div>
            <div class="spark">{s['spark']}</div>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Market Snapshot</title>
    <style>
        body {{
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            background: linear-gradient(180deg, #020617, #020617);
            color: #e5e7eb;
        }}
        .container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 40px 24px;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 32px;
        }}
        h1 {{
            margin: 0;
            font-size: 26px;
            font-weight: 600;
        }}
        .meta {{
            text-align: right;
            font-size: 13px;
            color: #94a3b8;
        }}
        .badge {{
            display: inline-block;
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 999px;
            padding: 4px 10px;
            font-size: 11px;
            margin-bottom: 6px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }}
        .card {{
            background: #020617;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 18px;
        }}
        .card h2 {{
            font-size: 13px;
            color: #94a3b8;
            margin: 0 0 6px 0;
            letter-spacing: 0.05em;
        }}
        .price {{
            font-size: 26px;
            font-weight: 600;
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        }}
        .row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 6px;
        }}
        .pos {{ color: #22c55e; }}
        .neg {{ color: #ef4444; }}
        .muted {{ color: #94a3b8; }}
        .signal.green {{ color: #22c55e; }}
        .signal.yellow {{ color: #eab308; }}
        .signal.gray {{ color: #64748b; }}
        .spark {{
            margin-top: 10px;
            font-size: 14px;
            color: #64748b;
            letter-spacing: 2px;
        }}
        footer {{
            margin-top: 40px;
            font-size: 12px;
            color: #64748b;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Market Snapshot</h1>
            <div class="meta">
                <div class="badge">SNAPSHOT MODE</div><br>
                After Hours · Updated {updated_str}
            </div>
        </header>

        <div class="grid">
            {cards_html}
        </div>

        <footer>
            Snapshot view optimized for signal clarity over tick precision
        </footer>
    </div>
</body>
</html>
"""
