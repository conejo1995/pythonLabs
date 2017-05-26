
def make_list_of_strings (*args):
    for c in args:
        print(c, end = " ")
    print()


def flower_colors(**kwargs):

    print(kwargs)


make_list_of_strings('The','cat','in','the','hat')


flower_colors(roses = 'red', violets = 'blue', sunflower = 'yellow')
