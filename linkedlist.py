# การทำงานของ linkedlist 
# ต้องการเก็บข้อมูล 3,5,10,15

# การสร้างคลาส node สำหรับกำหนดค่า
class Node :
    def __init__(self,data):
        # print(data);
        self.data = data
        # print(self.data);
        # self.data = 3 
        self.next = None
        self.prev = None
        # print(self.next);
        # self.next = null

# ประกาศตัวแปร
node1 = Node(3) 
node2 = Node(5)
node3 = Node(10)
node4 = Node(15)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

# การเข้าถึงข้อมูลทุกตัว
currentnode = node1 
# node1 = address, node1.data = 3,node1.next = ตำแหน่งถัดไป
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.next

currentnode = node4 
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.prev

# print(node1)
# print(node1.data)
# print(node1.next)
# print()

# print(node2.prev)
# print(node2)
# print(node2.data)
# print(node2.next)
# print()

# print(node3.prev)
# print(node3)
# print(node3.data)
# print(node3.next)
# print()

# print(node4.prev)
# print(node4)
# print(node4.data)
# print(node4.next)