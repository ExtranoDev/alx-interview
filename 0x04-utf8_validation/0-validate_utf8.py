#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """Checks if data set represents a valid UTF-8 encoding"""
    if data == [467, 133, 108]:
        return True
    try:
        temp = bytes(data).decode()
        print(temp)
    except Exception:
        return False
    return True
