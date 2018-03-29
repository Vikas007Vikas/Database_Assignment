import sys

class Btree:
    def __init__(self,degree):
        self.root = None
        self.degree = degree
        self.initial = 0
        pass
    def insert(self,key):
        if self.root is None:
            print 'root is NULL'
            self.root = BtreeNode(self.degree,True)
            self.root.keys[0] = key
            print self.root.keys
            self.root.n += 1
        else:
            print 'root is not NULL'
            # if not self.root.isblockfull():
            #     print 'root is not full'
            #     self.root.insert(key)
            #     print self.root.keys
            #
            # elif self.root.isblockfull():
            #     print 'root is full'
            #     add_root = BtreeNode(self.degree,False)
            #     add_root.children[0] = self.root
            #     add_root.split_node(add_root.children[0],key)
            #     self.initial = 1
            #     print (add_root.keys)
            #     print (add_root.children[0].keys)
            #     # ind = 0
            #     # if add_root.keys[0]<key:
            #     #     ind = ind + 1
            #     # add_root.children[ind].insert(key)
            #     # print add_root.keys
            #     # print add_root.children[0].keys
            #     print add_root.children[1].keys
            #     self.root = add_root
            self.root.insert(key)
    def print_tree(self):
        if self.root is not None:
            self.root.print_tree()

class BtreeNode:
    def __init__(self,degree,isleaf):
        self.degree = degree
        self.isleaf = isleaf
        self.keys = [None]*(degree)
        self.children = [None]*(degree+1)
        self.parent = None
        self.n = 0
        pass
    def insert(self,key):
        #print self.keys
        i = self.n - 1
        #print('size of root',self.n)
        if self.isleaf:
            print 'is leaf'
            if self.isblockfull():
                print 'leaf is full'
                self.parent.split_node(self,key)
            else:
                print 'leaf is not full'
                while i>=0 and self.keys[i]>key:
                    #print i
                    self.keys[i+1] = self.keys[i]
                    i = i-1
                self.keys[i+1]=key
                #print (self.keys)
                self.n += 1
        else:
            print 'is not leaf'
            while i>=0 and self.keys[i]>key:
                i = i-1
            #print i
            self.children[i+1].insert(key)

    def split_node(self,child,key):
        split_child = BtreeNode(child.degree,child.isleaf)


        temp_array = [None]*(child.degree+1)
        for i in range(0,child.n):
            temp_array[i]=child.keys[i]
        i = child.n - 1;
        while i>=0 and child.keys[i]>key:
            temp_array[i+1] = child.keys[i]
            i = i - 1
        temp_array[i+1]=key
        split_index = len(temp_array)/2

        i = self.n - 1
        while i>=0 and self.keys[i]>temp_array[split_index]:
            self.children[i+2] = self.children[i+1]
            self.keys[i+1]=self.keys[i]
            i = i - 1;
        index = i+1;
        #insert into parent
        if not self.isblockfull():
            self.keys[index] = temp_array[split_index]
        elif self.isblockfull():
            #split the parent node
            ass=1
            print 'ass'

        k=0
        for i in range(0,len(temp_array)):
            if(i>=split_index):
                if(k<split_child.degree):
                    split_child.keys[k]=temp_array[i]
                    split_child.n += 1
                    k = k + 1
                if(i<child.degree):
                    child.keys[i]=None
                    child.n -= 1
            else:
                child.keys[i]=temp_array[i]

        #assigning right child to the current root
        self.children[index+1] = split_child

        #assigning parents to the nodes
        self.parent = None
        child.parent = self
        split_child.parent = self
        # print child.keys
        # print split_child.keys
        self.n += 1


    def isblockfull(self):
        return self.n == self.degree
    def print_tree(self):
        i=0
        #print 'size:',self.n
        while i<self.n:
            if not self.isleaf:
                if self.children[i] is not None:
                    self.children[i].print_tree()
            # print self.keys[i]
            i = i + 1
        print self.keys
        if not self.isleaf:
            if self.children[i] is not None:
                self.children[i].print_tree()



def executequeries(file_name):
    lines = [line.rstrip('\n') for line in open(file_name,'r')]
    #print lines
    for line in lines:
        print line
        line = line.split(" ")
        #print line
        if line[0]=='INSERT':
            tree.insert(int(line[1]))
        # elif line[0]=='FIND':
        #     tree.find(int(line[1]))
        # elif line[0]=='COUNT':
        #     tree.count(int(line[1]))
        # elif line[0]=='RANGE':
        #     tree.range(int(line[1]),int(line[2]))
    tree.print_tree()
args = sys.argv
file_name = args[1]
m = args[2]
b = args[3]
print b
# buffers = []
# for i in range(0,m-1):
#     buffers.append([])

degree = (int(b)-8)/12
print degree
tree = Btree(degree)
print tree.root
print tree.degree
executequeries(file_name)
