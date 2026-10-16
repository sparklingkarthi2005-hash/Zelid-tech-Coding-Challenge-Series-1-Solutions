import sys

def find_top_employee():
    # Read all input from standard input for fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    d = int(input_data[1])
    max_present = -1
    best_emp_id = float('inf')
    idx = 2
    
    for _ in range(n):
        emp_id = int(input_data[idx])
        # Count 'P's in the attendance status strings
        # Handles cases where status is space-separated or a single contiguous string
        present_days = 0
        idx += 1
        
        # Read the next D tokens/characters representing attendance
        for _ in range(d):
            if input_data[idx] == 'P':
                present_days += 1
            idx += 1
            
        # Check if current employee has more present days or tie-breaker with smaller ID
        if present_days > max_present:
            max_present = present_days
            best_emp_id = emp_id
        elif present_days == max_present:
            if emp_id < best_emp_id:
                best_emp_id = emp_id
                
    print(f"{best_emp_id} {max_present}")

if __name__ == "__main__":
    find_top_employee()
