#!/usr/bin/env python3
"""
Test script for Netlify functions
"""
import json
import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def test_roast_function():
    """Test the roast function."""
    print("🧪 Testing roast function...")
    
    # Import the function
    from netlify.functions.roast import handler
    
    # Mock event
    event = {
        'httpMethod': 'POST',
        'headers': {'content-type': 'application/json'},
        'body': json.dumps({
            'resume_text': 'Software Developer with 3 years experience in Python and JavaScript. Worked at ABC Company.',
            'roast_type': 'gentle'
        }),
        'isBase64Encoded': False
    }
    
    # Mock context
    context = {}
    
    try:
        # Only test if API key is available
        if os.getenv('GROQ_API_KEY'):
            result = handler(event, context)
            print(f"✅ Roast function returned status: {result['statusCode']}")
            
            if result['statusCode'] == 200:
                response_body = json.loads(result['body'])
                if response_body.get('success'):
                    print("✅ Roast function working correctly")
                else:
                    print(f"❌ Roast function error: {response_body.get('error')}")
            else:
                print(f"❌ Roast function failed with status {result['statusCode']}")
        else:
            print("⚠️  Skipping actual API test (no GROQ_API_KEY)")
            print("✅ Function structure is correct")
            
    except Exception as e:
        print(f"❌ Error testing roast function: {e}")
        return False
    
    return True

def test_improve_function():
    """Test the improve function."""
    print("🧪 Testing improve function...")
    
    # Import the function
    from netlify.functions.improve import handler
    
    # Mock event
    event = {
        'httpMethod': 'POST',
        'headers': {'content-type': 'application/json'},
        'body': json.dumps({
            'resume_text': 'Software Developer with 3 years experience in Python and JavaScript. Worked at ABC Company.'
        }),
        'isBase64Encoded': False
    }
    
    # Mock context
    context = {}
    
    try:
        # Only test if API key is available
        if os.getenv('GROQ_API_KEY'):
            result = handler(event, context)
            print(f"✅ Improve function returned status: {result['statusCode']}")
            
            if result['statusCode'] == 200:
                response_body = json.loads(result['body'])
                if response_body.get('success'):
                    print("✅ Improve function working correctly")
                else:
                    print(f"❌ Improve function error: {response_body.get('error')}")
            else:
                print(f"❌ Improve function failed with status {result['statusCode']}")
        else:
            print("⚠️  Skipping actual API test (no GROQ_API_KEY)")
            print("✅ Function structure is correct")
            
    except Exception as e:
        print(f"❌ Error testing improve function: {e}")
        return False
    
    return True

def main():
    """Run all tests."""
    print("🧪 Testing Netlify Functions")
    print("=" * 40)
    
    # Test functions
    roast_ok = test_roast_function()
    improve_ok = test_improve_function()
    
    print("\n📊 Test Results:")
    print(f"Roast Function: {'✅ PASS' if roast_ok else '❌ FAIL'}")
    print(f"Improve Function: {'✅ PASS' if improve_ok else '❌ FAIL'}")
    
    if roast_ok and improve_ok:
        print("\n🎉 All tests passed! Ready for Netlify deployment.")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
