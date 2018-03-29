import sys
class Btree:
    def __init__(self,degree):
        self.root = None
        self.degree = degree
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
            if not self.root.isblockfull():
                print 'root is not full'
                self.root.insert(key)
                print self.root.keys

            elif self.root.isblockfull():
                print 'root is full'
                add_root = BtreeNode(self.degree,False)
                add_root.children[0] = self.root
                add_root.split_node(0,add_root.children[0],key)
                self.initial = 1
                ind = 0
                if add_root.keys[0]<key:
                    ind = ind + 1
                #print ind
                # if not add_root.children[ind].isleaf:
                #     print 'entered'
                #     add_root.children[ind].insert(key)
                # else:
                #     print 'not entered'
                add_root.children[ind].insert(key)
                print add_root.keys
                print add_root.children[0].keys
                print add_root.children[1].keys
                self.root = add_root
    def print_tree(self):
        if self.root is not None:
            self.root.print_tree()
    def print_leaf(self):
        if self.root is not None:
            self.root.print_leaf()

    def find_key(self,key):
        if self.root!=None:
            if self.root.find_key(key):
                return True
        return False

    def count_key(self,key):
        count = 0
        if self.root!=None:
            req_keys = self.root.count_key(key)
            for i in req_keys:
                if i is key:
                    count += 1;
            return count
        return 0


class BtreeNode:
    def __init__(self,degree,isleaf):
        self.degree = degree
        self.isleaf = isleaf
        self.keys = [None]*(degree)
        self.children = [None]*(degree+1)
        self.parent = None
        self.n = 0
        self.flag = 0
        pass
    def insert(self,key):
        #print self.keys
        i = self.n - 1
        #print self.n
        #print('size of root',self.n)
        if self.isleaf:
            while i>=0 and self.keys[i]>key:
                #print i
                self.keys[i+1] = self.keys[i]
                i = i-1
            self.keys[i+1]=key
            print (self.keys)
            self.n += 1
        else:
            print 'is not leaf'
            while i>=0 and self.keys[i]>key:
                i = i-1
            print i
            print 'size:',self.children[i+1].n
            if self.children[i+1].isblockfull():
                print 'child is full'
                self.split_node(i+1,self.children[i+1],key)
                if self.keys[i+1]<key:
                    i = i + 1

            self.children[i+1].insert(key)

    def split_node(self,index,child,key):
        self.flag = 1
        split_child = BtreeNode(child.degree,child.isleaf)

        #adding additional code
        # if child.isleaf:
        #     print 'child is leaf node'
        #     temp_array = [None]*(child.degree+1)
        #     for i in range(0,child.n):
        #         temp_array[i] = child.keys[i]
        #     i = child.n - 1
        #     while i>=0 and child.keys[i]>key:
        #         temp_array[i+1] = child.keys[i]
        #         i -= 1
        #     temp_array[i+1]=key
        #     print 'temp_array:',temp_array
        #     split_index = len(temp_array)/2
        #     val = temp_array[split_index]
        #     i = 0
        #     k=0
        #     while i<child.n:
        #         if child.keys[i]>val:
        #             split_child.keys[k]=child.keys[i]
        #             child.keys[i]=None
        #             k = k + 1;
        #             split_child.n += 1
        #         i += 1
        #     child.n = child.n - k
        #
        #     # k=0
        #     # #print 'val:',temp_array[split_index]
        #     # for i in range(0,len(temp_array)):
        #     #     if(i>=split_index):
        #     #         #print 's:',i,' ',temp_array[i]
        #     #         split_child.keys[k]=temp_array[i]
        #     #         if i<child.n:
        #     #             child.keys[i]=None
        #     #             child.n -= 1
        #     #         k = k + 1
        #     #         split_child.n += 1
        #     #     else:
        #     #         child.keys[i] = temp_array[i]
        #
        #     ind = self.n - 1
        #     for i in range(ind,index-1,-1):
        #         self.keys[i+1]=self.keys[i]
        #     self.keys[index]=temp_array[split_index]
        #
        #     ind = self.n
        #     for i in range(ind,index-1,-1):
        #         self.children[i+1]=self.children[i]
        #     #index = i+1;
        #     #insert into parent
        #     self.children[index+1] = split_child
        #
        #     self.n += 1
        #     print child.n
        #     print split_child.n
        # elif not child.isleaf:
        #     print 'child is not leaf node'
        split_index = (child.n)/2
        ind = self.n - 1
        for i in range(ind,index-1,-1):
            self.keys[i+1]=self.keys[i]
        self.keys[index] = child.keys[split_index]
        self.n += 1
        #print 'childval:',child.keys[split_index]
        k=0
        for i in range(0,child.n):
            if(i>split_index):
                split_child.keys[k]=child.keys[i]
                child.keys[i]=None
                k = k+1
                split_child.n += 1
                child.n -= 1
        print child.n
        print split_child.n
        # if not child.isleaf:
        for i in range(child.n):
            split_child.children[i] = child.children[i+split_index+1]
            child.children[i+split_index+1]=None
            #print child.keys
            # for i in child.children:
            #     if i!=None:
            #         print 'sss:',i.keys
            # print split_child.keys
            # for i in split_child.children:
            #     if i!=None:
            #         print 'sss1:',i.keys



        ind = self.n - 1
        print self.keys
        for i in range(ind,index,-1):
            self.children[i+1]=self.children[i]
        #index = i+1;
        #insert into parent
        self.children[index+1] = split_child

        # if not self.isblockfull():
        #     self.keys[index] = temp_array[split_index]
        # elif self.isblockfull():
        #     #split the parent node
        #     ass=1
        #     print 'ass'



        #assigning right child to the current root
        # self.children[index+1] = split_child

        #assigning parents to the nodes
        # self.parent = None
        # child.parent = self
        # split_child.parent = self
        print self.keys
        for i in self.children:
            if(i!=None):
                print 'ss:',i.keys



    def isblockfull(self):
        return self.n == self.degree

    def find_key(self,key):
        i=0
        while i < self.n:
            if(key<=self.keys[i]):
                break
            i += 1
        if i<self.n and self.keys[i]==key:
            return True
        if self.isleaf:
            return False
        return self.children[i].find_key(key)

    def count_key(self,key):
        if not self.isleaf:
            i=0
            while i<self.n and key>=self.keys[i]:
                i = i + 1
            return self.children[i].count_key(key)
        return self.keys



    def print_leaf(self):
        # i = 0
        # while i < self.n:
        #     if not self.isleaf:
        #         if(self.children[i]!=None):
        #             self.children[i].print_leaf()
        #     print(self.keys[i])
        #     i += 1
        # if not self.isleaf:
        #     if(self.children[i]!=None):
        #         self.children[i].print_leaf()
        #print self.keys
        for i in self.children:
            #print i.keys
            if i is not None:
                if not i.isleaf:
                    i.print_leaf()
                else:
                    print i.keys
        if i is not None:
            if not i.isleaf:
                i.print_leaf()

def executequeries(file_name):
    lines = [line.rstrip('\n') for line in open(file_name,'r')]
    #print lines
    for line in lines:
        print line
        line = line.split(" ")
        #print line
        if line[0]=='INSERT':
            tree.insert(int(line[1]))
        elif line[0]=='FIND':
            if tree.find_key(int(line[1]))==True:
                print 'Yes'
            else:
                print 'No'
        elif line[0]=='COUNT':
            print tree.count_key(int(line[1]))
        print '\n'
        # elif line[0]=='RANGE':
        #     tree.range(int(line[1]),int(line[2]))
    #tree.print_tree()
    tree.print_leaf()
args = sys.argv
file_name = args[1]
m = args[2]
b = args[3]
#print b
# buffers = []
# for i in range(0,m-1):
#     buffers.append([])

degree = (int(b)-8)/12
#print degree
tree = Btree(degree)
#print tree.root
#print tree.degree
executequeries(file_name)
