import keyword
def list_python_keywords():
keywords = keyword.kwlist
print("Python Keywords:")
for kw in keywords:
print(kw)
if __name__ == "__main__":
list_python_keywords()