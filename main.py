#Remove pass and complete the code
def check_character(word, index):
   if 0 <= index < len(word):
      char = word[index]
      if char.isalpha():
         return "letter"
      elif char.isdigit():
         return "digit"
      elif char.isspace():
         return "white space"
      else:
         return "unknown"
   else:
       return "index out of bounds"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))