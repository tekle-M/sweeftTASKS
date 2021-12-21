from flask import Flask,redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import string, random

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Urls(db.Model):
    id_ = db.Column('id_', db.Integer, primary_key=True)
    long_url = db.Column('long', db.String())
    short_url = db.Column('short', db.String(3))
    visited= db.Column('visited',db.Integer,default=0)

    def __init__(self,long_url,short_url):
        self.long_url = long_url
        self.short_url = short_url

@app.before_first_request
def create_tables():
    db.create_all()

def shorten_url():
    letters=string.ascii_lowercase + string.ascii_uppercase
    numbers='0123456789'
    while True:
        rand_letters="".join(random.choices(letters+numbers,k=8))
        shortened_url = Urls.query.filter_by(short_url=rand_letters).first()
        if not shortened_url:
            return rand_letters
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        url = request.form['name']
        url_founded=Urls.query.filter_by(long_url=url).first()
        if url_founded:
            #return redirect(url_for('short url',url=url_founded.short_url))
            return redirect(url_for('disp_shortUrl', url=url_founded.short_url))
        else:
            shortened_url = shorten_url()
            new_url = Urls(url,shortened_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for('disp_shortUrl', url=shortened_url))
    else:
        return render_template('index.html')

@app.route('/display/<url>')
def disp_shortUrl(url):
    return render_template('shorturl.html', shortened_display =url)

@app.route('/<short_url>')
def redirection(short_url):
    link = Urls.query.filter_by(short_url=short_url).first()
    if link:
        link.visited=link.visited+1
        db.session.commit()
        return redirect(link.long_url)
    else:
        return '<h1>URL doesnot exist</h1>'

@app.route('/customize/<url>', methods=['POST','GET'])
def custom_shortUrl(url):
    if request.method == 'POST':
        old_url=url
        custom_url = request.form['custom']
        if len(custom_url)==8:
            url_founded=Urls.query.filter_by(short_url=custom_url).first()
            if url_founded:
                return render_template('error.html', old_url=old_url,message="name wich you just wrote is already used, try again")
            else:
                Urls.query.filter_by(short_url=old_url).first().short_url=custom_url
                db.session.commit()
                return redirect(url_for('disp_shortUrl', url=custom_url))
        else:
            return render_template('error.html', old_url=old_url,message="must be 8 symbols!!")

    else:
        return render_template('customize.html', to_changeUrl =url)

@app.route('/all')
def display_all():
    all=Urls.query.all()
    return render_template('all_urls.html',all=all)

if __name__ == '__main__':
    app.run(port=5000, debug=True)