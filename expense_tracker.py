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
        remove = prompt('DO YOU WANT TO REMOVE THE CATEGORY AND IT`S EXPENSES (means deleting every expense in it too...) OR REMOVE THE CATEGORY ITSELF\n(Y/N): ')
        category = categories[ctx]

        if remove == True:    
            for expense in category:
                dict.pop(expenses, expense)

            list.clear(category)
            dict.pop(categories, ctx)

            return f'SUCESSFULLY REMOVED ALL EXPENSES AND CATEGORY {ctx}'
        else:
            list.clear(category)
            dict.pop(categories, ctx)

            return f'SUCESSFULLY REMOVED THE CATEGORY {ctx}'

    if ctx in expenses:
        dict.pop(expenses, ctx)

        return f'REMOVED EXPENSE {ctx}'

    return f'{ctx} NOT FOUND'

def help(ctx):
    meta = {
        'add': 'CREATE OR ADD TO AN EXPENSE, `add [context] [value] [*category]`. Category is optional.',
        'view': 'VIEW A CATEGORY OF EXPENSES OR SPECIFIC EXPENSE, `view [context]`',
        'sum': 'PRINT SUM OF A CATEGORY, `sum [ctx]`',
        'remove': 'REMOVE A CATEGORY (AND DELETE ALL EXPENSES WITHIN CATEGORY) OR A SPECIFIC CATEGORY, `remove [ctx]`',
        'help': 'PRINT DIRECTORY FOR A SPECIFIC COMMAND, `help [ctx]`'
    }

    try:
        return f'{ctx}: {meta[ctx]}'
    except:
        for cmd, text in meta.items():
            print(f'{cmd}: {text}')

        return f'NO COMMAND FOUND, PRINTING ALL INSTEAD.'

def parse(cmd):
    COMMANDS = {
        'add': [add, 2, True],
        'view': [view, 1, False],
        'sum': [sum, 1, False],
        'remove': [remove, 1, False],
        'help': [help, 1, False]
    }

    parsed = cmd.split(' ', 3)
    cmd = list.pop(parsed, 0)

    if cmd in COMMANDS:
        argLen = len(parsed)
        callback, argC, optArg = COMMANDS[cmd]

        if argLen >= argC:
            args = []

            for i in range(argC):
                list.append(args, parsed[i])
           
            if optArg and argLen >= 3: # find better way todo this, terrible way of implementing optional arguments
                list.append(args, parsed[2])

            return callback(*args)
        else:
            return 'NOT ENOUGH ARGUMENTS'
    else:
        return 'NO COMMAND FOUND'

def init():
    while True:
        cmd = input('What would you like to do?\n> ')

        if cmd == 'exit':
            break
        else:
            result = parse(cmd)

            print(f'\n{result}')

init()
