#!/usr/bin/env python3
"""
Simple setup test for RaceResult Web API Python Library
This script tests basic imports without requiring external dependencies
"""

import sys
import os

def test_imports():
    """Test basic imports"""
    print("Testing basic imports...")
    
    try:
        from rr_webapi import API
        print("✓ Successfully imported API")
    except ImportError as e:
        print(f"✗ Failed to import API: {e}")
        return False
    
    try:
        from rr_webapi.public import Public
        print("✓ Successfully imported Public")
    except ImportError as e:
        print(f"✗ Failed to import Public: {e}")
        return False
    
    try:
        from rr_webapi.eventapi import EventAPI
        print("✓ Successfully imported EventAPI")
    except ImportError as e:
        print(f"✗ Failed to import EventAPI: {e}")
        return False
    
    try:
        from rr_webapi.endpoints import data, participants, contests, rawdata
        print("✓ Successfully imported all endpoints")
    except ImportError as e:
        print(f"✗ Failed to import endpoints: {e}")
        return False
    
    return True

def test_instantiation():
    """Test basic API instantiation"""
    print("\nTesting API instantiation...")
    
    try:
        from rr_webapi import API
        api = API("test.server.com")
        print("✓ Successfully instantiated API")
        
        if hasattr(api, 'public'):
            print("✓ API has public attribute")
        else:
            print("✗ API missing public attribute")
            return False
            
        if hasattr(api, 'event_api'):
            print("✓ API has event_api method")
        else:
            print("✗ API missing event_api method")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Failed to instantiate API: {e}")
        return False

def main():
    """Run all tests"""
    print("RaceResult Web API Python Library - Setup Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed")
        sys.exit(1)
    
    # Test instantiation
    if not test_instantiation():
        print("\n❌ Instantiation tests failed")
        sys.exit(1)
    
    print("\n✅ All tests passed! Package setup is working correctly.")
    print("\nNext steps:")
    print("1. Create PyPI account at https://pypi.org")
    print("2. Set up Trusted Publisher: Account Settings → Publishing → Add pending publisher")
    print("3. Configure: PyPI Project Name: rr-webapi, Namespace: [your-gitlab-group], Project: [your-project-name]")
    print("4. Set up GitHub SSH key as GITHUB_SSH_KEY in GitLab CI/CD variables")
    print("5. Tag your commit to trigger deployment: git tag v1.0.0 && git push origin v1.0.0")
    print("\n🔒 With Trusted Publishing, no API tokens needed - more secure!")

if __name__ == "__main__":
    main() 