# Moved on to .py files for easy search and merge!

# Muttable and immutable data types:
# (you can remember them as data you can or cannot change)
# Muttable: list, dictionary, byte array, numpy array & recarray
# Immutable: numbers (integer, float, boolean), string, tuple, unicode

# example: string
mystr = 'Hello'
print(mystr[3]) # will let you access the element of string
#mystr[3] = 'd' # but you cannot change it! i.e. immutable

# += operator is not self = self + something!
a = ['a','b','c']
b = a
a += 'd' # in-place operation, changing a but not redefining a, thus b is also changed
a = a + 'd' # redefining a, thus, b is NOT changed

# How to slice a python list or tuple with a variable?
c = [1,2]
# print(a[c]) # error!
c = slice(1,2) # slice is an object that is used for this purpose, works just like [start:end:stride]
print(a[c]) # now it works
# How about arbitrary slice? like [1,3,7]
# Answer = list comprehension...
print([a[i] for i in [0,2]])

# Queue and Stack
# Python also has queue and stack class, e.g.
q = Queue() # is a queue
