numberList:list = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
hp:int = len(numberList) - 1
lp:int = 0
number:int = 111
while number != "found":
      if lp == hp or number not in numberList:
          break # num not found in list or in range
      if numberList[lp] == number or numberList[hp] == number or numberList[((lp + hp) // 2)] == number:
              break # num found
      if numberList[(lp + hp) // 2 ] > number:# Algorithm
          hp = (lp + hp) // 2 - 1
          lp += 1
      if numberList[(lp + hp) // 2] < number:
          lp = (lp + hp) // 2 + 1
          hp -= 1
# This program finds the middle of the array, checks the mid, low, and high pointers to see if they are higher than, lower than, or are the number. Then adjusts the pointers to a correct range.
# If the number is 17, the Low Pointer starts at -20(beginning of array), and the High Pointer starts at 50(end of array), A mid pointer looks at the in between(15).
# Since 15 is below 17 AND NOT the answer, it adjusts the Low pointer UP (Mid value + 1 place) to 16 and moves the high pointer DOWN 1 place to 49. The mid is now (32)
# Since 32 is above 17 AND NOT the answer, it adjusts the High pointer DOWN (Mid value - 1 place) to 31, and the Low pointer UP 1 to 17(the answer).
# The checks are run and the Low Pointer is found to be the answer.
# This was fun and super challenging, and I would never have figured it out if I didn't draw it on the board.