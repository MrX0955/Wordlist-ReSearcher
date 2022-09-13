class MrX:
    def __init__(self):
        self.num = 0
        self.hesapnum = 0
        self.liste = []
        self.accts = open("hhh.txt", "r", encoding="utf-8").readlines()
        for i in self.accts: self.acct = i.strip()
        self.keys = open("key.txt", "r", encoding="utf-8").readlines()

    def main(self):
        while len(self.accts) > self.num:
            for key in self.keys:
                self.x = key.strip()
                try:
                    hesap = self.accts[self.hesapnum]
                except IndexError:
                    self.num += 1
                    self.hesapnum = 0
                self.liste.append(self.x)
                if self.liste[self.num] in hesap:
                    print(hesap.strip())
                    self.num += 1
                    self.hesapnum += 1
                else:
                    #print(self.liste[self.num], hesap)
                    self.hesapnum += 1

MrX().main()
