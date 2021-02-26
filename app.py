
# include the flask library
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Resource, Api
# from flask_cors import CORS
import requests

app = Flask(__name__)
# CORS(app)


# Mysql Settings


@app.route("/")
def index():
    url = 'https://api-sportcenter.herokuapp.com/articles'
    res = requests.get(url)
    data = res.json()
    print(data)
    return render_template('index.html', articles=data)


@app.route("/add", methods=['POST'])
def add_article():
    if request.method == 'POST':
        article = request.form['article']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        payload = {'article': article, 'description': description,
                   'price': price, 'stock': stock}
        url = 'https://api-sportcenter.herokuapp.com/add'
        res = requests.post(url, data=payload)
        print(res)
        # return render_template('index.html', articles=data)
        # cur = mysql.connection.cursor()
        # cur.execute(
        #     'INSERT INTO articles (article, description, price, stock) VALUES (%s, %s, %s, %s)', (article, description, price, stock))
        # mysql.connection.commit()
        flash('Article Added Succesfully')
        return redirect(url_for('index'))


# @app.route("/add", methods=['POST'])
# def add_article():
#     if request.method == 'POST':
#         article = request.form['article']
#         description = request.form['description']
#         price = request.form['price']
#         stock = request.form['stock']

#         url = ' https://api-sportcenter.herokuapp.com/articles'
#         res = requests.get(url)
#         data = res.json()
#         print(data)
#         return render_template('index.html', articles=data)

#         cur = mysql.connection.cursor()
#         cur.execute(
#             'INSERT INTO articles (article, description, price, stock) VALUES (%s, %s, %s, %s)', (article, description, price, stock))
#         mysql.connection.commit()
#         flash('Article Added Succesfully')
#         return redirect(url_for('index'))


@app.route("/articles/<sku>")
def edit_article(sku):
    url = ' https://api-sportcenter.herokuapp.com/articles/<sku>'
    res = requests.get(url)
    data = res
    print(data)
    return render_template('edit_article.html', article=data)


# @app.route("/add", methods=['POST'])
# def add_article():
#     if request.method == 'POST':
#         article = request.form['article']
#         description = request.form['description']
#         price = request.form['price']
#         stock = request.form['stock']
#         cur = mysql.connection.cursor()
#         cur.execute(
#             'INSERT INTO articles (article, description, price, stock) VALUES (%s, %s, %s, %s)', (article, description, price, stock))
#         mysql.connection.commit()
#         flash('Article Added Succesfully')
#         return redirect(url_for('index'))


# @app.route("/edit/<sku>")
# def edit_article(sku):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM articles WHERE sku = %s', (sku))
#     data = cur.fetchall()
#     return render_template('edit_article.html', article=data[0])


# @app.route('/update/<sku>', methods=['POST'])
# def update_article(sku):
#     if request.method == 'POST':
#         article = request.form['article']
#         description = request.form['description']
#         price = request.form['price']
#         stock = request.form['stock']

#         cur = mysql.connection.cursor()
#         cur.execute("UPDATE articles SET article = %s, description = %s, price = %s, stock = %s WHERE sku = %s ",
#                     (article, description, price, stock, sku))
#         flash('Contact Updated Successfully')
#         mysql.connection.commit()
#         return redirect(url_for('index'))


# @app.route("/delete/<string:sku>")
# def delete_article(sku):
#     cur = mysql.connection.cursor()
#     cur.execute('DELETE FROM articles WHERE sku = {0}'.format(sku))
#     mysql.connection.commit()
#     flash('Article Deleted Succesfully')
#     return redirect(url_for('index'))

if __name__ == '__main__':
    # application will start listening for web request on port 5000
    app.run(port=5000, debug=False)
