# Python Decorators - Study Notes

This repository contains my notes and practice code while learning **Python Decorators** as part of my Python learning journey.

> **Note**
> This project is intended for educational purposes. The files are primarily study notes, small experiments, and practice examples rather than a production-ready application.

---

## 📚 Topics Covered

Today's lesson focuses on understanding how decorators work in Python, including:

- Functions as first-class objects
- Passing functions as arguments
- Nested functions
- Returning functions
- Wrapper functions
- Creating custom decorators
- Measuring function execution time with `time.time()`

---

## 📂 Contents

```text
.
├── main.py        # Practice exercises
├── notes.py       # Learning examples and personal notes (if applicable)
└── README.md
```

---

## 🧠 Practice Exercise

The main exercise implements a custom decorator that measures how long a function takes to execute.

Example:

```python
@speed_calc_decorator
def fast_function():
    ...
```

The decorator:

1. Records the start time.
2. Executes the original function.
3. Records the end time.
4. Prints the execution time.

Example output:

```text
fast_function run speed: 0.34s
slow_function run speed: 2.96s
```

---

## 🎯 Learning Objectives

By completing today's exercises, I learned:

- How Python decorators work behind the scenes.
- Why functions are considered first-class objects.
- How wrapper functions extend existing functionality.
- How decorators can execute code before and after another function.
- How to measure execution time using the `time` module.

---

## 📖 Notes

Most files in this repository are intended as **personal study notes**. Some examples are simplified to demonstrate specific Python concepts and may not represent production-ready code.

---

## 🚀 Course

Part of my journey through **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.