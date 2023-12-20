katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print('The line is currently empty.')
    else:
        line = 'The line is currently:'
        for i in range(len(katz_deli)):
            line = line + ' ' + str(i+1) + '. ' + katz_deli[i]
        print(line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print('Welcome, ' + name + '. You are number ' + str(len(katz_deli)) + ' in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print('There is nobody waiting to be served!')
    else:
        print('Currently serving ' + katz_deli[0] + '.')
        katz_deli.pop(0)

