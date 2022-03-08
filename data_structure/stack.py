class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack)==0

#检测括号是否匹配
def bracks_match(str):
    stack=Stack()
    match={')':'(',']':'[','}':'{'}
    for ch in str:
        if ch in {'(','[','{'}:
            stack.push(ch)
        else:  #ch in {')',']','}',}
            if stack.is_empty():
                return False
            elif match[ch]==stack.get_top():
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
str='[([])]'
res=bracks_match(str)
print(res)


