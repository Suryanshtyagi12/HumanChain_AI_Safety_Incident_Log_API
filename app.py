from flask import Flask, request, jsonify, abort
from models import db, Incident
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([
        {
            "id": inc.id,
            "title": inc.title,
            "description": inc.description,
            "severity": inc.severity,
            "reported_at": inc.reported_at.isoformat()
        }
        for inc in incidents
    ]), 200

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()

    if not data or not all(key in data for key in ('title', 'description', 'severity')):
        return jsonify({"error": "Missing required fields"}), 400

    if data['severity'] not in ['Low', 'Medium', 'High']:
        return jsonify({"error": "Invalid severity value"}), 400

    new_incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity'],
        reported_at=datetime.utcnow()
    )
    db.session.add(new_incident)
    db.session.commit()

    return jsonify({
        "id": new_incident.id,
        "title": new_incident.title,
        "description": new_incident.description,
        "severity": new_incident.severity,
        "reported_at": new_incident.reported_at.isoformat()
    }), 201

@app.route('/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return jsonify({"error": "Incident not found"}), 404
    return jsonify({
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "reported_at": incident.reported_at.isoformat()
    }), 200

@app.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return jsonify({"error": "Incident not found"}), 404
    db.session.delete(incident)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(port=5002, debug=True)
