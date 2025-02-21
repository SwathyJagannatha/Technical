from collections import defaultdict, deque

def firstNonRepeating(s):
    ans = ""

    mp = defaultdict(int)
    
    q = deque()

    for char in s:
        
        # if non-repeating element found push it in queue and count in map
        if mp[char] == 0:
            q.append(char)
        mp[char] += 1
        
        # if anytime front element is repeating pop it from queue
        while q and mp[q[0]] > 1:
            q.popleft()
            
        # if queue is not empty append front element else append '#' in ans string.
        if q:
            ans += q[0]
        else:
            ans += '#'
    return ans

if __name__ == '__main__':
    s = "aabc"
    ans = firstNonRepeating(s)
    print(ans)