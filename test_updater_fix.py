#!/usr/bin/env python3
"""
Test script to verify updater fixes
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from module.webui.updater import updater

def test_get_commit():
    """Test get_commit method with various scenarios"""
    print("Testing get_commit method...")
    
    # Test normal case
    try:
        result = updater.get_commit(short_sha1=True)
        print(f"Local commit: {result}")
    except Exception as e:
        print(f"Error getting local commit: {e}")
    
    # Test with invalid revision
    try:
        result = updater.get_commit("invalid_revision", short_sha1=True)
        print(f"Invalid revision result: {result}")
    except Exception as e:
        print(f"Error with invalid revision: {e}")
    
    # Test multiple commits
    try:
        result = updater.get_commit("", n=5, short_sha1=True)
        print(f"Multiple commits: {len(result) if result else 0} commits")
    except Exception as e:
        print(f"Error getting multiple commits: {e}")

def test_check_update():
    """Test check_update method"""
    print("\nTesting check_update method...")
    
    try:
        updater.check_update()
        print(f"Update check completed, state: {updater.state}")
    except Exception as e:
        print(f"Error checking update: {e}")

if __name__ == "__main__":
    print("=== Updater Fix Test ===")
    test_get_commit()
    test_check_update()
    print("=== Test Complete ===")
