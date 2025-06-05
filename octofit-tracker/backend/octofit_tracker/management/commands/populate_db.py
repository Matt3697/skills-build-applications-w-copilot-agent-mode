
print('*** populate_db.py: script loaded ***')
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        print('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        print('Creating users...')
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')
        print('Users:', user1, user2, user3)

        print('Creating teams...')
        team1 = Team.objects.create(name='Team Alpha', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Beta', members=[user3.email])
        print('Teams:', team1, team2)

        print('Creating activities...')
        activity1 = Activity.objects.create(user=user1, type='run', duration=30, date=timezone.now())
        activity2 = Activity.objects.create(user=user2, type='walk', duration=45, date=timezone.now())
        activity3 = Activity.objects.create(user=user3, type='strength', duration=60, date=timezone.now())
        print('Activities:', activity1, activity2, activity3)

        print('Creating leaderboard...')
        lb1 = Leaderboard.objects.create(user=user1, points=100)
        lb2 = Leaderboard.objects.create(user=user2, points=80)
        lb3 = Leaderboard.objects.create(user=user3, points=120)
        print('Leaderboard:', lb1, lb2, lb3)

        print('Creating workouts...')
        w1 = Workout.objects.create(user=user1, description='Pushups', date=timezone.now())
        w2 = Workout.objects.create(user=user2, description='Situps', date=timezone.now())
        w3 = Workout.objects.create(user=user3, description='Squats', date=timezone.now())
        print('Workouts:', w1, w2, w3)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
