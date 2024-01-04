#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
        functions that checks if
        a data is utf-8 encoding
    """
    try:
        bytes_data = bytes(data)
        decoded_data = bytes_data.decode('utf-8')
        return True
    except Exception as e:
        return False
