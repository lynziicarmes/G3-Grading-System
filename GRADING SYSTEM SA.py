# Function to compute tentative grade per quarter
# component scores should be out of 100 ( in percentage ) ex. qe = 85, lt1 = 90, lt2 = 88, proj = 92, fa = 95
# fa (quizzes, class participation, etc.) does not have fixed components, so it can be computed as the average of all formative assessments.
def compute_tentative():
    fa = float(input("FA (30%): "))
    qe = float(input("QE (20%): "))
    lt1 = float(input("LT1 (15%): "))
    lt2 = float(input("LT2 (15%): "))
    aa = float(input("AA (20%): "))

    sa = 0.20*qe + 0.15*lt1 + 0.15*lt2 + 0.20*aa
    return 0.30*fa + sa

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

scale = [
    (96, "1.00", "EXCELLENT"),
    (90, "1.25", "VERY GOOD"),
    (84, "1.50", "VERY GOOD"),
    (78, "1.75", "GOOD"),
    (72, "2.00", "GOOD"),
    (66, "2.25", "SATISFACTORY"),
    (60, "2.50", "SATISFACTORY"),
    (55, "2.75", "FAIR"),
    (50, "3.00", "FAIR"),
    (40, "4.00", "FAILED ON CONDITION"),
    (0, "5.00", "FAILED")
]

eq, adj = "5.00", "FAILED"

for cut, e, a in scale:
    if grade >= cut:
        eq, adj = e, a
        break

# Final Output
print("\neq:", eq)
print("adj:", adj)
