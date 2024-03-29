import random as r

class Dice:
    def __init__(self,val):#selfは初期で入れなければならない、valは第一引数
        self.face_num = val

    def shot(self):
        return r.randint(1,self.face_num)