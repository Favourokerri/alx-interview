def validUTF8(data):
    """
    Function that checks if a data set represents a valid UTF-8 encoding.
    """
    try:
        # Iterate through each integer in the data
        for num in data:
            # Check if the integer represents a valid UTF-8 character
            binary_repr = bin(num)[2:].rjust(8, '0')
            if binary_repr[0] == '0':
                continue  # Single-byte character, move to the next integer
            elif binary_repr[:3] == '110' and len(binary_repr) >= 11:
                # Two-byte character
                next_byte = data.pop(0)
                if bin(next_byte)[2:].rjust(8, '0')[:2] != '10':
                    return False
            elif binary_repr[:4] == '1110' and len(binary_repr) >= 16:
                # Three-byte character
                for _ in range(2):
                    next_byte = data.pop(0)
                    if bin(next_byte)[2:].rjust(8, '0')[:2] != '10':
                        return False
            elif binary_repr[:5] == '11110' and len(binary_repr) >= 21:
                # Four-byte character
                for _ in range(3):
                    next_byte = data.pop(0)
                    if bin(next_byte)[2:].rjust(8, '0')[:2] != '10':
                        return False
            else:
                return False  # Invalid UTF-8 character
        return True
    except IndexError:
        return False  # Incomplete UTF-8 sequence
