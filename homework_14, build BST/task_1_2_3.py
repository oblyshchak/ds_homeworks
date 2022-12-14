
class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        #Check different conditions for node:
        # 1) if in tree we don't have value, first value which we get it will be node
        if self.value is None:
            self.value = value
            print(f"Inserting value {self.value} is {value}")
            return

        # 2) Checking value
        if self.value == value:
            raise ValueError(f"{value} in tree already")

        # 3) If we get value which is less than ours, and we don't have left child, we assign a value to left child.
        # If we have left child already, we need to call recursively function for this value,
        # but node in this call will be self.left --> parents for value which we get.
        if self.value > value:
            if self.left:
                print(f"Inserting LEFT recursively {value} for {self.value}")
                self.left.insert(value)
            else:
                self.left = Tree(value)
                print(f"Inserting {self.left.value} LEFT")

        # 4)Same as left
        else:
            if self.right:
                print(f"Inserting recursively {value} for {self.value}")
                self.right.insert(value)
            else:
                self.right = Tree(value)
                print(f"Insert {self.right.value} RIGHT")


    def insert_list(self, list_tree):
        #Firstly we need to check list which we took:
        # 1) Length list have to be odd. Node consist of value, left and right.
        if len(list_tree) % 2 == 0:
            raise ValueError(f"{list_tree} invalid list")

        # 2) Determine max index for iteration in the loop,
        # compare last el in the list with len list (2i + 2 = len-1) - last element in the list(right child).
        # Left child has a index (2*i + 1)
        i_max = (len(list_tree) - 3) // 2
        for i in range(i_max+1):
            value = list_tree[i]
            if value is None:
                continue
            left = list_tree[2*i + 1]
            right = list_tree[2*i + 2]
        # Compare left/right with value, if this conditions is False, we call raise and finish program
            if left is not None:
                if left >= value:
                    raise ValueError(f"{left} is greatest than {value}")
            if right is not None:
                if right <= value:
                    raise ValueError(f"{right} is less than {value}")

        # Call function "insert" for each element in the list for building search tree.
        # If value in list is None, we skep this value and continue
        for i in list_tree:
            if i is None:
                continue
            self.insert(i)


    def print_inorder(self):
        #This function for printing tree
        # Calling recursively for each value in tree

        if self.left:
            self.left.print_inorder()
        print(self.value)
        if self.right:
            self.right.print_inorder()


    def min_value(self):
        #Going deep in the tree on the left branch

        if self.left:
            return self.left.min_value()
        else:
            return self.value


    def max_value(self):
        #Going deep in the tree on the right branch

        if self.right:
            return self.right.max_value()
        else:
            return self.value


    def delete(self, value, parent=None):
        #Finding value in the branches

        if self.value > value:
            if self.left:
                self.left.delete(value, self)
        elif self.value < value:
            if self.right:
                self.right.delete(value, self)
        else:
            #Value is found. This value need to be deleted.
            # This conditions true if this value is leaf.
            if self.left is None and self.right is None:
                if parent:
                    # Leaf is a left child
                    if parent.left is self:
                        # Remove left child (us) from parent
                        parent.left = None
                    else:
                        # Leaf is right child
                        parent.right = None
            #This conditions is true if value has right child, and doesn't have left child.
            #Firstly we exchanging parents value with child value,
            #and we do it using recursive function while value wouldn't have a child.
            if self.right and not self.left:
                self.right.value, self.value = self.value, self.right.value
                self.right.delete(self.right.value, self)
                return

            #Same as right
            if self.left and not self.right:
                self.left.value, self.value = self.value, self.left.value
                self.left.delete(self.left.value, self)
                return

            #This conditions is true if value has 2 child.
            # According to the rules of removal value from binary search tree, node's value is replaced with minimal value in right branch.
            # Calling function for definition of minimal value in right branch and make reassignment.
            #Calling function recursively to delete value.
            if self.left and self.right:
                inorder_successor = self.right.min_value()
                self.value, inorder_successor = inorder_successor, self.value
                self.right.delete(self.value, self)


root = Tree(None)
root.insert_list([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None])

print("********")
root.print_inorder()
print("********")
root.delete(1)
root.delete(3)
root.delete(10)
root.delete(6)
root.delete(14)
root.delete(13)
root.delete(8)
root.delete(7)
root.delete(4)
root.print_inorder()
