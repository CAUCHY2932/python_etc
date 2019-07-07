class Judge:
    """
    测试，如果在init语句中使用初始化会出现什么情况
    
"""
    def __init__(self, list):
        self.list = list

    def __lt__(self, other):
        s, t = 0, 0
        for c in self:
            s += c
        for c in other:
            t += c
        return True if s > t else False

