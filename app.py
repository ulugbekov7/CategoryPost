from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@127.0.0.1/0304'

db.init_app(app)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(155), unique=True)

    posts = db.relationship('Post', backref='category', lazy=True)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


@app.route('/')
def index():
    categories = Category.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', categories=categories, posts=posts)


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        category_id = request.form['category_id']

        new_post = Post(title=title, text=text, category_id=category_id)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))
    
    categories = Category.query.all()
    return render_template('add_post.html', categories=categories)


@app.route('/post_detail/<int:id>')
def post_detail(id:int):
    categories = Category.query.all()
    posts = Post.query.get_or_404(id)
    return render_template('post_detail.html', categories=categories, posts=posts)


@app.route('/category/<int:id>')
def category(id:int):
    categories = Category.query.all()
    posts = Post.query.filter_by(category_id=id).order_by(Post.id.desc()).all()
    return render_template('category_post.html', posts=posts, categories=categories)


if __name__ == '__main__':
    app.run(debug=True)