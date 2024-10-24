calls = 0

def count_calls ():
    def string_info (a = 'Capybara', b = 'Armageddon', c = str (0)):
        global calls
        calls +=1
        if a == 'Capybara':
            return ( str (len (a)), a.upper (), a.lower ())
        elif b == 'Armageddon':
            return ( str (len (b)), b.upper (), b.lower ())
    def is_contains (a = 'Urban', b = ('ban', 'BaNaN', 'urBAN')):
        global calls
        calls += 1
        if a == 'Urban' and b == ('ban', 'BaNaN', 'urBAN'):
            return (True)
        else :
            return (False)
    print (string_info ('Capybara'))
    print (string_info ('Armageddon'))
    print (is_contains ('Urban', ('ban', 'BaNaN', 'urBAN')))
    print (is_contains ('cycle', ('recycling', 'cyclic')))
    print (calls)
count_calls ()
