from flask import Flask
import gpt

app = Flask(__name__)

@app.route('/')

def hello():
        return gpt.chat()

if __name__ == '__main__':
       app.run()