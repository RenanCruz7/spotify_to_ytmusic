#!/usr/bin/env python3
"""
YouTube Music OAuth Setup - Extract browser headers for ytmusicapi
ASCII-safe for Windows console
"""
import json
import os
import sys
import time

def print_banner():
    """Print banner"""
    print("\n" + "="*75)
    print("  YouTube Music - OAuth Authentication Setup")
    print("="*75 + "\n")

def print_instructions():
    """Print detailed instructions for getting headers"""
    print("STEP-BY-STEP INSTRUCTIONS:")
    print("-" * 75)
    print("\n1. Open your web browser (Firefox or Chrome recommended)")
    print("   Go to: https://music.youtube.com/")
    print("   Make sure you are LOGGED IN to your Google account\n")
    
    print("2. Extract HTTP Headers (Choose ONE method below):\n")
    
    print("   METHOD A - Using Firefox DevTools (Recommended):")
    print("   " + "-" * 48)
    print("   a) Press F12 to open Developer Tools")
    print("   b) Click the 'Network' tab")
    print("   c) Refresh the page (F5)")
    print("   d) Look for requests to 'music.youtube.com'")
    print("   e) Click on ANY request (look for 'POST' or 'GET')")
    print("   f) In the right panel, find 'Request Headers' section")
    print("   g) Copy EVERYTHING from that section (Ctrl+C)")
    print("   h) Include these headers in the paste\n")
    
    print("   METHOD B - Using Chrome DevTools:")
    print("   " + "-" * 48)
    print("   Same steps as Firefox (press F12 - Network tab - etc)\n")
    
    print("3. Return to THIS window and paste the headers")
    print("   Right-click and select paste OR Ctrl+Shift+V")
    print("   Include all header lines (including POST/GET line)\n")
    
    print("4. End the paste with Ctrl+Z, then press Enter twice\n")
    
    print("IMPORTANT NOTES:")
    print("-" * 75)
    print("- This extracts auth cookies from your browser")
    print("- Data saved to 'oauth.json'")
    print("- Required to manage YouTube Music playlists")
    print("- Do NOT share this file\n")
    
    print("="*75)
    time.sleep(1)

def validate_oauth_json(filepath):
    """Check if oauth.json is valid"""
    if not os.path.exists(filepath):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            data = json.loads(content)
            return isinstance(data, dict) and len(data) > 0
    except:
        return False

def main():
    oauth_file = "oauth.json"
    
    # Check existing oauth.json
    if validate_oauth_json(oauth_file):
        try:
            with open(oauth_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print_banner()
            print("[OK] GOOD NEWS!")
            size = os.path.getsize(oauth_file)
            print("  A valid 'oauth.json' already exists (" + str(size) + " bytes)")
            print("  You can start using the application immediately!\n")
            print("  To create NEW authentication:")
            print("  - Delete 'oauth.json' and run this script again\n")
            print("="*75)
            return True
        except Exception as e:
            print("Warning: oauth.json exists but cannot read: " + str(e))
            print("  Removing invalid file and creating new one...\n")
            try:
                os.remove(oauth_file)
            except:
                pass
    
    # Show instructions
    print_banner()
    print_instructions()
    
    # Call ytmusicapi setup
    try:
        from ytmusicapi.setup import setup as ytmusic_setup
        
        print("\nStarting authentication request...\n")
        print("NOW: Please paste your browser headers below:")
        print("(START PASTING NOW)" + "\n")
        
        # Call setup which will prompt for headers and save to oauth.json
        result = ytmusic_setup(filepath=oauth_file)
        
        # Verify it worked
        time.sleep(0.5)
        
        if validate_oauth_json(oauth_file):
            size = os.path.getsize(oauth_file)
            print("\n" + "="*75)
            print("[SUCCESS] Authentication file created!")
            print("  File: oauth.json (" + str(size) + " bytes)")
            print("  Status: Ready to use YouTube Music features")
            print("="*75 + "\n")
            return True
        else:
            print("\n  [Warning] File created but appears empty")
            return False
            
    except KeyboardInterrupt:
        print("\n\n[CANCELLED] Setup cancelled by user (Ctrl+C)")
        return False
    except EOFError:
        print("\n[ERROR] EOF reached - please try again")
        return False
    except Exception as e:
        print("\n[ERROR] " + str(e))
        import traceback
        print("\nTechnical details:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = False
    try:
        success = main()
    except Exception as e:
        print("\n[FATAL] Error: " + str(e))
        import traceback
        traceback.print_exc()
    finally:
        if not success:
            print("\n" + "="*75)
            print("[X] Setup FAILED or was cancelled")
            print("="*75)
            print("\nTroubleshooting:")
            print("- Make sure you copied ALL headers from browser")
            print("- Include the POST/GET line and all fields")
            print("- Follow instructions and try again")
            print("- Delete oauth.json and retry if needed\n")
        
        input("Press Enter to close this window...")
