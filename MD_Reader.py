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
      self.identifyParse(open(filename, 'r').read())
   
   def identifyParse(self, filestr):
      buffer = ""
      header = 0

      for char in filestr:
         if (char == "#"):
            header += 1
         elif (char == "\n"):
            if (header > 0):
               print(self.header[header](buffer))
               header = 0
            else:
               print(buffer)
            buffer = ""
         else:
            buffer += char
         



if __name__ == "__main__":
   MD = MD_Reader()
   MD.read("test-simple-text.md")