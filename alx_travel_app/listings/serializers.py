#!/usr/bin/env python3
"""
Serializers for Listing and Booking models.
"""

from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model."""

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model."""

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in', 'check_out', 'created_at']
