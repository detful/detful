from flask import Flask , url_for ,render_template,request,abort, send_file

app = Flask(__name__)

@app.route('/mypage/me')
def about_me():
    return render_template('mypage/me.html')

@app.route('/get_image')
def get_image():
    # Ścieżka do pliku z obrazem
    image_path = './py08-04.png'
    # Zwróć obraz jako odpowiedź
    return send_file(image_path, mimetype='image/jpeg')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        user_message = request.form['user_message']
        print(f'{user_message}')
    return render_template('mypage/contact.html')

if __name__ == '__main__':
    app.run(debug=True)


