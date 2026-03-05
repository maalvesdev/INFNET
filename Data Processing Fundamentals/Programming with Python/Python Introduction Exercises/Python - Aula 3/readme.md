# String Manipulation and Text Processing
**Date:** 05/03/2026

### Topics Covered

- Converting text to lowercase with `lower()`
- Counting occurrences using `count()`
- Checking if text exists using `in`
- Replacing text using `replace()`
- Converting text to title case with `title()`
- Getting string length with `len()`
- Splitting strings using `split()`
- Finding positions in text with `find()`
- String slicing
- String multiplication (`*`)

---

### Example: Checking if Text Exists (`in`)

The in operator checks if a word is present in a string.

```python
sentence = input("Enter a sentence: ").lower()
word = input("Enter a word: ").lower()

print(word in sentence)
```

### Example: Splitting Strings (`split()`)

Divides a string into parts based on a separator.

```python
email = input("Enter your email: ")

user, domain = email.split("@")

print(user)
print(domain)
```
