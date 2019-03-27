def curve_pre():
    def curve():
        return 'nihao'
    return curve


a = curve_pre()()
print(a)