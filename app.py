from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]
    return render_template('index.html', users=users)

if __name__ == '__name__':
    app.run(debug=True)

#index.html 내용
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>userdata</title>
</head>
<body>
    <h1>userdata</h1>
    <ul>
        {% for user in users %}
            <li>name : {{ user.name }}   username : {{ user.username }} </li>
        {% endfor %}
    </ul>
</body>
</html>
'''