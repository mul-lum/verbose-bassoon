_profile = {
    'expenses': {},
    'category': {},
}

def getExpense(ctx):
    categories, expenses = _profile['category'], _profile['expenses']

    return expenses[ctx]

def add(ctx, amt, category=None):
    categories, expenses = _profile['category'], _profile['expenses']

    if category != None:
        if not category in categories:
            categories[category] = []
        
        list.append(categories[category], ctx)
    
    if not ctx in expenses:
        expenses[ctx] = amt

        return f'CREATED EXPENSE `{ctx}` and SET VALUE TO ${amt}'

    expenses[ctx] = amt
    
    return f'ADDED ${amt} to EXPENSE `{ctx}`'

def view(ctx):
    categories, expenses = _profile['category'], _profile['expenses']

    if ctx in expenses:
        total = expenses[ctx]

        return f'EXPENSE `{ctx}` IS AT ${total}'
    elif ctx in categories:
        for index, exp in enumerate(categories[ctx]):
            total = expenses[exp]

            print(f'{index}. EXPENSE: {exp} and total is ${total}')

        return f'CATEGORY {ctx} SHOWN...'

    return f'NO EXPENSE NAMED `{ctx}` FOUND...'

def sum(ctx):
    categories, expenses = _profile['category'], _profile['expenses']

    if ctx in expenses:
        return 

    return

def remove(ctx):
    return

def parse(cmd):
    COMMANDS = {
        'add': [add, 2],
        'view': [view, 1],
        'sum': [view, 1],
        'remove': [remove, 1],
    }

    parsed = cmd.split(' ', 3)
    cmd = list.pop(parsed, 0)

    if cmd in COMMANDS:
        callback, argC = COMMANDS[cmd]

        if len(parsed) >= argC:
            args = []
            
            for i in range(argC):
                list.append(args, parsed[i])

            return callback(*args)
        else:
            return 'NOT ENOUGH ARGUMENTS'
    else:
        return 'NO COMMAND FOUND'

def init():
    while True:
        cmd = input('What would you like to do?')

        if cmd == 'exit':
            break
        else:
            final = parse(cmd)

            print(final)

init()
