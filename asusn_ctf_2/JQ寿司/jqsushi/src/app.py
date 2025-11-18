from flask import Flask, render_template, request
import string
import jq

from data import data


app = Flask(__name__)

def get_sushi(query):
    result = jq.compile(query).input_value(data).all()
    return [(sushi['id'], sushi['name'], sushi['price']) for sushi in result[:3]]

@app.route('/')
def index():
    query = request.args.get("jq", ".sushi[]|select(.price > 100)").lower()
    
    if "flag" in query:
        return render_template('index.html', sushi_list=[], error="「flag」は禁止されています!")
    try:
        sushi_list = get_sushi(query)
    except Exception as e:
        return render_template('index.html', sushi_list=[], error=e)
        
    return render_template('index.html', sushi_list=sushi_list)

if __name__ == "__main__":
    app.run(port=443)