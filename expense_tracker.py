# expense_track.py
# Jaycob & Muneeb

"""
Simple CLI Expense Tracker

Features:
- Multiple user profiles
- Add / view / remove expenses
- Optional expense categories
- Category summation
- Two modes: User Mode and Profile Mode

Mode 1: User Mode (manage profiles)
Mode 2: Profile Mode (manage expenses inside a profile)
"""

from os import system


# -------------------------------------------------
# Utility Function
# -------------------------------------------------

def prompt(msg):
    """
    Prompts user for yes/no input.

    Returns:
        True  -> if input is 'y' or 'yes'
        False -> otherwise
    """
    choice = input(msg).lower()

    if choice in {'y', 'yes', 'Y'}:
        return True
    else:
        return False


# -------------------------------------------------
# User Class (Top-Level Controller)
# -------------------------------------------------

class User:
    """
    Represents the main application state.

    Attributes:
        profiles (dict): All created user profiles
        current: Current active object (User or UserProfile)
        mode (int): 1 = user mode, 2 = profile mode
    """

    def __init__(self):
        # Stores all profiles
        self.profiles = {}

        # Current active object
        self.current = self

        # Start in user mode
        self.mode = 1


    def switch(self, name):
        """
        Switch to an existing profile.
        """
        if not name in self.profiles:
            return 'NO PROFILE FOUND.'
        
        self.current = self.profiles[name]
        self.mode = 2

        return 'SWITCH TO x PROFILE.'


    def new(self, name):
        """
        Create a new profile.
        """
        if name in self.profiles:
            return 'PROFILE CALLED x FOUND'
        
        self.profiles[name] = UserProfile(self, name)

        return 'CREATED PROFILE x.'


    def view(self):
        """
        Print all available profiles.
        """
        for key, value in self.profiles.items():
            print(f'PROFILE: {key}')

        return f'ALL PROFILES PRINTED'


    def help(self, ctx=None):
        """
        Displays available commands in user mode.
        """
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


# -------------------------------------------------
# UserProfile Class (Expense Management)
# -------------------------------------------------

class UserProfile:
    """
    Represents a single profile.

    Stores:
        expenses (dict): {expense_name: amount}
        category (dict): {category_name: [expense_names]}
    """

    def __init__(self, user, name):
        self.user = user
        self.name = name

        self.expenses = {}
        self.category = {}


    def add(self, ctx, amt, category=None):
        """
        Add or update an expense.

        Args:
            ctx (str): Expense name
            amt (str): Amount (must be numeric)
            category (str, optional): Category name
        """

        if not str.isdigit(amt):
            return f'AMOUNT IS NOT A NUMBER'
        
        amt = float(amt)
        expenses = self.expenses
        
        # If category is provided, assign expense to category
        if category != None:
            categories = self.category

            if not category in categories:
                categories[category] = []
            
            list.append(categories[category], ctx)
        
        # Create new expense
        if not ctx in expenses:
            expenses[ctx] = amt
            return f'CREATED EXPENSE `{ctx}` and SET VALUE TO ${amt}'

        # Add to existing expense
        expenses[ctx] += amt
        
        return f'ADDED ${amt} to EXPENSE `{ctx}`'
    

    def back(self):
        """
        Return to user mode.
        """
        self.user.current = self.user
        self.user.mode = 1

        system('clear')

        return 'RETURNED TO USERMODE'


    def view(self, ctx):
        """
        View a specific expense.
        """
        expenses = self.expenses

        if ctx in expenses:
            return f'EXPENSE `{ctx}` IS AT ${expenses[ctx]}'

        return f'NO EXPENSE NAMED `{ctx}` FOUND...'


    def viewCategory(self, ctx):
        """
        View all expenses inside a category.
        """
        categories, expenses = self.category, self.expenses

        if ctx in categories:
            for index, exp in enumerate(categories[ctx]):
                total = expenses[exp]
                print(f'{index}. EXPENSE: {exp} and total is ${total}')

            return f'CATEGORY {ctx} SHOWN...'

        return f'NO CATEGORY NAMED {ctx} FOUND'


    def sum(self, ctx):
        """
        Calculate total value of a category.
        """
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
        """
        Remove an expense or category.

        If category:
            - Option to delete only category
            - Or delete category and all its expenses
        """

        categories, expenses = self.category, self.expenses
        option = True

        # If name matches both expense and category
        if ctx in categories and ctx in expenses:
            option = prompt(
                f'FOUND TWO INSTANCES OF {ctx}, WOULD YOU LIKE TO REMOVE THE CATEGORY (Y for category) (N for expense)\n(Y/N): '
            )

        # Remove category
        if option and ctx in categories:
            remove = prompt(
                'DO YOU WANT TO REMOVE THE CATEGORY AND IT`S EXPENSES (means deleting every expense in it too...) OR REMOVE THE CATEGORY ITSELF\n(Y/N): '
            )

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

        # Remove expense
        if ctx in expenses:
            dict.pop(expenses, ctx)
            return f'REMOVED EXPENSE {ctx}'

        return f'{ctx} NOT FOUND'


    def help(self, ctx=None):
        """
        Display help menu for profile mode.
        """
        meta = {
            'add': 'CREATE OR ADD TO AN EXPENSE, `add [context] [value] [*category]`. Category is optional.',
            'view': 'VIEW A SPECIFIC EXPENSE, `view [context]`',
            'view_category': 'VIEW A CATEGORY AND IT`S RESPECTED EXPENSES, `view_category [context]`',
            'sum': 'PRINT SUM OF A CATEGORY, `sum [ctx]`',
            'remove': 'REMOVE A CATEGORY OR A SPECIFIC EXPENSE, `remove [ctx]`',
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


# -------------------------------------------------
# Application Entry Point
# -------------------------------------------------

def init():
    """
    Initializes program.
    Handles command parsing and main loop.
    """

    system('clear')

    user = User()

    # Command structure:
    # 'command': [function, required_arg_count, has_optional_arg]
    COMMANDS = {
        1: {
            'switch': [User.switch, 1, False],
            'new': [User.new, 1, False],
            'view': [User.view, 0, False],
            'help': [User.help, 0, True]
        },
        
        2: {
            'add': [UserProfile.add, 2, True],
            'view': [UserProfile.view, 1, False],
            'view_category': [UserProfile.viewCategory, 1, False],
            'sum': [UserProfile.sum, 1, False],
            'remove': [UserProfile.remove, 1, False],
            'back': [UserProfile.back, 0, False],
            'help': [UserProfile.help, 0, True]         
        }
    }


    def parse(cmd):
        """
        Parses user input and executes correct function.
        """

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
            
                # Basic optional argument handling
                if optArg and argLen >= (argC + 1):
                    list.append(args, parsed[argLen - 1])

                return callback(user.current, *args)
            else:
                return 'NOT ENOUGH ARGUMENTS'
        else:
            return 'NO COMMAND FOUND'


    print('EXPENSE TRACKER\n')

    # Main loop
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


# Start program
init()
