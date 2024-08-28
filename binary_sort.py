def findNum(number:int, numberList:list):
  lp:int = 0
  hp:int = len(numberList) - 1
  def pointerPos():
    print(f"\nLow pointer pos: {numberList[lp]}")
    print(f"High pointer pos: {numberList[hp]}")
    print(f"Mid pointer pos: {numberList[((lp + hp) // 2)]}\n")
    

  pointerPos()
  while number != "found":
      if lp == hp:# Some basic error handling is added if its not found, or not in range.
          print("num not found")
          break
      if numberList[lp] == number or numberList[hp] == number or numberList[((lp + hp) // 2)] == number:
          if numberList[lp] == number:
              print(f"{number} Found as low pointer")
              break
          elif numberList[hp] == number:
              print(f"{number} Found as high pointer")
              break
          elif numberList[((lp + hp) // 2)]:
              print(f"{number} Found as mid check")
              break
      
      if numberList[(lp + hp) // 2 ] > number:
          print("Moving left")
          hp = (lp + hp) // 2 - 1
          lp += 1
          pointerPos()
      if numberList[(lp + hp) // 2] < number:
          print("Moving right")
          lp = (lp + hp) // 2 + 1
          hp -= 1
          pointerPos()

if __name__== "__main__":
    numberList:list = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 
 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    number:int = 17
    counter:int=0
    if number not in numberList:
        print(f"num not in range of {numberList[0]} and {numberList[-1]} \n")
        quit()
    findNum(number, numberList)

#This program finds the middle of the array, checks the mid, low, and high pointers to see if they are higher than, lower than, or are the number. Then adjusts the pointers to a correct range.
#If the number is 17, the Low Pointer starts at -20(beginning of array), and the High Pointer starts at 50(end of array), A mid pointer looks at the in between(15).
#Since 15 is below 17 AND NOT the answer, it adjusts the Low pointer UP (Mid value + 1 place) to 16 and moves the high pointer DOWN 1 place to 49. The mid is now (32)
#Since 32 is above 17 AND NOT the answer, it adjusts the High pointer DOWN (Mid value - 1 place) to 31, and the Low pointer UP 1 to 17(the answer).
# The checks are run and the Low Pointer is found to be the answer.
# This was fun and super challenging, and I would never have figured it out if I didn't draw it on the board.