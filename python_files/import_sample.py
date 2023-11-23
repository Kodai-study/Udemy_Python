from package import *
import package.ignore_module
# from package import ignore_module

print("module1_string", module1.get_str())
print("module2_string", module2.get_str())
print(package.ignore_module.get_str())
