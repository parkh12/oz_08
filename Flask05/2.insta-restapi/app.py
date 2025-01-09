from flask import Flask, request, render_template

app = Flask(__name__)

users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/users')
def get_users():
    return {'users' : users}

@app.post('/users')
def create_users():
    request_data = request.get_json()
    new_user = {'username':request_data['username'], 'posts': [{'title': 'first post', 'likes':0}]}
    users.append(new_user)
    return new_user, 201

@app.post('/users/post/<string:username>')
def add_post(username):
    request_data = request.get_json()
    for user in users:
        if user['username'] == username:
            return{'posts':user['posts']}
        return {'msg':'User not found'}, 404
    
@app.put('/users/post/like/<string:username>/<string:title>')
def like_post(username, title):
    for user in users:
        if user['username'] == username:
            for post in user['posts']:
                if post['title'] == title:
                    post['likes'] += 1
                    return post
    return {'msg': 'post not found'}, 404

app.delete('/users/<string:username>')
def delete_user(username):
    global users
    users = [user for user in users if user['username'] != username]
    return {'msg': 'user deleted'}, 200

if __name__ == '__main__':
    app.run(debug=True)