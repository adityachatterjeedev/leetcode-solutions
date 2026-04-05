# Last updated: 4/5/2026, 12:56:31 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        q=deque()
        q.append(root)
        res=[]
        while(q):
            node=q.popleft()
            if(node is not None):
                res.append(str(node.val))
            else:
                res.append("#")
            if(node is not None):
                q.append(node.left)
            if(node is not None):
                q.append(node.right)
        return ",".join(res)
        

    def deserialize(self, data):
        if not data:
            return None
        list1=data.split(',')
        root=TreeNode(list1[0])
        q=deque()
        q.append(root)
        i=1
        while(q):
            node=q.popleft()
            if(list1[i]!='#'):
                lnode=TreeNode(int(list1[i]))
                node.left=lnode
                q.append(lnode)
            i+=1
            if(list1[i]!='#'):
                rnode=TreeNode(int(list1[i]))
                node.right=rnode
                q.append(rnode)
            i+=1
        return root

                

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))