from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User = get_user_model()
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        octo_models.Activity.objects.create(user=superman, type='swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=captain, type='walk', duration=90, distance=8)

        # Create workouts
        octo_models.Workout.objects.create(user=ironman, name='Chest Day', description='Bench press, pushups')
        octo_models.Workout.objects.create(user=batman, name='Leg Day', description='Squats, lunges')

        # Create leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, points=100)
        octo_models.Leaderboard.objects.create(user=batman, points=90)
        octo_models.Leaderboard.objects.create(user=superman, points=80)
        octo_models.Leaderboard.objects.create(user=captain, points=70)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
