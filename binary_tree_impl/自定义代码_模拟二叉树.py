class Node:
    def __init__(self,item):
        self.item = item
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self,node=None):
        self.root = node

    def add(self,item):
        new_node = Node(item)
        #判断根节点是否为空,如果为空,设置当前节点为根节点
        if self.root is None:
            self.root = new_node
            return #核心 做完了就不用再往下走了
        #创建队列 添加根节点到队列中
        queue = []
        queue.append(self.root)
        # 通过死循环找到空缺节点的位置
        while True:
            #获取队列的第一个元素
            node = queue.pop(0)
            # 6.判断当前节点的左子树是否为空
            if node.lchild is None:
                node.lchild = new_node
                return
            else: #走这里说明左子树不为空 将当前节点的左子树添加到队列
                queue.append(node.lchild)

            # 7.判断当前节点的右子树是否为空
            if node.rchild is None:
                node.rchild = new_node
                return
            else:
                queue.append(node.rchild)

    #定义breadth()函数,表示:广度优先遍历,一层一层遍历
    def breadth_travel(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            #获取队列的第一个元素
            node = queue.pop(0)
            #打印该节点的元素域
            print(node.item,end=' ')
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    #定义preorder()函数,表示:深度优先遍历(根左右)先序
    def preorder_travel(self,root):
        if root is not None:
            print(root.item,end=' ')
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)


    #定义inorder()函数,表示:深度优先遍历(左根右)中序
    def inorder_travel(self,root):
        if root is not None:
            self.inorder_travel(root.lchild)
            print(root.item, end=' ')
            self.inorder_travel(root.rchild)

    #定义postorder()函数,表示:深度优先遍历(左右根)后续
    def postorder_travel(self,root):
        if root is not None:
            self.inorder_travel(root.lchild)
            self.inorder_travel(root.rchild)
            print(root.item, end=' ')


def dm01_测试节点和二叉树():
    # 创建节点的 元素域,左子树,右子树
    node1 = Node('A')
    # 打印对应信息
    print(node1.item)
    print(node1.lchild)
    print(node1.rchild)

    print('-' * 23)

    # 测试二叉树
    bt = BinaryTree(node1)
    print(bt.root)  # 根节点的地址
    print(bt.root.item)  # 根节点的元素域

def dm02_模拟队列取元素():
    # 创建队列
    queue = []

    # 模拟向队列中添加元素
    queue.append('A')
    queue.append('B')
    queue.append('C')

    # 模拟从队列中取出元素
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    # 打印队列
    print(queue)

def dm03_breadth_travel():
    bt = BinaryTree()
    bt.add('A')
    bt.add('B')
    bt.add('C')
    bt.add('D')
    bt.add('E')
    bt.add('F')
    bt.add('G')
    bt.add('H')
    bt.add('I')
    bt.add('J')

    bt.breadth_travel()

def dm04_深度优先遍历测试():
    bt = BinaryTree()
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    bt.add(10)
    # 深度优先遍历
    print('先序(根左右):', end=' ')
    bt.preorder_travel(bt.root)

    print('\n中序(左根右):', end=' ')
    bt.inorder_travel(bt.root)

    print('\n后序(左右根):', end=' ')
    bt.postorder_travel(bt.root)


if __name__ == '__main__':
    # dm01_测试节点和二叉树()
    # print('-'*23)
    # dm02_模拟队列取元素()
    # print('-'*23)
    # dm03_breadth_travel()
    # print('-'*23)
    dm04_深度优先遍历测试()
































