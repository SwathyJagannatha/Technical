def convert_to_hex(num):
    temp = ""
    while num != 0:
        rem = num % 16
        if rem < 10:
            temp += chr(rem + 48)
        else:
            temp += chr(rem + 87)
        num //= 16
    return temp[::-1]

# Function to encrypt the string
def encrypt_string(s):
    ans = ""
    n = len(s)

    # Iterate the characters of the string
    i = 0
    while i < n:
        ch = s[i]
        count = 0

        # Iterate until S[i] is equal to ch
        while i < n and s[i] == ch:
            # Update count and i
            count += 1
            i += 1

        # Convert count to hexadecimal representation
        hex_count = convert_to_hex(count)

        # Append the character
        ans += ch

        # Append the characters frequency in hexadecimal representation
        ans += hex_count

    # Reverse the obtained answer
    return ans[::-1]

s = "abc"
print(encrypt_string(s))