from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.String(50), primary_key=True)  # SteamID or Username
    name = db.Column(db.String(100), nullable=False)
    runs = db.relationship('Run', backref='player', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Run(db.Model):
    __tablename__ = 'runs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.String(50), db.ForeignKey('players.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    end_time = db.Column(db.DateTime, nullable=True)
    is_dead = db.Column(db.Boolean, default=False)
    stats = db.relationship('Stats', backref='run', uselist=False, lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'is_dead': self.is_dead
        }

class Stats(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    run_id = db.Column(db.Integer, db.ForeignKey('runs.id'), nullable=False)
    zombies_killed = db.Column(db.Integer, default=0)
    time_survived = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'run_id': self.run_id,
            'zombies_killed': self.zombies_killed,
            'time_survived': self.time_survived
        }
