# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# ^^^ for color list

class Styler:
   def __init__(self):
      self.color = {}
      self.color["K"] = "\u001b[30m" # Black
      self.color["R"] = "\u001b[31m" # Red
      self.color["G"] = "\u001b[32m" # Green
      self.color["Y"] = "\u001b[33m" # Yellow
      self.color["B"] = "\u001b[34m" # Blue
      self.color["M"] = "\u001b[35m" # Magenta
      self.color["C"] = "\u001b[36m" # Cyan
      self.color["W"] = "\u001b[37m" # White
      self.color["X"] = "\u001b[0m"  # Reset

   def format(self, msg ="", color="X"):
      return u"" + self.color[color] + msg + self.color["X"]


if __name__ == "__main__":
   S = Styler()

   print (S.format("Red", "R"), 
          S.format("Blue", "B"), 
          S.format("Cyan", "C"), 
          S.format("White", "W"), 
          sep=" | ")
