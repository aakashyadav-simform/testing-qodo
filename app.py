import os

def add(x,y):
    return x + y

if __name__ == "__main__":
    a = int(os.getenv("A", "0"))
    b = int(os.getenv("B", "0"))
    result = add(a, b)
    print(f"This is the result: {result}")

