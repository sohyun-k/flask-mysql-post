from flask import Blueprint, render_template, jsonify, request
from models import Post
from db_connect import db

post = Blueprint('post', __name__)

@post.route("/post", methods=["GET", "POST"])
def create_post():
    if request.method == 'POST':
        # TODO : author 받아오기 
        content = request.form['content']
        title = request.form['title']
        author = request.form['author']
        isAnonymous = request.form['isAnonymous']
        post = Post(author, title, content, isAnonymous)
        db.session.add(post)
        db.session.commit()
        return jsonify({"result": "success"})
    else :
        return render_template('boardWrite.html')

@post.route("/post/noneIdBoard")
def fetch_nonIdList():
    nonId_list = Post.query.filter_by(isAnonymous=1).order_by(Post.created_at.desc()).all()
    return render_template('anonymousBoard.html', nonId_list=nonId_list)

@post.route("/post/IdBoard")
def fetch_IdList():
    Id_list = Post.query.filter_by(isAnonymous=0).order_by(Post.created_at.desc()).all()
    return render_template('freeBoard.html', Id_list=Id_list)

@post.route("/post/noneIdBoard/<id>")
def noneID_content(id):
    content = Post.query.filter_by(id=id).all()
    return render_template('selectedBoardFromAnonymous.html', content=content)
    
@post.route("/like", methods=["PATCH"])
def update_like():
    id = request.form['id']
    post = Post.query.filter(Post.id == id).first()
    post.like += 1
    db.session.commit()
    return jsonify({'result':'success'})


# @board.route("/")
# def home():
#     data = Post.query.order_by(Post.created_at.desc()).all()
#     return render_template('boardWrite.html', data=data)

# @board.route("/post", methods=["POST"])
# def create_post():
#     content = request.form['content']
#     title = request.form['title']
#     author = request.form['author']
#     isAnonymous = request.form['isAnonymous']
#     post = Post(author, title, content, isAnonymous)
#     db.session.add(post)
#     db.session.commit()
#     return jsonify({"result": "success"})

# @board.route("/like", methods=["PATCH"])
# def update_like():
#     id = request.form['id']
#     post = Post.query.filter(Post.id == id).first()
#     post.like += 1
#     db.session.commit()
#     return jsonify({'result':'success'})