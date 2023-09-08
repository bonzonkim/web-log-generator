import random
import time
import ipaddress


def generate_random_ip():
    return str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

num_entries = 200000

http_methods = ["GET", "POST", "PUT", "DELETE"]
paths = ["/api/v1/orders", "/api/v1/products", "/api/v1/users"]
statuses = ["200 OK", "404 Not Found", "500 Internal Server Error"]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5000.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.5000.0 Safari/537.36",
]
referrers = ["https://example.com", "https://example.com/account", "https://example.com/products"]
user_ids = ["12345", "67890", "54321"]
session_ids = ["ABCDEFG12345", "XYZ1234567890", "12345ABCDEFG"]

def generate_log_entry():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + " UTC"
    ip_address = generate_random_ip() 
    http_method = random.choice(http_methods)
    path = random.choice(paths) + f"?id={random.randint(1, 10000)}&status={random.choice(statuses).split()[0].lower()}"
    status = random.choice(statuses)
    user_agent = random.choice(user_agents)
    referer = random.choice(referrers)
    x_forwarded_for = f"{random.choice(ip_address)}, {random.choice(ip_address)}"
    bytes_sent = random.randint(1000, 1000000)
    duration = f"{random.randint(1, 500)}ms"
    cache_control = "no-cache"
    rate_limit_limit = random.randint(50, 200)
    rate_limit_remaining = random.randint(0, rate_limit_limit)
    rate_limit_reset = 3600
    user_id = random.choice(user_ids)
    session_id = random.choice(session_ids)
    request_id = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(12))
    
    log_entry = (
        f"{timestamp} | {ip_address} | {http_method} {path} | {status} | {user_agent} | "
        f"User-Agent: {user_agent} | Referer: {referer} | X-Forwarded-For: {x_forwarded_for} | "
        f"Bytes-Sent: {bytes_sent} | Duration: {duration} | Cache-Control: {cache_control} | "
        f"X-Rate-Limit-Limit: {rate_limit_limit} | X-Rate-Limit-Remaining: {rate_limit_remaining} | "
        f"X-Rate-Limit-Reset: {rate_limit_reset} | User-Id: {user_id} | Session-Id: {session_id} | "
        f"Request-Id: {request_id}\n"
    )
    
    return log_entry


with open("generated_web_logs.log", "w") as file:
    for _ in range(num_entries):
       log_entry = generate_log_entry()
       file.write(log_entry)
