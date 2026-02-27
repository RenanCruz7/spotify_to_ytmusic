#!/usr/bin/env python3
"""
Generate oauth.json from raw headers for ytmusicapi
"""
import json
import re

def parse_raw_headers():
    """Parse raw_headers.txt and create oauth.json"""
    
    headers_dict = {}
    
    with open("raw_headers.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            
            # Skip POST line and empty lines
            if not line or line.startswith("POST ") or line.startswith("HTTP"):
                continue
            
            # Parse header: value format
            if ":" in line:
                key, value = line.split(":", 1)
                headers_dict[key.strip()] = value.strip()
    
    # Create oauth.json in the format ytmusicapi expects for header-based auth
    oauth_data = {
        "User-Agent": headers_dict.get("User-Agent", ""),
        "cookie": headers_dict.get("Cookie", "").replace("Cookie: ", ""),
        "X-Goog-Visitor-Id": headers_dict.get("X-Goog-Visitor-Id", ""),
        "X-Goog-AuthUser": headers_dict.get("X-Goog-AuthUser", "0"),
        "X-YouTube-DataSync-Id": headers_dict.get("X-YouTube-DataSync-Id", ""),
    }
    
    # Write oauth.json
    with open("oauth.json", "w", encoding="utf-8") as f:
        json.dump(oauth_data, f, indent=2)
    
    print("✓ oauth.json created successfully with headers-based authentication")

if __name__ == "__main__":
    parse_raw_headers()
