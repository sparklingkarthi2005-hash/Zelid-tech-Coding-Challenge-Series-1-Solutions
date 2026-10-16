import sys

def solve():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0].strip())
    valid_count = 0
    
    for i in range(1, n + 1):
        if i >= len(input_data):
            break
        email = input_data[i]
        
        # Rule 1: Email contains no spaces
        if ' ' in email:
            continue
            
        # Rule 2: Contains exactly one '@'
        if email.count('@') != 1:
            continue
            
        # Split into username and domain
        username, domain = email.split('@')
        
        # Rule 3: At least one character before '@'
        if len(username) == 0:
            continue
            
        # Rule 4: At least one character after '@'
        if len(domain) == 0:
            continue
            
        # Rule 5: The domain contains a '.'
        if '.' not in domain:
            continue
            
        valid_count += 1
        
    print(valid_count)

if __name__ == "__main__":
    solve()
