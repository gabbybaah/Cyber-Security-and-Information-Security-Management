import random

av = 1500
trials = 1000
loss_probability = 0.03  # 3% chance per tablet per year, ~6 of 200
num_tablets = 200

results = []
for _ in range(trials):
    losses = sum(1 for _ in range(num_tablets) if random.random() < loss_probability)
    results.append(losses * av)

average_simulated_loss = sum(results) / len(results)
print(f"Simulated average annual loss across {trials} years: ${average_simulated_loss:.2f}")
print(f"Minimum simulated year: ${min(results)}")
print(f"Maximum simulated year: ${max(results)}")
