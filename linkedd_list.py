# # class linked:
# #     def __init__(self,value):
# #         self.head=value
# #         self.next = None


# # a = linked(2)
# # # print(int(0x000001D87E23EC10))
# # # print(id(a))
# # # print(a.next)

# # b = linked(3)
# # c = linked(4)
# # # print(b.head)
# # # print(a.next)
# # a.next = b
# # b.next = c
# # print(b.next)

# class link:
#     def __init__(self,value):
#         self.head = value
#         self.next = None
#         self.n = 0
#     def inset_node(self,value):
#         new_node = link(value)
#         new_node.next = self.head

#         self.head = new_node
#         self.n = self.n +1

#     def read(self):
#         node = self.head
#         st = ''
#         while node!=None:
#             print(node.head)
#             node = node.next
             



# x = link(5)


# x.inset_node(10)

# x.inset_node(100)
# x.inset_node(20)
# x.inset_node(200)
# x.inset_node(30)

# x.read()


