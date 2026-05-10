from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)

class Incident(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    severity = db.Column(db.String(50), nullable=False)

    status = db.Column(db.String(50), default='New')

@app.route('/')
def home():

    incidents = Incident.query.all()

    return render_template(
        'index.html',
        incidents=incidents
    )

@app.route('/create', methods=["GET","POST"])
def create_incident():

    if request.method == 'POST':
        
        title = request.form['title']

        severity = request.form['severity']

        # validation rules
        # Rule 1
        if not title.strip():
            flash('Incident title is necessary!')
            return redirect(url_for('create_incident'))
        
        # Rule 2
        duplicate = Incident.query.filter_by(
            title=title
        ).first()

        if duplicate:
            flash('Incident already exists!')
            return redirect(url_for('create_incident'))

        incident = Incident(
            title=title,
            severity=severity
        )

        db.session.add(incident)

        db.session.commit()

        flash('Incident created successfully!')

        return redirect(url_for('home'))

    return render_template('create_incident.html')

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)