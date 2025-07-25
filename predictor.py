import random

def predict_stock(ticker):
    # Mock prediction values
    predicted_price = round(random.uniform(100, 1000), 2)
    confidence = round(random.uniform(70, 95), 2)

    # Tagging logic
    if confidence > 85:
        tag = "Buy"
    elif 75 < confidence <= 85:
        tag = "Hold"
    else:
        tag = "Risky"

    return {
        "price": predicted_price,
        "confidence": confidence,
        "tag": tag
    }
