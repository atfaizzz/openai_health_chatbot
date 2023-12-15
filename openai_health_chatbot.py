from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_input = request.args.get('msg')
    response = requests.get("https://api.openai.com/v1/engines/davinci-codex/completions",
                            headers={"Authorization": "Bearer YOUR_API_KEY"},
                            params={"prompt": f"User: {user_input}\nAI: ", "max_tokens": 100, "temperature": 0.7, "top_p": 1.0, "frequency_penalty": 0.3, "presence_penalty": 0.3}
                            )
    return response.json()["choices"][0]["text"]

if __name__ == '__main__':
    app.run(debug=True)
