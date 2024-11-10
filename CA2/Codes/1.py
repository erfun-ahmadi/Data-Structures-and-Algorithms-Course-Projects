import sys

class Queue :
    def __init__(self):
        self.my_queue = list()
        
    def getSize(self):
        print(len(self.my_queue))
        
    def enqueue(self, value):
        self.my_queue.append(value)
        
    def dequeue(self):
        print(self.my_queue[0])
        self.my_queue.pop(0)
        
    def isEmpty(self):
        if len(self.my_queue) == 0:
            print(True)
        else:
            print(False)
    
    def getInOneLine(self):
        print(*self.my_queue)
            
class Stack:
    def __init__(self, size=10):
        self.my_stack = list()
        self.size = size

    def isEmpty(self):
        if len(self.my_stack) == 0:
            print(True)
        else:
            print(False)

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        print(self.my_stack[len(self.my_stack)-1])
        self.my_stack.pop(len(self.my_stack)-1)

    def put(self,value_):
        self.my_stack.pop(len(self.my_stack)-1)
        self.my_stack.append(value_)

    def peek(self):
        print(self.my_stack[len(self.my_stack)-1])

    def expand(self):
        self.size *= 2

    def getInOneLine(self):
        print(*self.my_stack)

    def getSize(self):
        print(len(self.my_stack))
    
    def getCapacity(self):
        print(self.size)

class Node():
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def getList(self):
        pointer = self.head
        elements = list()
        while(pointer):
            elements.append(pointer.data)
            pointer = pointer.next
        print(*elements)
    
    def insertFront(self, new_data):
        new_node = Node(new_data)
        second = self.head
        self.head = new_node
        new_node.next = second
           
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node
    
    def reverse(self):
        first = None
        second = self.head
        while second:
            third = second.next
            second.next = first
            first = second
            second = third
        self.head = first
            
classDict = { "stack": Stack, "queue": Queue, "linked_list": LinkedList}

class Utils():
    def __init__(self):
        pass

    def parseLine(self, line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def deleteEndChar(self, line):
        return line.rstrip(line[-1])

    def getAttributePointer(self, object, attribute):
        return getattr(object, attribute)

    def getArgs(self, argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def runFunction(self, attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)

class MainEmu():
    def __init__(self):
        self.utils = Utils()
        self.items = dict()

    def startProgram(self):
        for line in sys.stdin:
            line = self.utils.deleteEndChar(line)
            action, line = self.utils.parseLine(line)
            actionPointer = self.utils.getAttributePointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = self.utils.parseLine(line)
        itemName, line = self.utils.parseLine(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = self.utils.parseLine(line, '.')
        funcName, line = self.utils.parseLine(line, '(')
        argsLine, line = self.utils.parseLine(line, ')')
        args = self.utils.getArgs(argsLine)
        attribute = self.utils.getAttributePointer(self.items[itemName],
                                                   funcName)

        self.utils.runFunction(attribute, args)

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.startProgram()
