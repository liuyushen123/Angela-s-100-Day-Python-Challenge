import time

timer = ["[     ]", "[■    ]", "[■■   ]", "[■■■  ]", "[■■■■ ]", "[■■■■■]"]
for _ in timer:
    print(f"{_}\r", flush=True, end="")
    time.sleep(1)
print()
