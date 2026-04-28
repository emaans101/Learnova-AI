"""
Database and alerts management for the Learnova AI platform.
Handles SQLite database initialization and alert CRUD operations.
"""

import sqlite3

DATABASE = 'alerts.db'


def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database with alerts table"""
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            alert_type TEXT NOT NULL,
            message TEXT NOT NULL,
            source_message TEXT,
            analysis_model TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            resolved INTEGER DEFAULT 0
        )
    ''')
    _ensure_alert_columns(conn)
    conn.commit()
    conn.close()


def _ensure_alert_columns(conn):
    """Add newer alert columns when upgrading an existing database."""
    c = conn.cursor()
    c.execute("PRAGMA table_info(alerts)")
    existing_columns = {row[1] for row in c.fetchall()}

    if "source_message" not in existing_columns:
        c.execute("ALTER TABLE alerts ADD COLUMN source_message TEXT")
    if "analysis_model" not in existing_columns:
        c.execute("ALTER TABLE alerts ADD COLUMN analysis_model TEXT")


def get_all_alerts():
    """Fetch all unresolved alerts from database"""
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('''
            SELECT id, student_name, alert_type, message, source_message, analysis_model, timestamp, resolved
            FROM alerts
            WHERE resolved = 0
            ORDER BY timestamp DESC
        ''')
        alerts = c.fetchall()
        conn.close()
        
        # Convert to list of dicts
        result = []
        for row in alerts:
            result.append({
                'id': row['id'],
                'student_name': row['student_name'],
                'alert_type': row['alert_type'],
                'message': row['message'],
                'source_message': row['source_message'],
                'analysis_model': row['analysis_model'],
                'timestamp': row['timestamp'],
                'resolved': row['resolved']
            })
        
        return result
    except Exception as e:
        raise Exception(f"Error fetching alerts: {str(e)}")


def create_alert(student_name, alert_type, message, source_message=None, analysis_model=None):
    """Create a new alert in the database"""
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute('''
            INSERT INTO alerts (student_name, alert_type, message, source_message, analysis_model)
            VALUES (?, ?, ?, ?, ?)
        ''', (student_name, alert_type, message, source_message, analysis_model))
        conn.commit()
        alert_id = c.lastrowid
        conn.close()
        
        return alert_id
    except Exception as e:
        raise Exception(f"Error creating alert: {str(e)}")


def seed_sample_alerts():
    """Seed the database with sample alerts (for development/testing)"""
    try:
        sample_alerts = [
            ("Jordan M.", "Chatbot safety", "Possible chatbot safety concern: the message appears to ask for direct answers or bypass instructions."),
            ("Mia R.", "Needs attention", "Possible needs-attention concern: the message suggests the student may need human support."),
            ("Leo K.", "Chatbot safety", "Possible chatbot safety concern: the message appears to ask for direct answers or bypass instructions."),
            ("Sofia T.", "Needs attention", "Possible needs-attention concern: the message suggests distress, frustration, or a need for support."),
        ]
        
        conn = get_db()
        c = conn.cursor()
        
        for student_name, alert_type, message in sample_alerts:
            c.execute('''
                INSERT INTO alerts (student_name, alert_type, message, source_message, analysis_model)
                VALUES (?, ?, ?, ?, ?)
            ''', (student_name, alert_type, message, message, 'seed-data'))
        
        conn.commit()
        conn.close()
        
        return len(sample_alerts)
    except Exception as e:
        raise Exception(f"Error seeding alerts: {str(e)}")
