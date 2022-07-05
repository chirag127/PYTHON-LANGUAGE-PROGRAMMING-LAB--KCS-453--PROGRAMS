# Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.
# File I/O : File input and output operations in Python Programming
# Exceptions and Assertions
# Modules : Introduction , Importing Modules ,
# Abstract Data Types : Abstract data types and ADT interface in Python Programming.
# 08
# V
from curses import pair_number


def sieve_of_eratosthenes(n):
    prime_list = []
    for i in range(2, n + 1):
        if i not in prime_list:
            prime_list.append(i)
            for j in range(i * 2, n + 1, i):
                if j not in prime_list:
                    prime_list.append(j)
    return prime_list

print(sieve_of_eratosthenes(100))

class file_io:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_object = open(file_name, "r")
        self.file_content = self.file_object.read()
        self.file_object.close()

    def read_file(self):
        return self.file_content

    def write_file(self, content):
        self.file_object = open(self.file_name, "w")
        self.file_object.write(content)
        self.file_object.close()

    def append_file(self, content):
        self.file_object = open(self.file_name, "a")
        self.file_object.write(content)
        self.file_object.close()

    def __del__(self):
        self.file_object.close()

file_io_object = file_io("test.txt")
file_io_object.write_file("Hello World")
file_io_object.append_file("\nHello World")
print(file_io_object.read_file())
del file_io_object


def exeptions_and_assertions():
    try:
        assert 1 == 2
    except AssertionError:
        print("Assertion Error")
    except Exception as e:
        print(e)

exeptions_and_assertions()
class adt():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class adt_list(list):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

adt_list_object = adt_list("adt_list")
print(adt_list_object)
print(adt_list_object == adt_list_object)
print(adt_list_object == adt_list("adt_list"))
print(adt_list_object == adt_list("adt_list2"))

# Classes : Class definition and other operations in the classes , Special Methods ( such as _init_,
# _str_, comparison methods and Arithmetic methods etc.) , Class Example , Inheritance , Inheritance
# and OOP.

def classes():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name

        def __eq__(self, other):
            return self.name == other.name

        def __hash__(self):
            return hash(self.name)

    class Student(Person):
        def __init__(self, name, age, grade):
            super().__init__(name, age)
            self.grade = grade

        def __str__(self):
            return self.name + " " + str(self.grade)

        def __repr__(self):
            return self.name + " " + str(self.grade)

    class Teacher(Person):
        def __init__(self, name, age, salary):
            super().__init__(name, age)
            self.salary = salary

        def __str__(self):
            return self.name + " " + str(self.salary)

        def __repr__(self):
            return self.name + " " + str(self.salary)

    class Course:
        def __init__(self, name, teacher, students):
            self.name = name
            self.teacher = teacher
            self.students = students

        def __str__(self):
            return self.name + " " + str(self.teacher) + " " + str(self.students)

        def __repr__(self):
            return self.name + " " + str(self.teacher) + " " + str(self.students)

    class School:
        def __init__(self, name, courses):
            self.name = name
            self.courses = courses

        def __str__(self):
            return self.name + " " + str(self.courses)

        def __repr__(self):
            return self.name + " " + str(self.courses)

    class StudentCourse(Course):
        def __init__(self, name, teacher, students, grade):
            super().__init__(name, teacher, students)
            self.grade = grade

        def __str__(self):
            return self.name + " " + str(self.teacher) + " " + str(self.students) + " " + str(self.grade)

        def __repr__(self):
            return self.name + " " + str(self.teacher) + " " + str(self.students) + " " + str(self.grade)

    class SchoolCourse(Course):
        def __init__(self, name, teacher, students, grade):
            super().__init__(name, teacher, students)
            self.grade = grade

        def __str__(self):
            return self.name + " " + str(self.teacher) + " " + str(self.students) + " " + str(self.grade)

        def __repr__(self):
            return self.name + " " + str(self.teacher) + " " + str(self.students) + " " + str(self.grade)


    student_1 = Student("John", 20, "A")
    print(student_1)

    teacher_1 = Teacher("John", 20, 1000)
    print(teacher_1)


# Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi
# Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search
# Time
# Sorting & Merging: Selection Sort , Merge List , Merge Sort , Higher Order Sort

def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def tower_of_hanoi(n, A, B, C):
    if n == 1:
        print(A, "->", C)
    else:
        tower_of_hanoi(n - 1, A, C, B)
        print(A, "->", C)
        tower_of_hanoi(n - 1, B, A, C)

def simple_search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1

def binary_search(list, element):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == element:
            return mid
        elif list[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list


print(selection_sort([6, 5, 3, 1, 8, 7, 2, 4]))

def merge_list(list1, list2):
    merged_list =[]
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            merged_list.append(list1[0])
            list1.pop(0)
        else: 
            merged_list.append(list2[0])
            list2.pop(0)
    if len(list1) > 0:
        merged_list += list1
    if len(list2) > 0:
        merged_list += list2
    return merged_list


print(merge_list([1, 3, 5], [2, 4, 6]))


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge_list(left, right)

print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4]))

def higher_order_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = higher_order_sort(list[:mid])
    right = higher_order_sort(list[mid:])
    return merge_list(left, right)