import time

class B_S_T:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = B_S_T(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = B_S_T(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

BST = B_S_T(names_1[0])
for name_1 in names_1:
    BST.insert(name_1)

for name_2 in names_2:
        if BST.contains(name_2):
            duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
#BST is log n time 