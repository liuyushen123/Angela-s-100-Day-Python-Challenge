# ============================================
# Question 1 — Simple Type
# ============================================

# Consider the snippet below. Which of the following is the correct output?
# -------------------------------------------------------
a = (1,)
print(type(a))
# -------------------------------------------------------

# Options:
# A. tuple
# B. int
# C. double
# D. float

# Correct Answer: A
print()


# ============================================
# Question 2 — Fooor!
# ============================================

# Consider the snippet below. Which of the following is the correct output?
# -------------------------------------------------------
for x in range(3):
    print(x, end=" ")
    x = 3
# -------------------------------------------------------
print()

# Options:
# A. 0, then an error is raised.
# B. Nothing is printed.
# C. 0, then the loop breaks.
# D. 0 1 2

# Correct Answer: D
print()


# ============================================
# Question 4 — Sorting the sorted!
# ============================================

# Observe the code snippet below. What is printed?
# -------------------------------------------------------
nums = [4, 1, 3, 2]
rev = reversed(nums)
print(sorted(rev) is sorted(rev))
# -------------------------------------------------------

# Options:
# A. True
# B. False

# Correct Answer: B
print()


# ============================================
# Question 5 — Integer Division!
# ============================================

# Observe the code snippet below. What is printed?
# -------------------------------------------------------
print(1 // -2)
# -------------------------------------------------------

# Options:
# A. 0
# B. 0.5
# C. -1
# D. -0.5

# Correct Answer: C
print()


# ============================================
# Question 6 — Give me a hint!
# ============================================

# Observe the code snippet below. What is printed?
# -------------------------------------------------------
def add_ints(a: int, b: int) -> int:
    return a + b

print(add_ints(1, 1))
print(add_ints((1,), (2, 3)))
print(add_ints("1", "23"))
print(add_ints(("1",), ("23",)))
# -------------------------------------------------------

# Correct Answer:
# 2
# (1, 2, 3)
# 123
# ('1', '23')
print()
