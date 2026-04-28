# ------------------------------------------
# Global and Local Scope Demonstration
# ------------------------------------------

# Example 1: Reading a global variable (works)
player_health = 5

def read_health():
    # Reading global variable is allowed
    print("Example 1 - Reading global:", player_health)

read_health()
print("-" * 50)


# Example 2: Updating global variable without 'global' (fails)
player_health = 5

def update_health_fail():
    # This line acts like: player_health = player_health * 5
    # That is an assignment → Python treats player_health as LOCAL
    # But it tries to read it first → ERROR
    try:
        player_health *= 5
        print("Example 2:", player_health)
    except Exception as e:
        print("Example 2 - Updating global without global keyword → ERROR:", e)

update_health_fail()
print("-" * 50)


# Example 3: Updating global variable correctly using 'global' (works)
player_health = 5

def update_health_global():
    global player_health  # explicitly using global variable
    player_health *= 5
    print("Example 3 - Updated with global keyword:", player_health)

update_health_global()
print("Global after update:", player_health)
print("-" * 50)


# Example 4: Mutating a global LIST (works without global)
player_health = [5]

def mutate_list():
    # This does NOT reassign; it mutates the object
    player_health.append(10)
    print("Example 4 - Mutated global list:", player_health)

mutate_list()
print("Global list after mutation:", player_health)
print("-" * 50)


# Example 5: Reassigning inside function creates a LOCAL variable (works, but does not change global)
player_health = [5]

def reassign_list():
    # This creates a local variable, does NOT change the global list
    player_health = "string"
    print("Example 5 - Local reassignment:", player_health)

reassign_list()
print("Example 5 - Global remains unchanged:", player_health)
print("-" * 50)


# ------------------------------------------
# SUMMARY FOR LEARNING
# ------------------------------------------

# SUMMARY OF PYTHON SCOPE RULES:
# ------------------------------

# 1. Reading a global variable inside a function → OK
# 2. Reassigning a global variable inside a function → ERROR unless you use 'global'
# 3. Mutating a global object (list / dict / set) inside a function → OK
# 4. Reassigning a variable name inside a function → Creates a LOCAL variable
# 5. 'global' keyword is required if you want to change which object the global name points to.

# This file includes working and failing examples to demonstrate all behaviors.

