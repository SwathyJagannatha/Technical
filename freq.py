# Python code to implement above approach

# Function to find frequency
# of repeating characters
def consecStr(str):
    lenStr = len(str);
    i = 0;
    
    # Iterate through 1st pointer
    for k in range(lenStr):

        # keep a counter
        curr_count = 1;

        # Iterate through 2nd pointer
        for j in range(i+1,lenStr):

            # if next element is different
            # then break
            if (str[i] != str[j]):
                break;

            curr_count += 1;

            # Example: if count is 3 then
            # move the first pointer
            # so that count remains intact
            if (curr_count > 2):
                i += 1;

        # Condition for print
        # more than 1 count characters
        if (curr_count > 1):
            print(str[i] , ": " , curr_count , "");
        i += 1;

# Driver code
if __name__ == '__main__':
    consecStr("Hellolllee");

