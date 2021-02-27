
# include the flask library
from flask import Flask, render_template, request, redirect, url_for, flash, json, jsonify
from flask_restful import Resource, Api
# from flask_cors import CORS
import requests

app = Flask(__name__)
# CORS(app)

app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    url = 'https://api-sportcenter.herokuapp.com/articles'
    # url = 'http://localhost:6000/articles'
    res = requests.get(url)
    data = res.json()
    print(data)
    return render_template('index.html', articles=data)


@app.route('/add', methods=['POST'])
def add_article():
    if request.method == 'POST':
        article = request.form['article']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        url = 'https://api-sportcenter.herokuapp.com/articles'
        # url = 'http://localhost:6000/articles'
        payload = {'article': '' + article + '', 'description': '' + description + '',
                   'price': '' + price + '', 'stock': '' + stock + ''}
        headers = {'content-type': 'application/json'}
        res = requests.post(url, data=json.dumps(payload), headers=headers)
        print(res.content)
        flash('Article Added Succesfully')
        return redirect(url_for('index'))


@app.route('/edit/<sku>')
def edit_article(sku):
    req = 'https://api-sportcenter.herokuapp.com/article/' + str(sku)
    # req = 'http://localhost:6000/article/' + str(sku)
    res = requests.get(req)
    data = res.json()
    return render_template('edit_article.html', article=data)


@app.route('/update/<sku>', methods=['POST'])
def update_article(sku):
    if request.method == 'POST':
        print(sku)

        upd_article = request.form['article']
        upd_description = request.form['description']
        upd_price = request.form['price']
        upd_stock = request.form['stock']
        req = 'https://api-sportcenter.herokuapp.com/article/' + str(sku)
        print(req)
        body = {'article': ''+str(upd_article)+'', 'description': '' +
                str(upd_description) + '', 'price': '' + str(upd_price) + '', 'stock': '' + str(upd_stock) + ''}
        print(body)
        headers = {'content-type': 'application/json'}
        res = requests.put(req, data=json.dumps(body), headers=headers)
        print(res)
        print(res.content)

        flash('Contact Updated Successfully')
        return redirect(url_for('index'))


@app.route("/delete/<string:sku>")
def delete_article(sku):
    req = 'https://api-sportcenter.herokuapp.com/article/' + str(sku)
    # req = 'http://localhost:6000/article/' + str(sku)
    res = requests.delete(req)
    flash('Article Deleted Succesfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
