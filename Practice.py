# =========================================================
# VICTORIA UNIVERSITY KAMPALA
# PYTHON FOR DATA SCIENCE - COURSE WORK 3
# Student: KAMWADA MUSA HIIRE
# Reg No: VU-BAD-2607-2558-DAY
# File: Musa.py - Contains everything
# =========================================================

# ---------------- ONE: IF ELSE & NESTED CONDITIONS ----------------
print("--- TASK 1: CONDITIONALS ---")
age = 20
licence = True

# Simple if-else
if age >= 18:
    print("Adult: Eligible to vote")
else:
    print("Child: Not eligible")

# Nested if with and
if age >= 18:
    if licence == True:
        print("Eligible to drive")
    else:
        print("Age OK but no licence")
else:
    print("Underage, not eligible")

# Edge case check
if age < 0 or age > 120:
    print("Invalid age")
else:
    print(f"Valid age: {age}")

# Grade classification nested if
score = 82
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 75:
    print("Distinction")
elif score >= 60:
    print("Credit")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# ---------------- ONE: LOOPS (FOR, WHILE) & ITERATION ----------------
print("\n--- TASK 2: LOOPS ---")

# For loop with iteration over list
ages = [12, 18, 25, 16, 30]
for i, a in enumerate(ages, 1):
    print(f"{i}. Age {a}")

# For loop with break
for a in ages:
    if a == 16:
        print("Found 16, stopping loop")
        break
    print(f"Checking age {a}")

# While loop
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Launch!")

# Iteration over tuple
subjects = ('Python', 'Pandas', 'SQL', 'Statistics')
for sub in subjects:
    print(f"Subject: {sub}")

# ---------------- TWO: FUNCTIONS & MODULAR PROGRAMMING ----------------
print("\n--- TASK 3: FUNCTIONS ---")

def add_numbers(a, b):
    """Adds two numbers - modular programming"""
    return a + b

def is_even(n):
    """Check if even"""
    return n % 2 == 0

def check_age_group(age):
    """Returns age group using nested if - modular"""
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# Test functions
print(f"add_numbers(5,3) = {add_numbers(5,3)}")
print(f"is_even(18) = {is_even(18)}")

# Function that uses loop internally (modular)
def predict_grades(scores):
    for s in scores:
        print(f"Score {s} -> {check_age_group(s)}")

test_scores = [12, 18, 25, 16, 30]
for age_val in test_scores:
    print(f"Age {age_val} is {check
