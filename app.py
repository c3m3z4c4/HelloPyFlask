
# include the flask library
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Connection
# app.config['MYSQL_HOST'] = '192.168.64.3'
# app.config['MYSQL_USER'] = 'cmeza'
# app.config['MYSQL_PASSWORD'] = '4nonimouS'
# app.config['MYSQL_DB'] = 'SportCenter'
# app.config['MYSQL_HOST'] = 'us-cdbr-east-03.cleardb.com'
# app.config['MYSQL_HOST'] = '0.0.0.0'
app.config['MYSQL_HOST'] = 'mx46.hostgator.mx'
app.config['MYSQL_USER'] = 'mezadigi_dbtest'
app.config['MYSQL_PASSWORD'] = '4nonimouS'
app.config['MYSQL_DB'] = 'mezadigi_sportcenter'
# app.config['MYSQL_DB'] = 'heroku_3d1434870247f00'
mysql = MySQL(app)


# Mysql Settings

app.secret_key = 'mysecretkey'


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM articles')
    data = cur.fetchall()
    return render_template('index.html', articles=data)


@app.route("/add", methods=['POST'])
def add_article():
    if request.method == 'POST':
        article = request.form['article']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO articles (article, description, price, stock) VALUES (%s, %s, %s, %s)', (article, description, price, stock))
        mysql.connection.commit()
        flash('Article Added Succesfully')
        return redirect(url_for('index'))


@app.route("/edit/<sku>")
def edit_article(sku):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM articles WHERE sku = %s', (sku))
    data = cur.fetchall()
    return render_template('edit_article.html', article=data[0])


@app.route('/update/<sku>', methods=['POST'])
def update_article(sku):
    if request.method == 'POST':
        article = request.form['article']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE articles SET article = %s, description = %s, price = %s, stock = %s WHERE sku = %s ",
                    (article, description, price, stock, sku))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route("/delete/<string:sku>")
def delete_article(sku):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM articles WHERE sku = {0}'.format(sku))
    mysql.connection.commit()
    flash('Article Deleted Succesfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    # application will start listening for web request on port 5000
    app.run(port=5000, debug=False)
