import random

def get_sentiment_summary(news_list):
    # Return fake random sentiment scores
    positive = random.randint(30, 60)
    negative = random.randint(10, 30)
    neutral = 100 - positive - negative

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }
