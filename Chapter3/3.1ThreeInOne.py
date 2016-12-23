# Chapter 3 problem 1
import numpy


class ThreeInOne:
    class __InsideStack:
        def __init__(self, low_limit, limit):
            self.top = low_limit - 1
            self.limit = limit
            self.low_limit = low_limit

        def can_push(self):
            if self.top == self.limit:
                return False
            return True

        def has_elements(self):
            if self.top < self.low_limit:
                return False
            return True

        def push(self):
            self.top += 1

        def pop(self):
            self.top -= 1

    def __init__(self):
        self.array = numpy.empty(30, dtype=object)
        self.stack1 = self.__InsideStack(0, 9)
        self.stack2 = self.__InsideStack(10, 19)
        self.stack3 = self.__InsideStack(20, 29)

    def push(self, stack_number, value):
        if stack_number == 1:
            self.__push_into_stack(self.stack1, value)
        elif stack_number == 2:
            self.__push_into_stack(self.stack2, value)
        elif stack_number == 3:
            self.__push_into_stack(self.stack3, value)
        else:
            print("Invalid stack number")

    def __push_into_stack(self, stack, value):
        if stack.can_push():
            stack.push()
            self.array[stack.top] = value
        else:
            print("This stack is full, wait for new functionality to fix this.")

    def pop(self, stack_number):
        if stack_number == 1:
            self.__pop_from_stack(self.stack1)
        elif stack_number == 2:
            self.__pop_from_stack(self.stack2)
        elif stack_number == 3:
            self.__pop_from_stack(self.stack3)
        else:
            print("Invalid stack number")

    def __pop_from_stack(self, stack):
        if stack.has_elements():
            value = self.array[stack.top]
            self.array[stack.top] = None
            stack.pop()
            return value
        else:
            print("This stack does not have elements")

    def peek(self, stack_number):
        if stack_number == 1:
            self.__peek_from_stack(self.stack1)
        elif stack_number == 2:
            self.__peek_from_stack(self.stack2)
        elif stack_number == 3:
            self.__peek_from_stack(self.stack3)
        else:
            print("Invalid stack number")

    def __peek_from_stack(self, stack):
        if stack.has_elements():
            return self.array[stack.top]
        else:
            print("This stack does not have elements")




mystack = ThreeInOne()
mystack.push(1, 2)
mystack.push(3, 5)
mystack.push(3, 5)
mystack.push(3, 5)
mystack.push(3, 5)
mystack.push(3, 5)
mystack.push(3, 4)
mystack.pop(3)
mystack.peek(2)
print(mystack.array)
