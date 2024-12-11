#by:neverfriendme
import math
def radius_calc_circ():
  try:
    r = int(input("Radius:\n"))
    r *= r
    a = r*math.pi
    print(f"The area of the circle is {a}")
  except ValueError:
    print("Incorrect Value")
