from math import cosh

# constants
MAX_SERIES = 500

# strings for ASCII art
series_ASCII = """
Function 'cosh(h)' Taylor series:

          500
        _______
        \          2k
         \        x
cosh(x) = >    ---------
         /       (2k)!
        /______
         k = 0
"""


function_definition_region = "Function 'cosh(x)' definition region: -inf < x < +inf"


recurrence_ASCII = """
                                2
                               x
recurrence multiplier = ---------------
                          2k*(2k - 1)
"""


# calculation of 'cosh(x)' Taylor series till 500th
def my_cosh(x):
	
	print("Calculating 'cosh(%.10f)' till %dth Taylor series element"%(x,MAX_SERIES))
	k = 0
	a = 1.0
	S = a

	while k <= MAX_SERIES:
		k = k + 1
		R = x**2/( (2*k)*(2*k - 1) )
		a = a*R
		S = S + a
		if k == (MAX_SERIES - 1):
			print("a%d = %.10f\tS%d = %.10f"%(k,a,k,S))
		if k == (MAX_SERIES - 0):
			print("a%d = %.10f\tS%d = %.10f"%(k,a,k,S))


	return S
# my_cosh end

# print in ASCII 'y = cosh(x)' Taylor series
print(series_ASCII)

# print in ASCII function definition region
print(function_definition_region)

# print in ASCII recurrence multiplier
print(recurrence_ASCII)

# get 'x' value from user input
x = float(input("Please, enter argument value (x): "))

# calculate 'cosh(x)' value using our created function
my_y = my_cosh(x)
print("cosh(%.10f) = %.10f\n"%(x,my_y))

# calculate 'cosh(x)' value using Python library function
print("Calculating 'cosh(%.10f)' value using Python library function"%(x))
y = cosh(x)
print("cosh(%.10f) = %.10f"%(x,y))
