# 🌙 Ramadan Python Challenge — 30 Days of Practice

> A daily Python challenge for DevOps engineers who want to keep their coding sharp.  
> Ramadan 2026 Edition — One problem a day, every day.

---

## Week 1: Warm-Up & Foundations

### Day 1 — Reverse a Log Line
Take a log line like `"2026-02-28 ERROR server crashed"` and reverse the word order.  
**Bonus:** Parse it into a dict with keys `date`, `level`, `message`.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
reverse_log("2026-02-28 ERROR server crashed") ➞ "crashed server ERROR 2026-02-28"

reverse_log("2026-03-01 INFO deployment started") ➞ "started deployment INFO 2026-03-01"

reverse_log("2026-03-02 WARN disk space low") ➞ "low space disk WARN 2026-03-02"
```

**Bonus Examples**
```
parse_log("2026-02-28 ERROR server crashed") ➞ {"date": "2026-02-28", "level": "ERROR", "message": "server crashed"}

parse_log("2026-03-01 INFO deployment started") ➞ {"date": "2026-03-01", "level": "INFO", "message": "deployment started"}
```

### Day 2 — Count Unique IPs
Given a list of Apache/Nginx log lines, extract and count unique IP addresses.  
Return the top 5 most frequent IPs sorted by count.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
logs = [
    "192.168.1.1 - - [28/Feb/2026] GET /index.html",
    "10.0.0.5 - - [28/Feb/2026] POST /api/login",
    "192.168.1.1 - - [28/Feb/2026] GET /about.html",
    "10.0.0.5 - - [28/Feb/2026] GET /dashboard",
    "172.16.0.3 - - [28/Feb/2026] GET /index.html",
    "192.168.1.1 - - [28/Feb/2026] GET /contact"
]

count_ips(logs) ➞ [("192.168.1.1", 3), ("10.0.0.5", 2), ("172.16.0.3", 1)]

count_ips([]) ➞ []
```

### Day 3 — Flatten Nested Config
Write a function that flattens a nested dictionary (like a YAML config) into dot-notation keys.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
flatten({"server": {"host": "0.0.0.0", "port": 8080}}) ➞ {"server.host": "0.0.0.0", "server.port": 8080}

flatten({"db": {"primary": {"host": "db1", "port": 5432}}}) ➞ {"db.primary.host": "db1", "db.primary.port": 5432}

flatten({"name": "app"}) ➞ {"name": "app"}

flatten({}) ➞ {}
```

### Day 4 — Two Sum (Classic LeetCode #1)
Given a list of integers and a target, return indices of two numbers that add up to the target.  
Solve it in O(n) using a hash map.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
two_sum([2, 7, 11, 15], 9) ➞ [0, 1]

two_sum([3, 2, 4], 6) ➞ [1, 2]

two_sum([3, 3], 6) ➞ [0, 1]
```

### Day 5 — Validate Semantic Version
Write a function that checks if a string is a valid semver (`major.minor.patch`).  
**Bonus:** Compare two semver strings and return which is newer.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
is_valid_semver("1.0.0") ➞ True

is_valid_semver("2.11.3") ➞ True

is_valid_semver("1.0") ➞ False

is_valid_semver("abc.def.ghi") ➞ False

is_valid_semver("1.0.0.0") ➞ False
```

**Bonus Examples**
```
compare_semver("1.2.3", "1.2.4") ➞ "1.2.4"

compare_semver("2.0.0", "1.9.9") ➞ "2.0.0"

compare_semver("1.0.0", "1.0.0") ➞ "equal"
```

### Day 6 — Rotate an Array
Rotate a list `k` steps to the right. Do it in-place with O(1) extra space.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
rotate([1, 2, 3, 4, 5], 2) ➞ [4, 5, 1, 2, 3]

rotate([10, 20, 30, 40], 1) ➞ [40, 10, 20, 30]

rotate([1, 2, 3], 3) ➞ [1, 2, 3]

rotate([1, 2, 3], 5) ➞ [2, 3, 1]
```

### Day 7 — Parse Environment Variables
Given a `.env` file as a string, parse it into a dictionary. Handle comments (`#`), empty lines, and quoted values.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
env_str = """
DB_HOST=localhost
DB_PORT=5432
# This is a comment
API_KEY="secret-key-123"

DEBUG=true
"""

parse_env(env_str) ➞ {"DB_HOST": "localhost", "DB_PORT": "5432", "API_KEY": "secret-key-123", "DEBUG": "true"}

parse_env("NAME=app") ➞ {"NAME": "app"}

parse_env("# only comments") ➞ {}
```

---

## Week 2: Strings, Files & Automation

### Day 8 — Longest Common Prefix
Given a list of S3 bucket paths, find the longest common prefix.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
longest_prefix(["s3://bucket/logs/2026/", "s3://bucket/logs/2025/"]) ➞ "s3://bucket/logs/"

longest_prefix(["s3://data/raw/", "s3://data/processed/"]) ➞ "s3://data/"

longest_prefix(["flower", "flow", "flight"]) ➞ "fl"

longest_prefix(["abc", "xyz"]) ➞ ""

longest_prefix(["only_one"]) ➞ "only_one"
```

### Day 9 — YAML to JSON Converter
Write a script that reads a YAML file and outputs equivalent JSON. No libraries except `pyyaml` and `json`.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
yaml_str = "name: app\nport: 8080"
yaml_to_json(yaml_str) ➞ '{"name": "app", "port": 8080}'

yaml_str = "items:\n  - one\n  - two\n  - three"
yaml_to_json(yaml_str) ➞ '{"items": ["one", "two", "three"]}'

yaml_str = "debug: true"
yaml_to_json(yaml_str) ➞ '{"debug": true}'
```

### Day 10 — Find Duplicate Files
Given a directory path, find files with identical content (by hash). Return groups of duplicates.  
Use `hashlib` for hashing.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
# Assume these files exist with matching content:
# /tmp/a.txt contains "hello"
# /tmp/b.txt contains "hello"
# /tmp/c.txt contains "world"

find_duplicates("/tmp") ➞ [["/tmp/a.txt", "/tmp/b.txt"]]

# No duplicates
find_duplicates("/unique_files") ➞ []

# Multiple duplicate groups
find_duplicates("/logs") ➞ [["/logs/a.log", "/logs/b.log"], ["/logs/x.log", "/logs/y.log"]]
```

### Day 11 — Valid Parentheses (LeetCode #20)
Check if a string of brackets `()[]{}` is valid. Classic stack problem.  
**DevOps twist:** Validate nested Terraform/JSON bracket structures.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
is_valid("()") ➞ True

is_valid("()[]{}") ➞ True

is_valid("(]") ➞ False

is_valid("{[()]}") ➞ True

is_valid("([)]") ➞ False

is_valid("") ➞ True
```

### Day 12 — Tail a Log File
Implement a `tail -n` command in Python — read the last N lines of a file efficiently without loading the entire file into memory.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
# Assume /var/log/app.log has 1000 lines

tail("/var/log/app.log", 3) ➞ ["line 998", "line 999", "line 1000"]

tail("/var/log/app.log", 1) ➞ ["line 1000"]

tail("/var/log/app.log", 0) ➞ []
```

### Day 13 — Retry Decorator
Write a decorator `@retry(max_attempts=3, delay=1)` that retries a function on exception with exponential backoff.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
@retry(max_attempts=3, delay=1)
def fetch_data():
    raise ConnectionError("timeout")

fetch_data()
# Attempt 1: ConnectionError, waiting 1s...
# Attempt 2: ConnectionError, waiting 2s...
# Attempt 3: ConnectionError
# ➞ Raises ConnectionError after 3 attempts

@retry(max_attempts=3, delay=1)
def get_status():
    return 200

get_status() ➞ 200  # Succeeds on first try, no retries
```

### Day 14 — Merge Two Sorted Lists
Merge two sorted lists into one sorted list. Do it iteratively and recursively.  
Think of it as merging two sorted deployment queues.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
merge_sorted([1, 3, 5], [2, 4, 6]) ➞ [1, 2, 3, 4, 5, 6]

merge_sorted([1, 2, 3], []) ➞ [1, 2, 3]

merge_sorted([], [4, 5]) ➞ [4, 5]

merge_sorted([1, 1, 1], [1, 1]) ➞ [1, 1, 1, 1, 1]
```

---

## Week 3: Data Structures & DevOps Patterns

### Day 15 — LRU Cache (LeetCode #146)
Implement an LRU cache with `get` and `put` in O(1).  
**DevOps context:** Think of caching API responses or DNS lookups.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
cache = LRUCache(2)  # capacity = 2

cache.put(1, "ec2-instance") ➞ None
cache.put(2, "s3-bucket") ➞ None
cache.get(1) ➞ "ec2-instance"
cache.put(3, "lambda-fn")  # evicts key 2 (least recently used)
cache.get(2) ➞ -1  # not found
cache.get(3) ➞ "lambda-fn"
```

### Day 16 — CIDR Overlap Checker
Given two CIDR blocks (e.g., `10.0.0.0/16` and `10.0.1.0/24`), determine if they overlap.  
Use the `ipaddress` module.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
cidr_overlaps("10.0.0.0/16", "10.0.1.0/24") ➞ True

cidr_overlaps("192.168.1.0/24", "192.168.2.0/24") ➞ False

cidr_overlaps("10.0.0.0/8", "10.255.0.0/16") ➞ True

cidr_overlaps("172.16.0.0/12", "192.168.0.0/16") ➞ False
```

### Day 17 — Group Anagrams (LeetCode #49)
Group a list of strings into anagram clusters. Good hash map practice.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) ➞ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

group_anagrams([""]) ➞ [[""]]

group_anagrams(["a"]) ➞ [["a"]]

group_anagrams(["listen", "silent", "hello"]) ➞ [["listen", "silent"], ["hello"]]
```

### Day 18 — Cron Expression Parser
Parse a simple cron expression (`* * * * *`) and return a human-readable description.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
parse_cron("0 9 * * 1-5") ➞ "At 09:00 on every weekday"

parse_cron("*/15 * * * *") ➞ "Every 15 minutes"

parse_cron("0 0 * * *") ➞ "At 00:00 every day"

parse_cron("30 2 1 * *") ➞ "At 02:30 on day 1 of every month"

parse_cron("0 12 * * 0") ➞ "At 12:00 on Sunday"
```

### Day 19 — Binary Search on Sorted Logs
Given a sorted log file (by timestamp), use binary search to find the first log entry after a given timestamp.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
logs = [
    "2026-03-01T08:00:00 Server started",
    "2026-03-01T09:15:00 User login",
    "2026-03-01T10:30:00 Error occurred",
    "2026-03-01T11:45:00 Deployment done",
    "2026-03-01T14:00:00 Backup completed"
]

search_logs(logs, "2026-03-01T10:00:00") ➞ "2026-03-01T10:30:00 Error occurred"

search_logs(logs, "2026-03-01T12:00:00") ➞ "2026-03-01T14:00:00 Backup completed"

search_logs(logs, "2026-03-01T15:00:00") ➞ None  # No log after this time
```

### Day 20 — Health Check Aggregator
Write a function that takes a list of health check URLs, hits them concurrently using `asyncio`/`aiohttp` or `concurrent.futures`, and returns a summary (url, status_code, response_time).

Look at the examples below to get an idea of what the function should do.

**Examples**
```
urls = ["https://httpbin.org/status/200", "https://httpbin.org/status/500", "https://httpbin.org/delay/2"]

health_check(urls) ➞ [
    {"url": "https://httpbin.org/status/200", "status_code": 200, "response_time": 0.15},
    {"url": "https://httpbin.org/status/500", "status_code": 500, "response_time": 0.12},
    {"url": "https://httpbin.org/delay/2", "status_code": 200, "response_time": 2.03}
]

health_check([]) ➞ []
```

### Day 21 — Implement a Queue Using Two Stacks
Classic data structure problem. Implement a FIFO queue using only two stacks (lists with append/pop).

Look at the examples below to get an idea of what the function should do.

**Examples**
```
q = MyQueue()

q.push(1)
q.push(2)
q.push(3)
q.peek() ➞ 1
q.pop() ➞ 1
q.pop() ➞ 2
q.empty() ➞ False
q.pop() ➞ 3
q.empty() ➞ True
```

---

## Week 4: Graphs, Trees & Real-World DevOps

### Day 22 — Dependency Resolver (Topological Sort)
Given a dict of packages and their dependencies, return a valid installation order.  
Detect circular dependencies and raise an error.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
deps = {"app": ["flask", "redis"], "flask": ["jinja2"], "redis": [], "jinja2": []}
resolve(deps) ➞ ["jinja2", "flask", "redis", "app"]

deps = {"a": ["b"], "b": ["c"], "c": []}
resolve(deps) ➞ ["c", "b", "a"]

deps = {"a": ["b"], "b": ["a"]}
resolve(deps) ➞ raises CircularDependencyError
```

### Day 23 — Terraform State Diff
Given two JSON objects representing infrastructure state, produce a diff showing added, removed, and changed keys.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
old = {"instance_type": "t3.micro", "region": "us-east-1", "count": 2}
new = {"instance_type": "t3.medium", "region": "us-east-1", "count": 3, "tags": {"env": "prod"}}

state_diff(old, new) ➞ {
    "added": {"tags": {"env": "prod"}},
    "removed": {},
    "changed": {"instance_type": {"old": "t3.micro", "new": "t3.medium"}, "count": {"old": 2, "new": 3}}
}

state_diff({"a": 1}, {"a": 1}) ➞ {"added": {}, "removed": {}, "changed": {}}

state_diff({"a": 1, "b": 2}, {}) ➞ {"added": {}, "removed": {"a": 1, "b": 2}, "changed": {}}
```

### Day 24 — Sliding Window Maximum (LeetCode #239)
Find the max value in every window of size `k` in an array. Use a deque for O(n).

Look at the examples below to get an idea of what the function should do.

**Examples**
```
max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) ➞ [3, 3, 5, 5, 6, 7]

max_sliding_window([1], 1) ➞ [1]

max_sliding_window([9, 8, 7, 6, 5], 2) ➞ [9, 8, 7, 6]

max_sliding_window([1, 2, 3, 4, 5], 3) ➞ [3, 4, 5]
```

### Day 25 — AWS Tag Compliance Checker
Given a list of resources (dicts with a `tags` key), check which ones are missing required tags like `Environment`, `Owner`, `Team`.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
resources = [
    {"id": "i-001", "type": "ec2", "tags": {"Environment": "prod", "Owner": "devops", "Team": "platform"}},
    {"id": "i-002", "type": "ec2", "tags": {"Environment": "dev"}},
    {"id": "s3-003", "type": "s3", "tags": {}}
]
required = ["Environment", "Owner", "Team"]

check_compliance(resources, required) ➞ [
    {"id": "i-002", "type": "ec2", "missing_tags": ["Owner", "Team"]},
    {"id": "s3-003", "type": "s3", "missing_tags": ["Environment", "Owner", "Team"]}
]

check_compliance([{"id": "x", "type": "rds", "tags": {"Owner": "dba", "Team": "data", "Environment": "staging"}}], required) ➞ []
```

### Day 26 — Rate Limiter
Implement a token-bucket rate limiter class. It should support `allow_request()` that returns True/False.  
**DevOps context:** API gateway rate limiting.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
limiter = RateLimiter(capacity=3, refill_rate=1)  # 3 tokens max, 1 token/sec

limiter.allow_request() ➞ True   # 2 tokens left
limiter.allow_request() ➞ True   # 1 token left
limiter.allow_request() ➞ True   # 0 tokens left
limiter.allow_request() ➞ False  # no tokens!

# Wait 2 seconds...
time.sleep(2)
limiter.allow_request() ➞ True   # 2 tokens refilled, now 1 left
```

### Day 27 — Container Resource Calculator
Given a list of container specs `{"name": "app", "cpu": "250m", "memory": "512Mi"}`, calculate total CPU (in cores) and memory (in GiB) for a deployment.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
containers = [
    {"name": "app", "cpu": "250m", "memory": "512Mi"},
    {"name": "sidecar", "cpu": "100m", "memory": "256Mi"},
    {"name": "proxy", "cpu": "500m", "memory": "1Gi"}
]

calc_resources(containers) ➞ {"total_cpu_cores": 0.85, "total_memory_gib": 1.75}

calc_resources([{"name": "web", "cpu": "1000m", "memory": "2Gi"}]) ➞ {"total_cpu_cores": 1.0, "total_memory_gib": 2.0}

calc_resources([]) ➞ {"total_cpu_cores": 0.0, "total_memory_gib": 0.0}
```

### Day 28 — Word Ladder (LeetCode #127) — Lite Version
Given a start word and end word, find if you can transform one into the other by changing one letter at a time, using a given word list. BFS practice.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) ➞ 5
# hit → hot → dot → dog → cog

word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) ➞ 0
# "cog" is not in word list, no valid transformation

word_ladder("a", "c", ["a", "b", "c"]) ➞ 2
# a → c
```

---

## Final Days: Capstone Challenges

### Day 29 — Mini CI/CD Pipeline Simulator
Simulate a pipeline with stages: `build → test → deploy`.  
Each stage can pass or fail (random or configurable). Implement retries, logging, and a final status report.  
Use classes, decorators, and `logging`.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
pipeline = Pipeline(stages=["build", "test", "deploy"], max_retries=2)

pipeline.run() ➞ {
    "status": "SUCCESS",
    "stages": [
        {"name": "build", "status": "PASSED", "attempts": 1},
        {"name": "test", "status": "PASSED", "attempts": 2},
        {"name": "deploy", "status": "PASSED", "attempts": 1}
    ]
}

pipeline.run() ➞ {
    "status": "FAILED",
    "stages": [
        {"name": "build", "status": "PASSED", "attempts": 1},
        {"name": "test", "status": "FAILED", "attempts": 3},
        {"name": "deploy", "status": "SKIPPED", "attempts": 0}
    ]
}
```

### Day 30 — Infrastructure Cost Estimator
Build a CLI tool that takes a JSON/YAML file describing AWS resources and estimates monthly cost.
```yaml
resources:
  - type: ec2
    instance_type: t3.medium
    count: 3
  - type: s3
    storage_gb: 500
  - type: rds
    instance_type: db.t3.medium
    multi_az: true
```
Use a simple pricing dict. Add argument parsing with `argparse`.

Look at the examples below to get an idea of what the function should do.

**Examples**
```
resources = [
    {"type": "ec2", "instance_type": "t3.medium", "count": 3},
    {"type": "s3", "storage_gb": 500},
]

estimate_cost(resources) ➞ {
    "line_items": [
        {"type": "ec2", "description": "3x t3.medium", "monthly_cost": 90.72},
        {"type": "s3", "description": "500 GB storage", "monthly_cost": 11.50}
    ],
    "total_monthly": 102.22
}

estimate_cost([]) ➞ {"line_items": [], "total_monthly": 0.00}

# CLI usage:
# python cost_estimator.py --file infra.yaml
# Output:
# EC2:  3x t3.medium        $90.72/mo
# S3:   500 GB storage       $11.50/mo
# ──────────────────────────────────
# Total:                    $102.22/mo
```

---

## Bonus Challenges (If You Finish Early!)

| # | Challenge | Concept |
|---|-----------|---------|
| B1 | Implement `kubectl get pods` output parser | String parsing, tabular data |
| B2 | Write a GitHub webhook handler (Flask) | REST APIs, webhooks |
| B3 | Build a simple Prometheus metrics exporter | HTTP server, metrics |
| B4 | SSH config file parser & generator | File I/O, data modeling |
| B5 | Implement a simple key-value store with TTL | Dicts, time, threading |

### B1 — kubectl Output Parser

Look at the examples below to get an idea of what the function should do.

**Examples**
```
output = """NAME          READY   STATUS    RESTARTS   AGE
nginx-abc     1/1     Running   0          2d
redis-xyz     1/1     Running   3          5d
crash-pod     0/1     Error     10         1h"""

parse_pods(output) ➞ [
    {"name": "nginx-abc", "ready": "1/1", "status": "Running", "restarts": 0, "age": "2d"},
    {"name": "redis-xyz", "ready": "1/1", "status": "Running", "restarts": 3, "age": "5d"},
    {"name": "crash-pod", "ready": "0/1", "status": "Error", "restarts": 10, "age": "1h"}
]
```

### B2 — GitHub Webhook Handler

**Examples**
```
# POST /webhook with payload:
payload = {"action": "opened", "pull_request": {"title": "Fix bug", "user": {"login": "dev1"}}}

handle_webhook(payload) ➞ {"message": "PR 'Fix bug' opened by dev1", "status": "processed"}

payload = {"action": "closed", "pull_request": {"title": "Add feature", "merged": True}}
handle_webhook(payload) ➞ {"message": "PR 'Add feature' merged", "status": "processed"}
```

### B3 — Prometheus Metrics Exporter

**Examples**
```
exporter = MetricsExporter()
exporter.inc("http_requests_total", labels={"method": "GET", "path": "/api"})
exporter.inc("http_requests_total", labels={"method": "GET", "path": "/api"})
exporter.set("cpu_usage_percent", 72.5)

exporter.export() ➞ """
# HELP http_requests_total Total HTTP requests
http_requests_total{method="GET",path="/api"} 2
# HELP cpu_usage_percent CPU usage percentage
cpu_usage_percent 72.5
"""
```

### B4 — SSH Config Parser & Generator

**Examples**
```
config_text = """
Host dev-server
    HostName 10.0.1.5
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/dev_key

Host prod-server
    HostName 10.0.2.10
    User ec2-user
    Port 2222
"""

parse_ssh_config(config_text) ➞ {
    "dev-server": {"HostName": "10.0.1.5", "User": "ubuntu", "Port": "22", "IdentityFile": "~/.ssh/dev_key"},
    "prod-server": {"HostName": "10.0.2.10", "User": "ec2-user", "Port": "2222"}
}

generate_ssh_config({"my-server": {"HostName": "1.2.3.4", "User": "admin"}}) ➞ """
Host my-server
    HostName 1.2.3.4
    User admin
"""
```

### B5 — Key-Value Store with TTL

**Examples**
```
store = KVStore()

store.set("token", "abc123", ttl=5)  # expires in 5 seconds
store.get("token") ➞ "abc123"

time.sleep(6)
store.get("token") ➞ None  # expired

store.set("name", "app")  # no TTL, never expires
store.get("name") ➞ "app"

store.delete("name") ➞ True
store.get("name") ➞ None
```

---

## Tips for Success

- **Consistency > Perfection** — Even 20 minutes a day counts.
- **Write tests** — Use `pytest` to verify your solutions.
- **Time yourself** — Try to solve each problem within 30-45 minutes.
- **Refactor** — After solving, rewrite for readability and efficiency.
- **Document** — Add docstrings and type hints to every function.

Ramadan Mubarak! May your code be bug-free and your deployments smooth. 🌙
