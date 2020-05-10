#zip and enumerate are useful buildin functions that comes in handy when dealing with looops
#___________________________________ZIP___________________________________________
# Zip returns an iterator that combines multiple iterators into one sequence of tuples each tuple contains the elements
# in that position from alll the iterables
L = list(zip(['a','b'],[1,2]))
print(L)
letters = ['a','b']
nums = [1,2]
for letter,num in zip(letters,nums):
    print("({},{})".format(letter,num))

# In addition to zippping 2-list together you can also unzip a list into tuples using an asterisk
some_list = [('a',1),('b',1)]
letters,nums = zip(*some_list)
print(letters,nums)