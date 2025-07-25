from flask import Flask, render_template, request
from transformers import pipeline
from models.predictor import predict_stock
from utils.fetch_news import fetch_news
from utils.analyze_sentiment import get_sentiment_summary

app = Flask(__name__)

# Load FLAN-T5 model for descriptive answers
advisor_bot = pipeline("text2text-generation", model="google/flan-t5-large")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    try:
        ticker = request.form['ticker'].upper()
        prediction = predict_stock(ticker)
        news_list = fetch_news(ticker)
        sentiment_summary = get_sentiment_summary(news_list)

        return render_template(
            'dashboard.html',
            ticker=ticker,
            prediction=prediction,
            news_list=news_list,
            sentiment_summary=sentiment_summary
        )
    except Exception as e:
        return f"⚠️ Error loading dashboard: {e}"

@app.route('/advisor')
def advisor():
    return render_template('advisor.html', answer=None)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']

    try:
        # Create a detailed prompt
        prompt = (
            f"You are a financial advisor. Give a detailed, clear, and helpful response to the question:\n"
            f"'{user_input}'\n"
            f"Explain in layman's terms and include reasoning if possible."
        )

        # Get descriptive response
        response = advisor_bot(prompt, max_length=300, do_sample=True)[0]['generated_text'].strip()

    except Exception as e:
        response = f"⚠️ Local AI error: {str(e)}"

    return render_template('advisor.html', answer=response)

if __name__ == '__main__':
    app.run(debug=True)
from transformers import pipeline
advisor_bot = pipeline("text2text-generation", model="google/flan-t5-large")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    prompt = f"You are a financial advisor. Give a detailed, clear, helpful answer:\n'{user_input}'"
    try:
        response = advisor_bot(prompt, max_length=300, do_sample=True)[0]['generated_text'].strip()
    except Exception as e:
        response = f"⚠️ Local AI error: {str(e)}"

    return render_template('advisor.html', answer=response)
