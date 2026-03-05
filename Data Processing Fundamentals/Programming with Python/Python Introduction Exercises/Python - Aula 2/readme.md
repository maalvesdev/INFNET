# User Input and Basic Text Analysis - **Date:** 05/03/2026

### Topics Covered

- User interaction with `input()`
- Type conversion using `int()`
- Formatted output using f-strings
- String length calculation with `len()`
- Counting characters in a string using `count()`

---

### Example: Converting Seconds to Minutes

This exercise converts a number of seconds into minutes and seconds using integer division and modulo.

```python
seconds = int(input("Enter the number of seconds: "))
print(f"{seconds//60} Minutes and {seconds%60} Seconds")
```

###Example: Counting Characters in a Sentence

This exercise counts the total number of characters and the occurrences of the letter "a".

```python
sentence = input("Enter a sentence: ")

total_characters = len(sentence)
count_upper_a = sentence.count("A")
count_lower_a = sentence.count("a")

print(f"Total characters: {total_characters}")
print(f"Uppercase A: {count_upper_a}")
print(f"Lowercase a: {count_lower_a}")
```
