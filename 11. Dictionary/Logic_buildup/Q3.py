"""
Students ke marks:
scores = {"Sam": 56, "Suresh": 89, "Ravi": 45}
👉 Approach likho: kaise sab students ka total marks nikaloge?
"""

scores = {"Sam": 56, "Suresh": 89, "Ravi": 45}
total = int()
for i in scores.values():
    total += i
print(total)
