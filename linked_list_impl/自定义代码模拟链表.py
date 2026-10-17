class SingleNode:
    def __init__(self,item):
        self.item = item        #元素域
        self.next = None        #地址域

class SinglenessList:
    def __init__(self,node=None):
        self.head = node        #链表的 头节点 指向第一个节点


    # 2．is_empty(self）链表是否为空
    def is_empty(self):
        return True if self.head is None else False
        # return self.head is None      #最终极简版本

    # 3.length(self）链表长度
    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


    # 4．travel(self.）遍历整个链表
    def travel(self):
        cur = self.head
        while cur:
            print(f'数值域：{cur.item}')
            cur = cur.next


    # 5．add(self，item）链表头部添加元素
    def add(self,item):
        cur = self.head
        new_node = SingleNode(item)
        new_node.next = cur
        self.head = new_node


    # 6.append(self，item）链表尾部添加元素
    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node


    # 7．insert(self，pos，item）指定位置添加元素
    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            node = SingleNode(item)

            while count < pos-1:
                #走到这里 说明还未找到要插入前的那个节点 进行节点后移操作
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node


    # 8.remove(self，item)删除节点
    def remove(self,item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                    cur.next = None
                return
            else:
                pre = cur
                cur = cur.next


    # 9．search(self，item）查找节点是否存在
    def search(self,item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False



if __name__ == '__main__':
    node1 = SingleNode("xzx")
    print(f'元素域：{node1.item}')
    print(f'地址域：{node1.next}')
    print(f'node1的类型：{type(node1)}')
    print('-'*40)

    my_ll = SinglenessList(node1)
    print(f'my_ll的头节点：{my_ll.head}')
    print(f'头节点的元素域：{my_ll.head.item}')
    print(f'头节点的地址域：{my_ll.head.next}')
    print('-'*40)

    print(my_ll.is_empty())
    print(my_ll.search("bzx"))

    print('-'*40)

    my_ll.add("yzy")
    print('-'*40)

    my_ll.append("bzx")
    print('-'*40)

    print(f'链表长度为：{my_ll.length()}')
    print('-'*40)


    my_ll.insert(-3,"wangji")
    my_ll.insert(2,"hesi")
    my_ll.insert(10,"danyuan")

    my_ll.remove("yzy")

    my_ll.travel()
    print('-'*40)














