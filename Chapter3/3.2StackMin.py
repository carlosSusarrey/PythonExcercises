# Chapter 3 problem 2


class Stack:

    class __StackNode:

        def __init__(self, value: int, next_node, minimum: int):
            self.next = next_node
            self.value = value
            self.my_min = minimum

    def __init__(self):
        self.top = None
        self.minimum = 0

    def push(self, value):
        if self.top is None:
            self.top = self.__StackNode(value, None, 0)
            self.minimum = value
        else:
            temp = self.top
            if value < self.min:
                self.minimum = value
            self.top = self.__StackNode(value, temp, self.minimum)

    def peek(self):
        if self.top is None:
            print("The stack has 0 elements")
            return
        return self.top.value

    def pop(self):
        if self.top is None:
            print("Stack has 0 elements")
            return
        temp = self.top
        self.top = self.top.next
        if temp.value == self.minimum:
            self.minimum = self.top.my_min
        return temp.value

    def min(self):
        if self.top is None:
            print("No elements in the Stack")
            return
        else:
            return self.minimum