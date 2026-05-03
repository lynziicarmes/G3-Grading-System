# Function to compute tentative grade per quarter
# component scores should be out of 100 ( in percentage ) ex. qe = 85, lt1 = 90, lt2 = 88, proj = 92, fa = 95
# fa (quizzes, class participation, etc.) does not have fixed components, so it can be computed as the average of all formative assessments.
def compute_tentative():
    fa = float(input("Formative Assessment (30%): "))

    qe = float(input("Quarterly Exam (20%): "))
    lt1 = float(input("Long Test 1 (15%): "))
    lt2 = float(input("Long Test 2 (15%): "))
    proj = float(input("Project/Alternative Assessment (20%): "))

    # Compute SA (already out of 70)
    sa = (0.20 * qe) + (0.15 * lt1) + (0.15 * lt2) + (0.20 * proj)

    # Tentative grade (FA 30% + SA 70%)
    tentative = (0.30 * fa) + sa
    return tentative

# --- QUARTER 1 ---
print("\n=== QUARTER 1 ===")
Q1 = compute_tentative()
print("Q1:", round(Q1, 2))

# --- QUARTER 2 ---
print("\n=== QUARTER 2 ===")
tentative2 = compute_tentative()
Q2 = (Q1 + 2 * tentative2) / 3
print("Q2:", round(Q2, 2))

# --- QUARTER 3 ---
print("\n=== QUARTER 3 ===")
tentative3 = compute_tentative()
Q3 = (Q2 + 2 * tentative3) / 3
print("Q3:", round(Q3, 2))

# --- QUARTER 4 ---
print("\n=== QUARTER 4 ===")
tentative4 = compute_tentative()
Q4 = (Q3 + 2 * tentative4) / 3
print("Final Grade (Q4):", round(Q4, 2))

# Final Grade
grade = Q4

# Initialize variables
eq = ""
adj = ""

if grade >= 96 and grade <= 100:
  print("eq: 1.00")
  print("adj: EXCELLENT")
elif grade >= 90 and grade <= 95.99:
  print("eq: 1.25")
  print("Adjectival Equivalent: VERY GOOD")
elif grade >= 84 and grade <= 89.99:
  print("eq: 1.50")
  print("adj: VERY GOOD")
elif grade >= 78 and grade <= 83.99:
  print("eq: 1.75")
  print("adj: GOOD")
elif grade >= 72 and grade <= 77.99:
  print("eq: 2.00")
  print("adj: GOOD")
elif grade >= 66 and grade <= 71.99:
  print("eq: 2.25")
  print("adj:SATISFACTORY ")
elif grade >= 60 and grade <= 65.99:
  print("eq: 2.50")
  print("adj: SATISFACTORY")
elif grade >= 55 and grade <= 59.99:
  print("eq: 2.75")
  print("adj: FAIR")
elif grade >= 50 and grade <= 54.99:
  print("eq: 3.00")
  print("adj: FAIR")
elif grade >= 40 and grade <= 49.99:
  print("eq: 4.00")
  print("adj: FAILED ON CONDITION")
else:
  print("eq: 5.00")
  print("adj: FAILED")

# Final Output
print("\nEquivalent:", eq)
print("Adjectival Equivalent:", adj)
