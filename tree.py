import json
import pickle

class Tree:

    def __init__(self, letter, children=None):
        self.letter = letter
        self.children = []
        if children is not None:
            for child in children:
                self.children.append(child)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def get_letters(children):
    output = []
    for child in children:
        output.append(child.letter)
    return output

def create_tree():
    with open("pruned_words.json", 'r') as f:
        word_list = json.load(f)
    root = Tree('')

    # word_list = ['anger', 'angry', 'awesome']
    for word in word_list:
        branch = root
        for letter in word:
            if letter not in get_letters(branch.children):
                branch.add_child(Tree(letter))
            branch = branch.children[get_letters(branch.children).index(letter)]
    pickle.dump( root, open( "tree.p", "wb" ) )
    print("Tree Created")
# from queue import Queue
#
# q = Queue()
# q.put((root,""))
# while not q.empty():
#     current, branch_word = q.get()
#
#     print(branch_word)
#
#     for i in current.children:
#         q.put((i, branch_word + i.letter))


# def check_word(w):
#     b = root
#     for i,l in enumerate(w):
#         if l not in get_letters(b.children):
#             return False
#         b = b.children[get_letters(b.children).index(l)]
#     return True


# print(check_word("anger"))
# print(check_word("awidnawiuohndoa"))
# print(check_word("awesome"))
