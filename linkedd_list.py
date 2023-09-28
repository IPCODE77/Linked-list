class l_list:
    def __init__(self, value):
        self.data = value
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
# Insert a element at the starting of the array

    def insert_head(self, val):
        # create a new node
        new_node = l_list(val)
        # create a connection between two nodes
        new_node.next = self.head
        # assign head to this node
        self.head = new_node
        # increment the length of linked list
        self.n = self.n+1
# Print the element

    def traverse(self):
        item = self.head
        item_str = ''
        while (item != None):
            item_str += str(item.data)+'-->'
            # item_str = str(item.data)+'-->' + item_str
            item = item.next
        item_str = item_str[:-3]
        print(item_str)

    def insert_last(self, value):
        new_node = l_list(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n+1

        else:
            item = self.head
            while (item != None):
                if (item.next == None):
                    item.next = new_node
                    new_node.next = None
                item = item.next
            self.n = self.n+1

# Insert the element at the end of an array
    def insert_after(self, value, index):
        new_node = l_list(value)
        item = self.head
        while (item != None):
            if item.data == index:
                break
            item = item.next
        if item != None:
            new_node.next = item.next
            item.next = new_node
            self.n = self.n+1

        else:
            return 'Item not found'
# Clear the array

    def clear_array(self):
        self.head = None
        self.n = 0

# Delete from the head
    def delete_at_first(self):
        if self.head == None:
            print('Empty List')
        else:

            item = self.head
            self.head = item.next
            self.n = self.n-1

# Delete from the tail
    def delete_at_last(self):
        if self.head == None:
            print('Empty list')
        else:

            item = self.head

            while (item != None):
                if item.next.next == None:
                    item.next = None
                item = item.next
            self.n = self.n-1
# delete by value

    def delete_by_value(self, value):
        item = self.head
        if self.head.data == value:
            self.head = self.head.next
            self.n = self.n-1
        else:

            while (item.next != None):
                if item.next.data == value:
                    break
                item = item.next

            # There is 2 cases 1.item is not found  2.item is found
            if item.next == None:
                print('Item Not Found')
            else:
                item.next = item.next.next
                self.n = self.n-1
# searching the item
    def searching_item(self,value):
        item = self.head
        pos=0
        while(item!=None):
            if item.data == value:
                return f'Item present in {pos+1} position'
            item = item.next
            pos+=1

        return 'not found'

# Searching item by index position
    def search_by_index(self,index):
        item = self.head
        pos = 0

        while(item!=None):
            if pos==index:
                return item.data
            item = item.next
            pos+=1

        return 'Item Not Found'    

l = linkedlist()
l.insert_head(10)
l.insert_head(20)
l.insert_head(30)
l.insert_head(40)
l.insert_head(120)
l.insert_head(1209)
l.insert_head(50)
l.insert_head(100)

l.insert_last(200)
l.insert_last(500)

l.insert_after(2002, 20)

l.insert_after(400, 2002)

# l.clear_array()
l.delete_at_first()
l.delete_at_first()

l.delete_at_last()
l.delete_at_last()

l.delete_by_value(2002)
l.delete_by_value(40)
l.delete_by_value(1209)


print(l.searching_item(30))
print(l.search_by_index(4))

print(l.n)
# print(l)

l.traverse()
