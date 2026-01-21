_profile = {
    'expenses': {},
    'category': {},
}

def prompt(msg):
    act = input(msg).lower()

    if act in {'y', 'yes', 'Y'}:
        return True
    else:
        return False

def add(ctx, amt, category=None):
    if amt.isdigit() != True:
        return f'AMOUNT IS NOT A NUMBER'

    expenses = _profile['expenses']

    if category != None:
        categories = _profile['category']

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

    if ctx in categories:
        total = 0

        for expense in categories[ctx]:
            value = expenses[expense]
            total += value

        return f'CATEGORY `{ctx}` IS ${total}'
        
    return f'NO CATEGORY FOUND `{ctx}`'

def remove(ctx):
    categories, expenses = _profile['category'], _profile['expenses']

    if ctx in categories:
        remove = prompt('ARE YOU SURE YOU WANT TO REMOVE THIS CATEGORY (means deleting every expense in it too...)')

        if remove == True:
            category = categories[ctx]

            for expense in category:
                dict.pop(expenses, expense)

            dict.clear(category)
            dict.pop(categories, ctx)

            return f'SUCESSFULLY REMOVED ALL EXPENSES AND CATEGORY {ctx}'
        else:
            return 'PROMPT FAILED'

    if ctx in expenses:
        dict.pop(expenses, ctx)

        return f'REMOVED EXPENSE {ctx}'

    return f'{ctx} NOT FOUND'

def help(ctx):
    meta = {
        'add': '',
        'view': '',
        'sum': '',
        'remove': '',
    }

def parse(cmd):
    COMMANDS = {
        'add': [add, 2],
        'view': [view, 1],
        'sum': [view, 1],
        'remove': [remove, 1],
        'help': [help, 1]
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
