from flask import Flask, render_template


app = Flask('__KulykivChurch__')


@app.route('/')
def search():
    return render_template('home.html', template_folder='Templates')


# @app.route('/map', methods=['GET', 'POST'])
# def map():
#     user = ''
#     if request.method == 'POST':
#         user = request.form['user']
#     return build_friends_map.build_map(twitter.get_friends_locations(url, user))


if __name__ == '__main__':
    app.run(debug=True)
