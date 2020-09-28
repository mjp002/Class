x = 50


def func(x):
    print('x is'), x
    x = 2
    print('Changed local x to'), x

func(x)
print('x is still'), x




x = 50

def func():
    global x

    print('x is'), x
    x=2
    print('Changed global x to'), x


func()
print('Value of x is'), x


def say(message, times=1):
    print (message * times)

say('Hello')
say('World', 5)


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)


def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
        for key in keywords:
            count += keywords[key]
        return count

print (total(10, 1, 2, 3, vegetables=50, fruits=100))


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return ('The numbers are equal')
    else:
        return y



print (maximum(2, 3))



import sys
print('The command line arguments are:')
for i in sys.argv:
    print (i)

print('\n\nThe PYTHONPATH is'), sys.path, '\n'


from math import sqrt
print("Square root of 16 is", sqrt(16))



if __name__ == '__main__':
    print('This program is being run by itself')

else:
    print('I am being imported from another module')



shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:')
for item in shoplist:
    print item

print ('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print ('I bought the', olditem)
print('My shopping list is now', shoplist)





zoo = ('pyhton', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print ('Number of cages in the new zoo is', len(new_zoo))
print ('All animals in new zoo are', new_zoo)
print ('Animals brought from old zoo are', new_zoo[2])
print ('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', \
    len(new_zoo)-1+len(new_zoo[2]))





ab = {  'Swaroop'   :   'swaroop@swaroopch.com',
        'Larry' :   'larry@wall.org',
        'Matsumoto' :   'matz@ruby-lang.org',
        'Spammer'   :   'spammer@hotmail.com'
        }

print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']

print(\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])







shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])


print('Item 1 ti 3 is', shoplist[1:3])
print('Item 2 ti end is', shoplist[2:])
print('Item 1 tio -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])




bri = set(['brazil', 'russia', 'india'])
'india' in bri 
'usa' in bri
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
bri & bric





print('Simple Assignment')
shoplist = ['apple', 'mango','carrot','banana']
mylist = shoplist

del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')

mylist = shoplist[:]

del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)





name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))




class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()



class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()







class Robot:
    """Represents a robot, with a name"""
population = 0

def __init__(self, name):
    """Initializes the data"""
    self.name = name
    print("(Initializing {})".format(self.name))

    Robot.population += 1

def die(self):
    """I am dying."""
    print("{} is being destroyed!".format(self.name))

    robot.population -= 1

    if Robot.population == 0:
        print("{} was the last one.".format(self.name))

    else:
        print("There are still {:d} robots working.".format(Robot.population))

def say_hi(self):
    """Greeting by the robot.
    Yeah, they can do that."""
    print("Greetings, my masters call me {}.".format(self.name))

@classmethod
def how_many(cls):
    """Prints the current population."""
    print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print ("\nRobots can do some work here.\n")
print ("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()






class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, se;f.age),)

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()



