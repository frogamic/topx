#!/usr/bin/env python3
from heapq import *
import sys, io

class NumberStream:
  def __init__(self, fileStream):
    self.fileStream = fileStream
    self.line = 0
  def __iter__(self):
    return self
  def __next__(self):
    next = None
    while next == None:
      try:
        self.line += 1
        next = self.fileStream.readline()
        if next == '':
          raise StopIteration
        next = int(next)
      except StopIteration:
        raise StopIteration
      except:
        print(f'Error getting number on line {self.line}', file=sys.stderr)
        next = None
    return next

def die(msg, num=2):
    print(msg, file=sys.stderr)
    exit(num)

def topx(x, numberStream):
  h = []
  for i in numberStream:
    if len(h) < x:
      heappush(h, i)
    elif i > h[0]:
      heapreplace(h, i)
  return [heappop(h) for i in range(len(h))]

def main(argv):
  x = None
  filename = None
  try:
    x = int(argv[1])
    filePath = argv[2]
    if x < 0:
      raise ValueError
  except:
    die(f'usage: {argv[0]} number filepath\n  Number: integer >= 0');

  if x == 0:
    # All done here ;)
    exit()

  with io.open(filePath, 'r', encoding='utf-8') as file:
    numberStream = NumberStream(file)
    bignums = topx(x, numberStream)
    bignums.reverse()
    for i in range(len(bignums)):
      print(bignums[i])

if __name__ == '__main__':
  main(sys.argv)
