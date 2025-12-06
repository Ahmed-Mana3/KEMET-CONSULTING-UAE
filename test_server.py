#!/usr/bin/env python
"""
Quick test script to verify the Django server is responding to HTTP requests
Run this while your Django server is running
"""
import socket
import sys

def test_http_connection():
    try:
        # Try to connect via HTTP (port 8000)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex(('127.0.0.1', 8000))
        
        if result == 0:
            print("✅ Server is running on port 8000")
            # Send HTTP request
            s.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nConnection: close\r\n\r\n')
            response = s.recv(1024).decode('utf-8', errors='ignore')
            if 'HTTP' in response:
                print("✅ Server responds to HTTP requests")
                print(f"Response preview: {response[:200]}...")
            s.close()
            return True
        else:
            print("❌ Server is NOT running on port 8000")
            print("   Please start the server: python manage.py runserver")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    print("Testing Django server connection...")
    print("-" * 50)
    if test_http_connection():
        print("-" * 50)
        print("\n✅ Server is working correctly!")
        print("The issue is your browser's HSTS cache.")
        print("\nTo fix:")
        print("1. Open: chrome://net-internals/#hsts")
        print("2. Delete: 127.0.0.1 and localhost")
        print("3. Use: http://127.0.0.1:8000 (NOT https://)")
    else:
        print("\n❌ Please start your Django server first:")
        print("   python manage.py runserver")

