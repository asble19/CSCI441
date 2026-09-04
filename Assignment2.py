import sympy as sp

# STEP A: Ask the user for the number of variables/symbols

print("Expression 1")
num_vars1 = int(input("Enter the number of variables/symbols: "))

# STEP B: Ask the user to enter the mathematical expression

print("\nEnter Expression 1 using Python/SymPy format.")
print("\nExample: ")
print("2x^3y^2 - e^z y^4z + z^4 + 3yz becomes:")
print("2*x**3*y**2 - exp(z)*y**4*z + z**4 + 3*y*z") # x**3 is x^3 and exp(z) is e^z

expression1 = input("Enter the expression: ")

# Create the symbols for Expression 1
x, y, z = sp.symbols('x y z')

# Convert the user's expression into a SymPy expression
F = sp.sympify(expression1)

# STEP Ci: Program asks for the number of variables for Expression 2

print("\nExpression 2")
num_vars2 = int(input("Enter the number of variables/symbols: "))

# STEP Cii: Program asks for the mathematical expression for Expression 2

print("\nEnter Expression 2 using Python/SymPy format.")
print("\nExample: ")
print("2a^2b + b^3 - 3c^2d^4 - 5a^3c becomes:")
print("2*a**2*b + b**3 - 3*c**2*d**4 - 5*a**3*c")

expression2 = input("Enter the expression: ")

# Create the symbols for Expression 2
a, b, c, d = sp.symbols('a b c d')

# Convert the user's expression into a SymPy expression
W = sp.sympify(expression2)

# STEP Ciii: Compute and display the partial derivatives for both expressions
print("\n\nPARTIAL DERIVATIVES OF EXPRESSION 1\n")

print("F =", F)

print("∂F/∂x =", sp.diff(F, x))
print("∂F/∂y =", sp.diff(F, y))
print("∂F/∂z =", sp.diff(F, z))

print("\n\nPARTIAL DERIVATIVES OF EXPRESSION 2\n")

print("W =", W)

print("∂W/∂a =", sp.diff(W, a))
print("∂W/∂b =", sp.diff(W, b))
print("∂W/∂c =", sp.diff(W, c))
print("∂W/∂d =", sp.diff(W, d))

# STEP D: Submit this Python file/notebook lol