# expense_track.py
# Jaycob & Muneeb

from os import system

class UserProfile:
    def __init__(self):
        self.expenses = {}
        self.category = {}
    
# prompts user for yes or no input and returns value based on input using string comparison.
def prompt(msg):
    choice = input(msg).lower()

    if choice in {'y', 'yes', 'Y'}:
        return True
    else:
        return False

# creates, add, and categorizes expenses. if no category is passed than it'll default to no category...
def add(profile, ctx, amt, category=None):
    amt = float(amt)

    if not amt:
        return f'AMOUNT IS NOT A NUMBER'
    
    expenses = profile.expenses
    
    if category != None:
        categories = profile.category

        if not category in categories:
            categories[category] = []
        
        list.append(categories[category], ctx)
    
    if not ctx in expenses:
        expenses[ctx] = amt

        return f'CREATED EXPENSE `{ctx}` and SET VALUE TO ${amt}'

    expenses[ctx] += amt
    
    return f'ADDED ${amt} to EXPENSE `{ctx}`'

def view(profile, ctx):
    expenses = profile.expenses

    if ctx in expenses:
        return f'EXPENSE `{ctx}` IS AT ${expenses[ctx]}'

    return f'NO EXPENSE NAMED `{ctx}` FOUND...'

def viewCategory(profile, ctx):
    categories, expenses = profile.category, profile.expenses

    if ctx in categories:
        for index, exp in enumerate(categories[ctx]):
            total = expenses[exp]

            print(f'{index}. EXPENSE: {exp} and total is ${total}')

        return f'CATEGORY {ctx} SHOWN...'

    return f'NO CATEGORY NAMED {ctx} FOUND'

def sum(profile, ctx):
    categories, expenses = profile.category, profile.expenses

    if ctx in categories:
        total = 0

        for expense in categories[ctx]:
            if not expense in expenses:
                continue

            value = expenses[expense]
            total += value

        return f'CATEGORY `{ctx}` IS ${total}'
        
    return f'NO CATEGORY FOUND `{ctx}`'

def remove(profile, ctx):
    categories, expenses = profile.category, profile.expenses
    option = True

    if ctx in categories and ctx in expenses:
        option = prompt(f'FOUND TWO INSTANCES OF {ctx}, WOULD YOU LIKE TO REMOVE THE CATEGORY (Y for category) (N for expense)\n(Y/N): ')

    if option and ctx in categories:
        remove = prompt('DO YOU WANT TO REMOVE THE CATEGORY AND IT`S EXPENSES (means deleting every expense in it too...) OR REMOVE THE CATEGORY ITSELF\n(Y/N): ')
        category = categories[ctx]

        if remove == True:    
            for expense in category:
                if not expense in expenses:
                    continue

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

def help(ctx=None):
    meta = {
        'add': 'CREATE OR ADD TO AN EXPENSE, `add [context] [value] [*category]`. Category is optional.',
        'view': 'VIEW A SPECIFIC EXPENSE, `view [context]`',
        'view_category': 'VIEW A CATEGORY AND IT`S RESPECTED EXPENSES, `view_category [context]`',
        'sum': 'PRINT SUM OF A CATEGORY, `sum [ctx]`',
        'remove': 'REMOVE A CATEGORY (AND DELETE ALL EXPENSES WITHIN CATEGORY) OR A SPECIFIC CATEGORY, `remove [ctx]`',
        'help': 'PRINT DIRECTORY FOR A SPECIFIC COMMAND, `help [ctx]`'
    }

    if ctx in meta:
        return f'{ctx}: {meta[ctx]}'
    elif ctx:
        return f'NO COMMAND CALLED {ctx} FOUND...'

    for cmd, text in meta.items():
        print(f'{cmd}: {text}')

    return f'ALL COMMANDS PRINTED.'

def init():
    system('clear')

    profile = UserProfile()

    def parse(cmd):
        COMMANDS = {
            'add': [add, 2, True],
            'view': [view, 1, False],
            'view_category': [viewCategory, 1, False],
            'sum': [sum, 1, False],
            'remove': [remove, 1, False],
            'help': [help, 0, True]
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
            
                if optArg and argLen >= (argC + 1): # find better way todo this, terrible way of implementing optional arguments
                    list.append(args, parsed[argLen - 1])

                return callback(profile, *args)
            else:
                return 'NOT ENOUGH ARGUMENTS'
        else:
            return 'NO COMMAND FOUND'

    print('EXPENSE TRACKER\n')

    while True:
        cmd = input('`help` for list of all commands; `exit` to exit.\n> ')

        if cmd == 'exit':
            break
        else:
            result = parse(cmd)

            print(f'{result}\n')

init()
