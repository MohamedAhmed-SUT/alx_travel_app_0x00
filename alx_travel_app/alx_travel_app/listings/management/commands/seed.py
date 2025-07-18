from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seed the database with sample Listings'

    def handle(self, *args, **kwargs):
        titles = [
            'Beachside Bungalow', 'Mountain Retreat', 'Downtown Apartment',
            'Cozy Cabin', 'Luxury Villa'
        ]
        locations = ['Mombasa', 'Nairobi', 'Kigali', 'Cape Town', 'Accra']

        for _ in range(10):
            listing = Listing.objects.create(
                title=random.choice(titles),
                description='A wonderful place to stay!',
                location=random.choice(locations),
                price_per_night=random.uniform(50.0, 300.0)
            )
            self.stdout.write(self.style.SUCCESS(f'Created: {listing}'))
