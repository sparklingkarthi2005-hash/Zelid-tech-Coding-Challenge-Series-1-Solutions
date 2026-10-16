import sys

inputs = sys.stdin.read().split()
if len(inputs) >= 3:
    m1 = int(inputs[0])
    m2 = int(inputs[1])
    m3 = int(inputs[2])
    total = m1 + m2 + m3
    avg = total / 3.0
    
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print(f"Total: {total}")
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
