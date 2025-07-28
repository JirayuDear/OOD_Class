class TorKham:
    def __init__(self):
        self.words = []
    
    
    def restart(self):
      self.words = []
      return "game restarted"
  
    def play(self, word):
      # if word == "X":
      #   return "game over"


      if word in self.words:
        return f"'{word}' -> game over"  # ห้ามซ้ำ

      if len(self.words) == 0:
        self.words.append(word)
        return f"'{word}' -> {self.words}"

      last_word = self.words[-1]

      # เอาตัวอักษร 2 ตัวสุดท้ายของคำก่อนหน้า
      last_two = last_word[-2:].lower()
      # เอาตัวอักษร 2 ตัวแรกของคำใหม่
      new_two = word[:2].lower()

      if last_two == new_two:
        self.words.append(word)
        return f"'{word}' -> {self.words}"
      else:
        return f"'{word}' -> game over"
        

    
    def add_word_list(self, word):
       return self.words.append(word)

torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')


for i in range(len(S)):
  if S[i][0] !='R':
    if S[i][0] == 'P':
      print(torkham.play(S[i].strip("P ")))
    elif S[i][0] == 'X':
      break
    else:
      print(f"'{S[i]}' is Invalid Input !!!")
      break
  else:
    print(torkham.restart())

