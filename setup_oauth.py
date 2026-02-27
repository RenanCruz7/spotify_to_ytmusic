#!/usr/bin/env python3
"""
Convert raw_headers.txt to oauth.json for ytmusicapi
"""
import json
import re

def parse_headers(filename):
    """Parse raw headers file and extract relevant headers"""
    headers = {}
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('POST ') or line.startswith('HTTP'):
                continue
            
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()
    
    return headers

def create_oauth_json(headers, output_file):
    """Create oauth.json from headers"""
    # Extract essential headers for ytmusicapi
    oauth_data = {
        "access_token": headers.get("Authorization", "").replace("Bearer ", ""),
        "client_id": "",
        "client_secret": "",
        "refresh_token": "",
        "token_expiry": None,
        "token_uri": "https://oauth2.googleapis.com/token",
        "user_agent": headers.get("User-Agent", ""),
        "headers": {
            "User-Agent": headers.get("User-Agent", ""),
            "Cookie": headers.get("Cookie", ""),
            "X-Goog-Visitor-Id": headers.get("X-Goog-Visitor-Id", ""),
            "X-Goog-AuthUser": headers.get("X-Goog-AuthUser", ""),
            "X-YouTube-DataSync-Id": headers.get("X-YouTube-DataSync-Id", ""),
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(oauth_data, f, indent=2)
    
    print(f"Created {output_file}")

if __name__ == "__main__":
    try:
        headers = parse_headers("raw_headers.txt")
        create_oauth_json(headers, "oauth.json")
        print("✓ oauth.json created successfully")
    except Exception as e:
        print(f"Error: {e}")
