class err(Exception):
    pass
class empexp(err):
    pass
class emp:
    def__init__(self,ename,sal)
    try:
      if sal<15000:
          raise empexp
        else:
            self.en=ename
            self.s=sal
            print(self.en,self.s)
           except empexp:
               print("emp sal should not be less then 15000")
    
