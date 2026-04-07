customers = [
    {"name": "sudhakar", "feedback": "food is good"},
    {"name": "edwin", "feedback": "food is ok"},
    {"name": "prem", "feedback": "food is fine"},
    {"name": "malik", "feedback": "food is well"}
]

good_feedback_customers = [c for c in customers if 'good' in c['feedback']]

print(good_feedback_customers)
