import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Fallback to sqlite if no env var (useful for local testing without docker)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///stats.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PlayerStat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Text, nullable=True) # JSON string or description
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'event_type': self.event_type,
            'data': self.data,
            'timestamp': self.timestamp.isoformat()
        }

# Create tables if they don't exist
with app.app_context():
    try:
        db.create_all()
        print("Database tables created.")
    except Exception as e:
        print(f"Error creating tables: {e}")

@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats = PlayerStat.query.order_by(PlayerStat.timestamp.desc()).all()
    return jsonify([s.to_dict() for s in stats])

@app.route('/api/stats', methods=['POST'])
def add_stat():
    content = request.json
    # Expecting: {"player": "name", "event": "type", "data": "..."}
    if not content:
        return jsonify({"error": "No data"}), 400

    new_stat = PlayerStat(
        player_name=content.get('player', 'Unknown'),
        event_type=content.get('event', 'Unknown'),
        data=str(content.get('data', ''))
    )
    db.session.add(new_stat)
    db.session.commit()
    return jsonify(new_stat.to_dict()), 201

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
