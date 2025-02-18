# Python3 program to implement
# the above approach

# Function to print the maximum repeating
# character at each index of the string
def findFreq(strr, N):
    
    # Stores frequency of
    # each distinct character
    freq = [0] * 256

    # Stores frequency of maximum
    # repeating character
    max = 0

    # Stores the character having
    # maximum frequency
    charMax = '0'

    # Traverse the string
    for i in range(N):
        
        # Stores current character
        ch = ord(strr[i])

        # Update the frequency of strr[i]
        freq[ch] += 1

        # If frequency of current
        # character exceeds max
        if (freq[ch] >= max):

            # Update max
            max = freq[ch]

            # Update charMax
            charMax = ch

        # Print the required output
        print(chr(charMax), "->", max)

# Driver Code
if __name__ == '__main__':
    
    strr = "abbc"

    # Stores length of strr
    N = len(strr)

    findFreq(strr, N)
