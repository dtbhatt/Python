# print "Hello World!"


# x = "Hello Python"

# print x

# y=42

# print y

# print "read below for more on multi-line comments in python!"

# '''
# Triple quotations allow us to comment accross multiple lines as long as
# '''

# def say_hello(name):
#     if name:
#         print 'Hello' + name + 'from inside the function'
#     else:
#         print 'No name'

# print 'Outside of the function'

# name = "What"

# print "My name is", name
# print "My name is " + name


# first_name = "Zen"
# last_name = "Coder"
# print "My name is {} {}".format(first_name, last_name)

# hw= "hello %s" % "world"

# print hw


# string = "What the hell is this"

# print string.find("this")

# x = [1,2,3,4]

# x.append(99)
# print x

# x = [99, 4,2,5,-3]

# print x[:]

# print x[1:]

# print x[2:4]

# my_list = [1, 'zen', 'hi']
# print len(my_list)

# print map(*2, my_list)

# my_list = [1, 'Zen', 'hi']

# print (enumerate(my_list))
# for index, item in enumerate(my_list):
#     print index,item


# print sorted(my_list)

# print min(my_list)

# print list.index("hi")

# enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

dog = ("Canis Familiaris", "dog", "carnivore", 12)

# dog = dog + ('domestic',)


dog = dog[:2] + ("man's best friend",) + dog[3:]

print dog





