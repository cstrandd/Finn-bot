app = "finn-bot"
primary_region = "arn"

[processes]
app = "python loop_runner.py"

[[vm]]
cpu_kind = "shared"
cpus = 1
memory = "1gb"

