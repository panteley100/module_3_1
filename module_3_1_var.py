calls = 0

def count_calls ():
    global calls
    calls += 1
def string_info (a):
    global calls
    calls +=1
    return ( str (len (a)), a.upper (), a.lower ())
def is_contains (a = 'Urban', b = ('ban', 'BaNaN', 'urBAN')):
    global calls
    calls += 1
    if a == 'Urban' and b == ('ban', 'BaNaN', 'urBAN'):
        return (True)
    else :
        return (False)
print (string_info ('Capybara'))
print (string_info ('Armageddon'))
print(is_contains('Urban', ('ban', 'BaNaN', 'urBAN')))
print(is_contains('cycle', ('recycling', 'cyclic')))
print (calls)