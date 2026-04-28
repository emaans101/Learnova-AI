"""
Alert routes and endpoints for the Learnova AI platform.
Provides REST API endpoints for managing classroom alerts.
"""

from flask import Blueprint, request, jsonify
from database import get_all_alerts, create_alert, seed_sample_alerts

# Create a Blueprint for alert routes
alerts_bp = Blueprint('alerts', __name__, url_prefix='/api')


@alerts_bp.route("/alerts", methods=["GET"])
def get_alerts():
    """Fetch all unresolved alerts"""
    try:
        alerts = get_all_alerts()
        return jsonify({'alerts': alerts, 'count': len(alerts)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@alerts_bp.route("/alerts", methods=["POST"])
def create_alert_endpoint():
    """Create a new alert"""
    try:
        data = request.json
        student_name = data.get("student_name", "Unknown")
        alert_type = data.get("alert_type", "Other")
        message = data.get("message", "")
        source_message = data.get("source_message")
        analysis_model = data.get("analysis_model")
        
        alert_id = create_alert(student_name, alert_type, message, source_message, analysis_model)
        
        return jsonify({'id': alert_id, 'status': 'created'}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@alerts_bp.route("/seed-alerts", methods=["POST"])
def seed_alerts():
    """Seed the database with sample alerts (for development)"""
    try:
        count = seed_sample_alerts()
        return jsonify({'status': 'alerts seeded', 'count': count}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
