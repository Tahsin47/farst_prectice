class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("The list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data, end="-->")
                n=n.ref

    def add_beggining(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("The list is not empty")
    def delete_begin(self):
        if self.head is None:
            print("The list is empty.")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("The list is empty ")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def farst_value(self):
        return self.head.data
    def delete_any_value(self,x):
        if self.head is None:
            print("Cannot delete the value becouse the list is empty.")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("The value is not present here")
        else:
            n.ref=n.ref.ref



lll=linked_list()
lll.add_beggining("Tanvir")
lll.add_beggining("Harun")
lll.add_end("Tasin")
lll.add_beggining(("Laboni"))
lll.delete_any_value("Laboni")
lll.print_ll()
