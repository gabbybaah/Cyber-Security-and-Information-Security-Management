av = 1500
aro_initial = 6
ale_initial = av * aro_initial
mdm_cost = 200 * 10
aro_mitigated = 1
ale_mitigated = av * aro_mitigated
total_mitigated_cost = ale_mitigated + mdm_cost
savings = ale_initial - total_mitigated_cost
print(f"Initial ALE: ${ale_initial}")
print(f"MDM Implementation Cost: ${mdm_cost}")
print(f"Mitigated ALE (including MDM cost): ${total_mitigated_cost}")
print(f"Total Annual Financial Benefit: ${savings}")
