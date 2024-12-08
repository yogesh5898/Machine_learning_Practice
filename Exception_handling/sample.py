# a=b # NameError: name 'b' is not defined

# try:
#     a = b
# except:
#     print('The b is not defined')

# try:
#     a=b
# except NameError as ex:
#     print(ex)

try:
    a=5+6
    b=a/0
    d=b+a
    print(d)
except NameError as ex:
    print(ex,'da venna..!!')
except Exception as ex:
    print(ex)