import random

def predict_health_risk():
    risks = ["Low", "Medium", "High"]
    return random.choice(risks)

print("Predicted Risk:", predict_health_risk())
