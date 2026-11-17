import datetime
def check_access(source_ip, current_time):
    hour = current_time.hour
    business_hours = 8 <= hour < 18
    trusted_subnet = source_ip.startswith("10.50.")
    if business_hours and trusted_subnet:
        return "ACCESS GRANTED: within business hours and trusted subnet"
    reasons = []
    if not business_hours:
        reasons.append("outside business hours")
    if not trusted_subnet:
        reasons.append("untrusted source subnet")
    return f"ACCESS DENIED: {', '.join(reasons)}"

print("On-site workstation during shift:", check_access("10.50.2.14", datetime.datetime(2026,8,18,10,0)))
print("Remote laptop after hours:", check_access("203.0.113.9", datetime.datetime(2026,8,18,23,0)))
