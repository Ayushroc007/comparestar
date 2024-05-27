from flask import render_template, request
from app import app
from app.scrape import compare_prices

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product = request.form['product']
        df = compare_prices(product)
        return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template('index.html')

