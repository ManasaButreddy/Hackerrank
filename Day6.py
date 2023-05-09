"""
Task
Given a string, S , of length N that is indexed from 0 to N - 1, print its even-indexed and
odd-indexed characters as 2 space-separated strings on a single line (see the Sample below
for more detail).

Note: 0 is considered to be an even index.
"""


N = int(input())

for i in range(0, N):
  s = input()

  for k in range(0, len(s)):
    if k % 2 == 0:
      print(s[k], end="")
  print(" ", end="")
  for k in range(0, len(s)):
    if k % 2 != 0:   
      print(s[k], end="")
  print(" ")
