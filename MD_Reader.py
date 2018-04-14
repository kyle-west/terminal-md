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

      for word in line.split():
         if   (word == "#"): header = 1
         elif (word == "##"): header = 2
         elif (word == "###"): header = 3
         elif (word == "####"): header = 4
         elif (word == "#####"): header = 5
         elif (word == "######"): header = 6
         else: l2 += word + " "

      if (header > 0): l2 = self.header[header](l2)

      return l2


if __name__ == "__main__":
   MD = MD_Reader()
   MD.read("test-simple-text.md")