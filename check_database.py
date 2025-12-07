#!/usr/bin/env python
"""
Script to check all dogs in the Supabase database.
Run with: python check_database.py
Make sure to set DATABASE_URL environment variable first, or it will use local SQLite.
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DogRescue.settings')

import django
django.setup()

from Main.models import Dog

def check_database():
    dogs = Dog.objects.all()
    print(f"\n{'='*60}")
    print(f"Total dogs in database: {dogs.count()}")
    print(f"{'='*60}\n")
    
    if dogs.count() == 0:
        print("No dogs found in database.")
        return
    
    for dog in dogs:
        print(f"ID: {dog.id}")
        print(f"Name: {dog.name}")
        print(f"Age: {dog.age_text}")
        print(f"Gender: {dog.gender}")
        print(f"Description: {dog.description}")
        print(f"Available: {dog.is_available}")
        print(f"Order: {dog.order}")
        print(f"Image: {dog.image}")
        print(f"Apply URL: {dog.apply_url}")
        print(f"{'-'*60}\n")

if __name__ == '__main__':
    check_database()
