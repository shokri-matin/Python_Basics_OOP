# Modules refer to a file containing Python statements and definitions.

# A file containing Python code, for e.g.: example.py, is called a module and its module name would be example.

# We use modules to break down large programs into small manageable and organized files.
# Furthermore, modules provide reusability of code.

import TaxModule as tax

mylst = [100, 200, 300, 400]
for m in mylst:
    print(tax.tax(m, .1))

