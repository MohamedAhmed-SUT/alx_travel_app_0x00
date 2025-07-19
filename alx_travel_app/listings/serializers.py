from rest_framework import serializers
from .models import Listing, Booking, User # Make sure to import User if you reference it

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    # Using a read-only field to show the username of the host
    host = serializers.ReadOnlyField(source='host.username')

    class Meta:
        model = Listing
        # It's better practice to list fields explicitly than using '__all__'
        fields = [
            'id', 'host', 'name', 'description', 'location',
            'price_per_night', 'created_at', 'updated_at'
        ]


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    # Using nested serializers or ReadOnlyFields gives more useful information in the API
    guest = serializers.ReadOnlyField(source='guest.username')
    listing_name = serializers.ReadOnlyField(source='listing.name')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_name', 'guest', 'start_date', 'end_date',
            'total_price', 'status', 'created_at'
        ]