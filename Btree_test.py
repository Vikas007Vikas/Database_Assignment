import sys

class Btree:
    def __init__(self,degree):
        self.root = None
        self.degree = degree
        self.initial = 0
        self.issplit = False
        pass
    def insert(self,key):
        if self.root is None:
            #print 'root is NULL'
            self.root = BtreeNode(self.degree,True)
            self.root.keys[0] = key
            #print self.root.keys
            self.root.n += 1
        else:
            #print 'root is not NULL'
            self.issplit,value,point = self.root.insert(key)
            #print self.issplit
            if(self.issplit == True):
                add_root = BtreeNode(degree,False)
                add_root.children[0] = self.root
                val,pointer = add_root.split_node(self.root,value,point)
                add_root.keys[0] = val
                add_root.children[1] = pointer
                add_root.n += 1
                self.root = add_root

    def print_tree(self,count):
        if self.root is not None:
            self.root.print_tree(count)

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
        self.next = None
        self.n = 0
        self.issplit = False
        pass
    def insert(self,key):
        #print self.keys
        i = self.n - 1
        #print('size of root',self.n)
        if self.isleaf:
            #print 'is leaf'
            if self.isblockfull():
                #print 'leaf is full'
                self.issplit = True
                return self.issplit,key,None
            else:
                #print 'leaf is not full'
                while i>=0 and self.keys[i]>key:
                    #print i
                    self.keys[i+1] = self.keys[i]
                    i = i-1
                self.keys[i+1]=key
                #print (self.keys)
                self.n += 1
        else:
            #print 'is not leaf'
            while i>=0 and self.keys[i]>key:
                i = i-1
            #print i
            self.issplit,val1,point1 = self.children[i+1].insert(key)
            if self.issplit:
                val,pointer = self.split_node(self.children[i+1],val1,point1)
                #print self.keys,val
                if self.isblockfull():
                    return True,val,pointer
                i = self.n - 1
                self.keys.append(0)
                while i>=0 and self.keys[i]>val:
                    self.keys[i+1] = self.keys[i]
                    self.children[i+2] = self.children[i+1]
                    i = i - 1
                #print i
                #print self.n
                #print len(self.keys)
                self.keys[i+1] = val
                self.children[i+2] = pointer
                self.n += 1
        return False,None,None

    def split_node(self,child,key,pointer):
        if child.isleaf:
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

            return temp_array[split_index],split_child
        else:
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


            child_list = []
            for i in range(0,child.n+1):
                child_list.append(child.children[i])

            #print child_list
            i = child.n -1
            #print 'key:',key
            child_list.append(0)

            #print i
            while i>=0 and temp_array[i]>=key:
                child_list[i+2] = child_list[i+1]
                i = i - 1
            #print 'ssss:',i
            child_list[i+2] = pointer

            print child_list


            k=0
            # for i in range(0,len(temp_array)):
            #     if(i>split_index):
            #         if(k<split_child.degree):
            #             split_child.keys[k]=temp_array[i]
            #             split_child.n += 1
            #             k = k + 1
            #         if(i<child.degree):
            #             child.keys[i]=None
            #             child.n -= 1
            #     elif i<split_index:
            #         child.keys[i]=temp_array[i]
            child.keys = temp_array[:split_index]
            split_child.keys = temp_array[split_index+1:]
            child.n = len(child.keys)
            split_child.n = len(split_child.keys)
            # print 'ss:',child.keys
            # print 'ss:',split_child.keys
            #print 'len:',len(child_list)

            i = 0
            while i<=child.n:
                child.children[i] = child_list[i]
                i += 1
            while k<=split_child.n:
                #print k,i
                split_child.children[k] = child_list[i]
                i += 1
                k += 1

            return temp_array[split_index],split_child



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

    def isblockfull(self):
        #print self.n,self.degree
        return self.n == self.degree
    def print_tree(self,count):
        i=0
        #print 'size:',self.n
        while i<self.n:
            if not self.isleaf:
                if self.children[i] is not None:
                    self.children[i].print_tree(count+1)
            # print self.keys[i]
            i = i + 1
        print self.keys,self.n,count
        if not self.isleaf:
            if self.children[i] is not None:
                self.children[i].print_tree(count+1)



def executequeries(file_name):
    lines = [line.rstrip('\n') for line in open(file_name,'r')]
    #print lines
    for line in lines:
        #print line
        line = line.split(" ")
        #print line
        if line[0]=='INSERT':
            tree.insert(int(line[1]))
        elif line[0]=='FIND':
            if tree.find_key(int(line[1])):
                print 'Yes'
            else:
                print 'No'
        elif line[0]=='COUNT':
            print tree.count_key(int(line[1]))
        # elif line[0]=='RANGE':
        #     tree.range(int(line[1]),int(line[2]))
    #tree.print_tree(1)
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
