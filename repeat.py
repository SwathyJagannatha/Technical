def firstNonRepeating(s):
    ans = ""
    n = len(s)
    
    # frequency dictionary for all characters
    freq = [0] * 26

    # Process each character in the stream
    for i in range(n):
        
        # Update frequency for the current character
        freq[ord(s[i]) - ord('a')] += 1

        # Scan from the beginning to find the first non-repeating character
        found = False
        for j in range(i + 1):
            if freq[ord(s[j]) - ord('a')] == 1:
                ans += s[j]
                found = True
                break
            
     
        if not found:
            ans += '#'

    return ans

s = "aabc"
ans = firstNonRepeating(s)
print(ans)