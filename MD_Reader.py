from Styler import Styler
import re

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
      print(self.identifyParse(open(filename, 'r').read()))
   
   def identifyParse(self, filestr):
      pre, md, buffer = "", "", ""
      header = 0

      pre = filestr
      
      # strike through
      pre = re.sub("\~\~[^\~]*\~\~", self.__STRKE, pre)
      
      # bold
      pre = re.sub("\_\_[^\_]*\_\_", self.__B, pre)
      pre = re.sub("\*\*[^\*]*\*\*", self.__B, pre)
      
      # Italic
      pre = re.sub("\*[^\*]*\*", self.__I, pre)
      pre = re.sub("\_[^\_]*\_", self.__I, pre)

      # paragraphing
      pre = re.sub("[^\n\#][ ]*\n[^\n\#]", self.__NEWLINE, pre)
      pre = re.sub("\n+", "\n\n", pre)
      
      # superfluos spacing
      pre = re.sub("[ ]+", " ", pre)
      
      for char in pre:
         if (char == "#"):
            header += 1
         
         elif (char == "\n"):
            if (header > 0 and header < 7):
               md += self.header[header](buffer) + "\n"
               header = 0
            else:
               md += buffer + "\n"

            buffer = ""

         else:
            buffer += char

      
      return md

   def __B (self, matchObj):
      return S.b(matchObj.group(0)[2:-2])

   def __I (self, matchObj):
      return S.i(matchObj.group(0)[1:-1])

   def __STRKE (self, matchObj):
      return S.strike(matchObj.group(0)[2:-2])

   def __NEWLINE (self, matchObj):
      return re.sub("\n", " ", matchObj.group(0))


if __name__ == "__main__":
   MD = MD_Reader()
   MD.read("test-simple-text.md")
   print("\n\n\n")
   MD.read("demo.md")