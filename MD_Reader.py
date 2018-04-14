from Styler import Styler

S = Styler(styling='other')

class MD_Reader:
   def __init__(self, filename = None):
      if filename: self.read(filename)
      self.header = {
         1: S.h1,
         2: S.h2,
         3: S.h3,
         4: S.h4,
         5: S.h5,
         6: S.h6
      }
   
   def read(self, filename):
      with open(filename, "r") as file:
         for line in file:
            print(self.identifyParse(line))
   
   def identifyParse(self, line):
      l2 = ""
      header = 0
      B, I = False, False
      sig = ""

      for word in line.split():
         if (word[0] == "#"): 
            header = len(word)

         elif (word[0] == "*" or word[0] == "_"):
            sig += word[0]
            if (word[1] == word[0]):
               B = True
               sig += word[1]
               if (word[2] == "*" or word[2] == "_"):
                  I = True
                  sig += word[2]
            else:
               I = True
            tmp = word[(len(sig)):-(len(sig))]
            if (I): tmp = S.i(tmp)
            if (B): tmp = S.b(tmp)
            l2 += tmp + " "
            B, I, sig = False, False, ""

         else: l2 += word + " "

      if (header > 0): l2 = self.header[header](l2)

      return l2


if __name__ == "__main__":
   MD = MD_Reader()
   MD.read("test-simple-text.md")