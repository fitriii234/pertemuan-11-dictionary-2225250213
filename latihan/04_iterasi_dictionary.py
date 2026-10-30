data = {"nama": "Ayu", "nilai": 85, "kelas": "A"}

print("Keys:")
for key in data:
    print(key)

print("\nValues:")
for value in data.values():
    print(value)

print("\nItems:")
for key, value in data.items():
    print(f"{key}: {value}")
