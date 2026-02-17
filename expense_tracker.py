# expense_track.py
# Jaycob & Muneeb

from os import system

# prompts user for yes or no input and returns value based on input using string comparison.
def prompt(msg):
    choice = input(msg).lower()

    if choice in {'y', 'yes', 'Y'}:
        return True
    else:
        return False
    
# classes
class User:
    def __init__(self):
        # data
        self.profiles = {}

        # state
        self.current = self
        self.mode = 1

    def switch(self, name):
        if not name in self.profiles:
            return 'NO PROFILE FOUND.'
        
        self.current = self.profiles[name]
        self.mode = 2

        return 'SWITCH TO x PROFILE.'

    def new(self, name):
        if name in self.profiles:
            return 'PROFILE CALLED x FOUND'
        
        self.profiles[name] = UserProfile(self, name)

        return 'CREATED PROFILE x.'
    
    def view(self):
        for key, value in self.profiles.items():
            print(f'PROFILE: {key}')

        return f'ALL PROFILES PRINTED'
    
    def help(self, ctx=None):
        meta = {
            'new': 'CREATE A NEW PROFILE, `new [context]`',
            'switch': 'SWITCHES PROFILES, `switch [context]`',

            'view': 'VIEWS CURRENT PROFILES, `view`',

            'help': 'PRINT DIRECTORY FOR A SPECIFIC COMMAND, `help [ctx]`',
        }

        if ctx in meta:
            return f'{ctx}: {meta[ctx]}'
        elif ctx:
            return f'NO COMMAND CALLED {ctx} FOUND...'

        for cmd, text in meta.items():
            print(f'{cmd}: {text}')

        return f'ALL COMMANDS PRINTED.'

class UserProfile:
    def __init__(self, user, name):
        self.user = user
        self.name = name

        self.expenses = {}
        self.category = {}

    # creates, add, and categorizes expenses. if no category is passed than it'll default to no category...
    def add(self, ctx, amt, category=None):
        if not str.isdigit(amt):
            return f'AMOUNT IS NOT A NUMBER'
        
        amt = float(amt)
        expenses = self.expenses
        
        if category != None:
            categories = self.category

            if not category in categories:
                categories[category] = []
            
            list.append(categories[category], ctx)
        
        if not ctx in expenses:
            expenses[ctx] = amt

            return f'CREATED EXPENSE `{ctx}` and SET VALUE TO ${amt}'

        expenses[ctx] += amt
        
        return f'ADDED ${amt} to EXPENSE `{ctx}`'
    

    def back(self):
        self.user.current = self.user
        self.user.mode = 1

        system('clear')

        return 'RETURNED TO USERMODE'

    def view(self, ctx):
        expenses = self.expenses

        if ctx in expenses:
            return f'EXPENSE `{ctx}` IS AT ${expenses[ctx]}'

        return f'NO EXPENSE NAMED `{ctx}` FOUND...'

    def viewCategory(self, ctx):
        categories, expenses = self.category, self.expenses

        if ctx in categories:
            for index, exp in enumerate(categories[ctx]):
                total = expenses[exp]

                print(f'{index}. EXPENSE: {exp} and total is ${total}')

            return f'CATEGORY {ctx} SHOWN...'

        return f'NO CATEGORY NAMED {ctx} FOUND'

    def sum(self, ctx):
        categories, expenses = self.category, self.expenses

        if ctx in categories:
            total = 0

            for expense in categories[ctx]:
                if not expense in expenses:
                    continue

                value = expenses[expense]
                total += value

            return f'CATEGORY `{ctx}` IS ${total}'
            
        return f'NO CATEGORY FOUND `{ctx}`'

    def remove(self, ctx):
        categories, expenses = self.category, self.expenses
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

    def help(self, ctx=None):
        meta = {
            'add': 'CREATE OR ADD TO AN EXPENSE, `add [context] [value] [*category]`. Category is optional.',
            'view': 'VIEW A SPECIFIC EXPENSE, `view [context]`',
            'view_category': 'VIEW A CATEGORY AND IT`S RESPECTED EXPENSES, `view_category [context]`',
            'sum': 'PRINT SUM OF A CATEGORY, `sum [ctx]`',
            'remove': 'REMOVE A CATEGORY (AND DELETE ALL EXPENSES WITHIN CATEGORY) OR A SPECIFIC CATEGORY, `remove [ctx]`',
            'help': 'PRINT DIRECTORY FOR A SPECIFIC COMMAND, `help [ctx]`',
            'back': 'EXITS CURRENT PROFILE, `back`'
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

    user = User()

    COMMANDS = {
        1: {
            'switch': [ User.switch, 1, False ],
            'new': [ User.new, 1, False ],

            'view': [ User.view, 0, False],

            'help': [ User.help, 0, True ]
        },
        
        2: {
            'add': [ UserProfile.add, 2, True ],
            'view': [ UserProfile.view, 1, False ],
            'view_category': [ UserProfile.viewCategory, 1, False ],
            'sum': [ UserProfile.sum, 1, False ],
            'remove': [ UserProfile.remove, 1, False ],

            'back': [ UserProfile.back, 0, False ],

            'help': [ UserProfile.help, 0, True ]         
        }
    }

    def parse(cmd):
        commands = COMMANDS[user.mode]

        parsed = cmd.split(' ', 3)
        cmd = list.pop(parsed, 0)

        if cmd in commands:
            argLen = len(parsed)
            callback, argC, optArg = commands[cmd]

            if argLen >= argC:
                args = []

                for i in range(argC):
                    list.append(args, parsed[i])
            
                if optArg and argLen >= (argC + 1): # find better way todo this, terrible way of implementing optional arguments
                    list.append(args, parsed[argLen - 1])

                return callback(user.current, *args)
            else:
                return 'NOT ENOUGH ARGUMENTS'
        else:
            return 'NO COMMAND FOUND'

    print('EXPENSE TRACKER\n')

    while True:

        if user.mode == 1:
            print('USER MODE')
        elif user.mode == 2:
            print('PROFILE MODE')
            print(f'CURRENT: {user.current.name}')

        cmd = input('`help` for list of all commands; `exit` to exit.\n> ')

        if cmd == 'exit':
            break
        else:
            result = parse(cmd)

            print(f'{result}\n')

init()
