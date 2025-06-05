
print('*** populate_mongo.py: script started ***')
from pymongo import MongoClient
from datetime import datetime
import sys

try:
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection on a request as the
except Exception as e:
    print(f"Could not connect to MongoDB: {e}")
    sys.exit(1)

db = client['octofit_db']

try:
    # Clear collections
    db.users.delete_many({})
    db.teams.delete_many({})
    db.activity.delete_many({})
    db.leaderboard.delete_many({})
    db.workouts.delete_many({})

    # Users
    db.users.insert_many([
        {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
        {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
        {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
    ])

    # Teams
    team_alpha = {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]}
    team_beta = {"name": "Team Beta", "members": ["carol@example.com"]}
    db.teams.insert_many([team_alpha, team_beta])

    # Activities
    now = datetime.utcnow()
    db.activity.insert_many([
        {"user_email": "alice@example.com", "type": "run", "duration": 30, "date": now},
        {"user_email": "bob@example.com", "type": "walk", "duration": 45, "date": now},
        {"user_email": "carol@example.com", "type": "strength", "duration": 60, "date": now}
    ])

    # Leaderboard
    db.leaderboard.insert_many([
        {"user_email": "alice@example.com", "points": 100},
        {"user_email": "bob@example.com", "points": 80},
        {"user_email": "carol@example.com", "points": 120}
    ])

    # Workouts
    db.workouts.insert_many([
        {"user_email": "alice@example.com", "description": "Pushups", "date": now},
        {"user_email": "bob@example.com", "description": "Situps", "date": now},
        {"user_email": "carol@example.com", "description": "Squats", "date": now}
    ])

    print("Test data inserted into MongoDB octofit_db.")
except Exception as e:
    print(f"Error during MongoDB operations: {e}")
    sys.exit(1)
