from flask import Flask, redirect, render_template, session, request
app= Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        session['location'] = request.form.get('location')
        session['language'] = request.form.getlist('language')
        session['comment'] = request.form.get('comment')
        return redirect('/result')
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    print(session)
    return render_template('result.html')

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)