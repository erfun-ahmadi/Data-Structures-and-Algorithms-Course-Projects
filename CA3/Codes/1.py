import sys
import functools

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)
      
    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)
    
    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)
    return wrapper

def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))
    return wrapper

class MainEmu():
    def __init__(self):
        self.items = dict()

    def start_program(self):
        for line in sys.stdin:
            line = Utils.delete_end_char(line)
            action, line = Utils.parse_line(line)
            actionPointer = Utils.get_attribute_pointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = Utils.parse_line(line)
        itemName, line = Utils.parse_line(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = Utils.parse_line(line, '.')
        funcName, line = Utils.parse_line(line, '(')
        argsLine, line = Utils.parse_line(line, ')')
        args = Utils.get_args(argsLine)
        attribute = Utils.get_attribute_pointer(self.items[itemName],
                                                   funcName)

        Utils.run_function(attribute, args)

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class MinHeap:
    def __init__(self):
        self.min_heap = list()
    
    class Node:
        pass
        
    def bubble_up(self, index):
        if type(index) != int:
            raise Exception("invalid index")
        elif index < 0 or index >= len(self.min_heap):
            raise Exception("out of range index")
        else:
            if index <= 0:
                return
            if self.min_heap[index] < self.min_heap[int((index-1)/2)]:
                self.min_heap[index], self.min_heap[int((index-1)/2)] = self.min_heap[int((index-1)/2)], self.min_heap[index]
                self.bubble_up(int((index-1)/2))
            else:
                return
            
    def bubble_down(self, index):
        if type(index) != int:
            raise Exception("invalid index")
        elif len(self.min_heap) == 0:
            return
        elif index < 0 or index >= len(self.min_heap):
            raise Exception("out of range index")
        else:
            if 2*index+2 < len(self.min_heap):
                find_min = min([self.min_heap[index], self.min_heap[2*index+1], self.min_heap[2*index+2]])
                if self.min_heap[index] == find_min:
                    return
                else:
                    if find_min == self.min_heap[2*index+1]:
                        self.min_heap[index], self.min_heap[2*index+1] = self.min_heap[2*index+1], self.min_heap[index]
                        self.bubble_down(2*index+1)
                    else:
                        self.min_heap[index], self.min_heap[2*index+2] = self.min_heap[2*index+2], self.min_heap[index]
                        self.bubble_down(2*index+2)
            elif 2*index+1 == len(self.min_heap)-1:
                if self.min_heap[index] > self.min_heap[2*index+1]:
                    self.min_heap[index], self.min_heap[2*index+1] = self.min_heap[2*index+1], self.min_heap[index]
                    self.bubble_down(2*index+1)
                else:
                    return
            elif 2*index+1 > len(self.min_heap)-1:
                return
    
    def print1(self):
        print(self.min_heap)    
    
    def heap_push(self, value):
        self.min_heap.append(value)
        self.bubble_up(len(self.min_heap)-1)
        
    def heap_pop(self):
        if len(self.min_heap) > 0:
            print(self.min_heap[0])
            self.min_heap[0] = self.min_heap[-1]
            self.min_heap.pop()
            self.bubble_down(0)
        else:
            raise Exception("empty")
    
    def find_min_child(self, index):
        if type(index) != int:
            raise Exception("invalid index")
        elif index >= 0 and index <= len(self.min_heap)-1:
            if 2*index+1 > len(self.min_heap)-1:
                raise Exception("out of range index")
            elif 2*index+1 == len(self.min_heap)-1:
                print(2*index+1)
            elif self.min_heap[2*index+1] <= self.min_heap[2*index+2]:
                print(2*index+1)
            else:
                print(2*index+2)
        elif index < 0 or index > len(self.min_heap)-1:
            raise Exception("out of range index")     
                    
    def heapify(self, *args):
        for i in args:
            self.min_heap.append(i)
            self.bubble_up(len(self.min_heap)-1)

class HuffmanTree:
    class Node:
        def __init__(self, letter, left, right):
            self.letter = letter
            self.left = left
            self.right = right
            
        def set_repetition(self, value):
            self.repetition = value
            
        def set_code(self, code):
            self.code = code
            
    def __init__(self):
        self.letters = list()
        self.head = None
        self.costs = list()

    @fix_str_arg    
    def set_letters(self,*args):
        for i in args:
            self.letters.append(self.Node(i, None, None))
               
    @fix_str_arg    
    def set_repetitions(self,*args):
        for i in range(len(args)):
            self.letters[i].set_repetition(args[i])
    
    def find_codes(self, node, value):
        if node.left == None:
            node.set_code(value)
            self.costs.append(len(value)*node.repetition)
            return
        self.find_codes(node.left, value+"0")
        self.find_codes(node.right, value+"1")  

    def build_huffman_tree(self):
        while len(self.letters) > 1:
            self.letters.sort(key = lambda x: x.repetition)
            new_node = self.Node("internal", self.letters[0], self.letters[1])
            new_node.set_repetition(self.letters[0].repetition + self.letters[1].repetition)
            self.letters.pop(0)
            self.letters.pop(0)
            self.letters.append(new_node)
        self.head = self.letters[0]
        self.find_codes(self.head.left, "0")
        self.find_codes(self.head.right, "1")

    def get_huffman_code_cost(self):
        print(sum(self.costs))

    @fix_str_arg
    def text_encoding(self, text):
        for i in set(text):
            self.letters.append(self.Node(i, None, None))
            self.letters[-1].set_repetition(text.count(i))
        self.build_huffman_tree()

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class RedBlackTree():
    def __init__(self):
        self.root = None
        
    class Node:
        def __init__(self, value, color, parent):
            self.value = value
            self.color = color
            self.parent = parent
            self.left = None
            self.right = None
            
        def change_color(self):
            if self.color == "RED":
                self.color = "BLACK"
            else:
                self.color = "RED"

    def fix_insert(self, node):
        if node.parent == None and node.color == "RED":
            node.change_color()
            return
        if node.parent == None or node.parent.color == "BLACK" :
            return       
        if node.parent.parent.left == node.parent:
            if node.parent.parent.right == None:
                if node == node.parent.right:
                    self.left_rotate(node.parent)
                    self.right_rotate(node.parent)
                    node.change_color()
                    node.right.change_color()
                    return
                elif node == node.parent.left:
                    self.right_rotate(node.parent.parent)
                    node.parent.change_color()
                    node.parent.right.change_color()
                    return
            elif node.parent.parent.right.color == "BLACK":
                if node == node.parent.right:
                    self.left_rotate(node.parent)
                    self.right_rotate(node.parent)
                    node.change_color()
                    node.right.change_color()
                    return
                elif node == node.parent.left:
                    self.right_rotate(node.parent.parent)
                    node.parent.change_color()
                    node.parent.right.change_color()
                    return
            elif node.parent.parent.right.color == "RED":
                node.parent.parent.change_color()
                node.parent.change_color()
                node.parent.parent.right.change_color()
                self.fix_insert(node.parent.parent)
        elif node.parent.parent.right == node.parent:
            if node.parent.parent.left == None:
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                    self.left_rotate(node.parent)
                    node.change_color()
                    node.left.change_color()
                    return
                elif node == node.parent.right:
                    self.left_rotate(node.parent.parent)
                    node.parent.change_color()
                    node.parent.left.change_color()
                    return
            elif node.parent.parent.left.color == "BLACK" :
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                    self.left_rotate(node.parent)
                    node.change_color()
                    node.left.change_color()
                    return
                elif node == node.parent.right:
                    self.left_rotate(node.parent.parent)
                    node.parent.change_color()
                    node.parent.left.change_color()
                    return
            elif node.parent.parent.left.color == "RED":
                node.parent.parent.change_color()
                node.parent.change_color()
                node.parent.parent.left.change_color()
                self.fix_insert(node.parent.parent)
        
    def find_node_color(self, value):
        if type(value) != int:
            raise Exception("invalid index")
        if self.root == None:
            raise Exception("empty")
        pointer = self.root
        while pointer != None:
            if pointer.value == value:
                print(pointer.color)
                return
            elif pointer.value < value:
                pointer = pointer.right
            elif pointer.value > value:
                pointer = pointer.left
        raise Exception("out of range index")

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left != None:
            new_root.left.parent = node
        new_root.left = node
        new_root.parent = node.parent
        if node != self.root:
            if node == node.parent.left:
                node.parent.left = new_root
            elif node == node.parent.right:
                node.parent.right = new_root
        else:
            self.root = new_root
        node.parent = new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right != None:
            new_root.right.parent = node
        new_root.right = node
        new_root.parent = node.parent
        if node != self.root:
            if node == node.parent.left:
                node.parent.left = new_root
            elif node == node.parent.right:
                node.parent.right = new_root
        else:
            self.root = new_root
        node.parent = new_root
        
    def insert(self, value):
        new_node = self.Node(value, "RED", None)   
        if self.root == None:
            self.root = new_node
            self.root.change_color()
        else:    
            pointer = self.root   
            while True:
                if value >= pointer.value:
                    if pointer.right == None:
                        pointer.right = new_node
                        new_node.parent = pointer
                        break
                    else:
                        pointer = pointer.right
                else:
                    if pointer.left == None:
                        pointer.left = new_node
                        new_node.parent = pointer
                        break
                    else:
                        pointer = pointer.left
            self.fix_insert(new_node)           

classDict = { "min_heap": MinHeap, "red_black_tree": RedBlackTree, "huffman_tree": HuffmanTree}
    
if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()
