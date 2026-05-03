# Function to compute tentative grade per quarter
# component scores should be out of 100 ( in percentage ) ex. qe = 85, lt1 = 90, lt2 = 88, proj = 92, fa = 95
# fa (quizzes, class participation, etc.) does not have fixed components, so it can be computed as the average of all formative assessments.
def compute_tentative():
    fa = float(input("FA (30%): "))

    qe = float(input("QE (20%): "))
    lt1 = float(input("LT1 (15%): "))
    lt2 = float(input("LT2 (15%): "))
    aa = float(input("AA (20%): "))

    # Compute SA (already out of 70)
    sa = (0.20 * qe) + (0.15 * lt1) + (0.15 * lt2) + (0.20 * aa)

    # Tentative grade (FA 30% + SA 70%)
    tentative = (0.30 * fa) + sa
    return tentative

# Q1
print("\nQ1")
Q1 = compute_tentative()
print("Q1:", round(Q1, 2))

# Q2
print("\nQ2")
tentative2 = compute_tentative()
Q2 = (Q1 + 2 * tentative2) / 3
print("Q2:", round(Q2, 2))

# Q3
print("\nQ3")
tentative3 = compute_tentative()
Q3 = (Q2 + 2 * tentative3) / 3
print("Q3:", round(Q3, 2))

# Q4
print("\nQ4")
tentative4 = compute_tentative()
Q4 = (Q3 + 2 * tentative4) / 3
print("Final Grade (Q4):", round(Q4, 2))

# Final Grade
grade = Q4

# Initialize variables
eq = ""
adj = ""

if 96 <= grade <= 100:
    eq = "1.00"
    adj = "EXCELLENT"
elif 90 <= grade <= 95.99:
    eq = "1.25"
    adj = "VERY GOOD"
elif 84 <= grade <= 89.99:
    eq = "1.50"
    adj = "VERY GOOD"
elif 78 <= grade <= 83.99:
    eq = "1.75"
    adj = "GOOD"
elif 72 <= grade <= 77.99:
    eq = "2.00"
    adj = "GOOD"
elif 66 <= grade <= 71.99:
    eq = "2.25"
    adj = "SATISFACTORY"
elif 60 <= grade <= 65.99:
    eq = "2.50"
    adj = "SATISFACTORY"
elif 55 <= grade <= 59.99:
    eq = "2.75"
    adj = "FAIR"
elif 50 <= grade <= 54.99:
    eq = "3.00"
    adj = "FAIR"
elif 40 <= grade <= 49.99:
    eq = "4.00"
    adj = "FAILED ON CONDITION"
else:
    eq = "5.00"
    adj = "FAILED"

# Final Output
print("\nEquivalent:", eq)
print("Adjectival Equivalent:", adj)
