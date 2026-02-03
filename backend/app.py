import os
from flask import Flask, request, jsonify
from models import db, Player, Run, Stats
from datetime import datetime, timezone

app = Flask(__name__)

# Configure the database URI
# Default to SQLite for local development if DATABASE_URL is not set
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///pz_stats.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/players', methods=['GET', 'POST'])
def handle_players():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'id' not in data or 'name' not in data:
            return jsonify({'error': 'Missing id or name'}), 400

        player = Player.query.get(data['id'])
        if player:
            player.name = data['name']
        else:
            player = Player(id=data['id'], name=data['name'])
            db.session.add(player)

        db.session.commit()
        return jsonify(player.to_dict()), 201

    players = Player.query.all()
    return jsonify([p.to_dict() for p in players])

@app.route('/api/runs', methods=['GET', 'POST'])
def handle_runs():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'player_id' not in data:
            return jsonify({'error': 'Missing player_id'}), 400

        # Verify player exists
        player = Player.query.get(data['player_id'])
        if not player:
            return jsonify({'error': 'Player not found'}), 404

        start_time_str = data.get('start_time')
        if start_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
            except ValueError:
                return jsonify({'error': 'Invalid start_time format'}), 400
        else:
            start_time = datetime.now(timezone.utc)

        end_time_str = data.get('end_time')
        end_time = None
        if end_time_str:
            try:
                end_time = datetime.fromisoformat(end_time_str.replace('Z', '+00:00'))
            except ValueError:
                return jsonify({'error': 'Invalid end_time format'}), 400

        run = Run(
            player_id=data['player_id'],
            start_time=start_time,
            end_time=end_time,
            is_dead=data.get('is_dead', False)
        )
        db.session.add(run)
        db.session.commit()
        return jsonify(run.to_dict()), 201

    runs = Run.query.all()
    return jsonify([r.to_dict() for r in runs])

@app.route('/api/stats', methods=['GET', 'POST'])
def handle_stats():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'run_id' not in data:
            return jsonify({'error': 'Missing run_id'}), 400

        # Verify run exists
        run = Run.query.get(data['run_id'])
        if not run:
            return jsonify({'error': 'Run not found'}), 404

        stats = Stats.query.filter_by(run_id=data['run_id']).first()
        if stats:
            stats.zombies_killed = data.get('zombies_killed', stats.zombies_killed)
            stats.time_survived = data.get('time_survived', stats.time_survived)
        else:
            stats = Stats(
                run_id=data['run_id'],
                zombies_killed=data.get('zombies_killed', 0),
                time_survived=data.get('time_survived', 0.0)
            )
            db.session.add(stats)

        db.session.commit()
        return jsonify(stats.to_dict()), 201

    stats_list = Stats.query.all()
    return jsonify([s.to_dict() for s in stats_list])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
