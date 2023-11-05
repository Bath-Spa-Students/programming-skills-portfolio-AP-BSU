# Dictionary
Glossary = {
    "conditions'ifs, elif, else'": "A statement based on condition of true or false.",
    "function[]": "A reusable block of code that performs a specific task.",
    "dictionary": "A index of keywords like right now.",
    "Python": "Our programming language for its readability and simplicity.",
    "print": "to print a text or block of commands.",
}
for word, meaning in Glossary.items():
    print(f"{word}: {meaning}")

# To print dictionary and title
for word, meaning in Glossary.items():
    print(f"{word}:")
    print(meaning)
    print()