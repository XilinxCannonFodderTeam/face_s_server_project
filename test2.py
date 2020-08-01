import importlib
import os


path = "C:/Users/sl1729/Documents/Xilinx_summer_school_project/face_s_server_project/test.py"
path = os.path.relpath(path)
path = path[:-3]
print(path)
print(path.__contains__('\\'))
tmp = path.split('\\')
path = '.'+'/'.join(tmp[1:])
package = tmp[0]
print(path)
# print(path)
tmp = importlib.import_module(path,package)
tmp2 = importlib.import_module(path,package)
tmp3 = importlib.import_module(path,package)
print(tmp)
print(tmp2)
print(tmp3)
tmp.test()
# print(dir(tmp)[-1])
# print(tmp.test)



# def get_func_module(func):
#     a = str(help(func))
#     print("123",a)
#     a = a.splitlines()[0]
#     a = a.split()[-1]
#     # a = a[:-1]
#     return a

# @get_func_module
# def test3():
#     print(2)

# def test2():
#     print(3)