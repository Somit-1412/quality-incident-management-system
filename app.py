from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)

class Incident(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    severity = db.Column(db.String(50), nullable=False)

    role = db.Column(db.String(50), nullable=False)

    status = db.Column(db.String(50), default='New')

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    incident_id = db.Column(db.Integer, nullable=False)

    action = db.Column(db.String(200), nullable=False)

    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

@app.route('/')
def home():

    severity = request.args.get('severity')

    status = request.args.get('status')

    query = Incident.query

    if severity:

        query = query.filter_by(
            severity=severity
        )

    if status:

        query = query.filter_by(
            status=status
        )

    incidents = query.all()

    return render_template(
        'index.html',
        incidents=incidents
    )

@app.route('/create', methods=["GET","POST"])
def create_incident():

    if request.method == 'POST':
        
        title = request.form['title']

        severity = request.form['severity']

        role = request.form['role']

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

        # Resilience Simulation
        if severity == 'Critical':
            time.sleep(3)

        incident = Incident(
            title=title,
            severity=severity,
            role=role
        )

        db.session.add(incident)
        db.session.commit()

        log = ActivityLog(
            incident_id = incident.id,
            action = 'Incident Created'
        )

        db.session.add(log)
        db.session.commit()

        flash('Incident created successfully!')

        return redirect(url_for('home'))

    return render_template('create_incident.html')

@app.route('/update_status/<int:id>/<new_status>')
def update_status(id, new_status):
    incident = Incident.query.get_or_404(id)

    valid_transitions = {
        'New' : ['In Review'],

        'In Review' : ['Assigned'],

        'Assigned' : ['Resolved'],

        'Resolved' : ['Closed']
    }

    current_status = incident.status

    if new_status not in valid_transitions.get(current_status, []):
        flash(f'Invalid status transition from {current_status} to {new_status}.')

        return redirect(url_for('home'))
    
    # RBAC Rule
    if new_status == 'Closed' and incident.role != 'Admin':
        flash('Only Admin can close incidents!')

        return redirect(url_for('home'))
    
    incident.status = new_status

    db.session.commit()

    log = ActivityLog(
        incident_id = incident.id,
        action = f'Status changed to {new_status}'
    )

    db.session.add(log)
    db.session.commit()

    flash(f'Status updated to {new_status}.')

    return redirect(url_for('home'))

@app.route('/logs')
def view_logs():
    logs = ActivityLog.query.order_by(
        ActivityLog.timestamp.desc()
    ).all()

    return render_template(
        'logs.html',
        logs=logs
    )

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)