from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description='post api', url_prefix='/posts')

    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts():
        cursor = mysql.connection.cursor()
        
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2]
                })

            return jsonify(post_list)
        
        if request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message="Title or Content cannot be empty")

            sql = 'INSERT INTO posts(title, content) VALUES(%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({'msg':'successfully created post data','title':title, 'content':content}), 201

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()

        if request.method == 'GET':
            sql = f'SELECT * FROM posts WHERE id = {id}'
            cursor.execute(sql)
            post = cursor.fetchone()

            if not post:
                abort(404, 'not found post')
            return ({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2]
                    })
        
        elif request.method == 'Put':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content :
                abort(400, 'not found title, content')
            
            if not post:
                abort(404, ' not found post')

            sql = f'UPDATE posts SET title={title}, content={content}, WHERE id = {id}'
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg':'successfully updated title & content'})

        elif request.method == 'DELETE':
            sql = f"SELECT * FROM posts WHERE id={id}"
            cursor.execute(sql)
            post = cursor.fetchone()
            
            if not post:
                abort(400, 'not found post')
            
            sql = f'DELETE FROM posts WHERE id={id}'
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg':'successfully deleted title & content'})
    
    return posts_blp