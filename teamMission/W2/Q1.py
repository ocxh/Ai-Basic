# 1번 문제
class Score:
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final

    @property
    def save(self):
        return self.__mid, self.__final

    @save.setter
    def save(self, s):
        self.__mid += s[0]
        self.__final += s[1]

    def prt(self):
        print((self.__mid+self.__final)/2)


score = Score(50, 75)
score.save = 10, 20
score.prt()
