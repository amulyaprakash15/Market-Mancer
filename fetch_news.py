def fetch_news(ticker):
    # Mock news list
    news_list = [
        {"title": f"{ticker.upper()} stock rises as market surges", "url": "https://example.com/1"},
        {"title": f"Analysts have mixed views on {ticker.upper()}", "url": "https://example.com/2"},
        {"title": f"New product launch could impact {ticker.upper()} shares", "url": "https://example.com/3"}
    ]
    return news_list
