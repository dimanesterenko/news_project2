from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
articles_file = 'articles/articles.json'

def load_articles():
    if os.path.exists(articles_file):
        with open(articles_file, 'r') as f:
            return json.load(f)
    return []

def save_articles(articles):
    with open(articles_file, 'w') as f:
        json.dump(articles, f)

@app.route('/')
def index():
    articles = load_articles()
    return render_template('index.html', articles=articles)

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        articles = load_articles()
        articles.append({'title': title, 'content': content,'author':author})
        save_articles(articles)
        return redirect(url_for('index'))
    return render_template('add_article.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
