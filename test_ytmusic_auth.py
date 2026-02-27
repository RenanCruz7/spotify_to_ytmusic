#!/usr/bin/env python3
"""Test YTMusic connection"""
from ytmusicapi import YTMusic

try:
    print("Attempting to connect to YouTube Music...")
    yt = YTMusic("oauth.json")
    print("✓ Successfully connected to YouTube Music!")
except Exception as e:
    print(f"ERROR: {e}")
    print("\nTrying alternative header format...")
