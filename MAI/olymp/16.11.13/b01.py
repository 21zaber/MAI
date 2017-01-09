#!/usr/bin/python3.5

from enum import Enum

class Dir(Enum):
    Top = 1
    Right = 2
    Bottom = 3
    Left = 4
    Front = 5
    Back = 6
 
    def TurnRight(self):
        trans = {Dir.Top: Dir.Right, 
                 Dir.Right: Dir.Bottom,
                 Dir.Bottom: Dir.Left,
                 Dir.Left: Dir.Top,
                 }
        if self in trans:
            return trans[self]
        else:
            return self

    def TurnLeft(self):
        trans = {Dir.Top: Dir.Left, 
                 Dir.Right: Dir.Top,
                 Dir.Bottom: Dir.Right,
                 Dir.Left: Dir.Bottom,
                 }
        if self in trans:
            return trans[self]
        else:
            return self

    def FlipVer(self):
        trans = {Dir.Front: Dir.Back, 
                 Dir.Right: Dir.Left,
                 Dir.Back: Dir.Front,
                 Dir.Left: Dir.Right,
                 }
        if self in trans:
            return trans[self]
        else:
            return self

    def FlipHor(self):
        trans = {Dir.Front: Dir.Back, 
                 Dir.Back: Dir.Front,
                 Dir.Top: Dir.Bottom,
                 Dir.Bottom: Dir.Top,
                 }
        if self in trans:
            return trans[self]
        else:
            return self

    def FlipDiag1(self):
        trans = {Dir.Right: Dir.Bottom, 
                 Dir.Bottom: Dir.Right,
                 Dir.Top: Dir.Left,
                 Dir.Left: Dir.Top, 
                 Dir.Front: Dir.Back,
                 Dir.Back: Dir.Front,
                 }                  
        if self in trans:
            return trans[self]
        else:
            return self

    def FlipDiag2(self):
        trans = {Dir.Left: Dir.Bottom, 
                 Dir.Bottom: Dir.Left,
                 Dir.Top: Dir.Right,
                 Dir.Right: Dir.Top, 
                 Dir.Front: Dir.Back,
                 Dir.Back: Dir.Front,
                 }                  
        if self in trans:
            return trans[self]
        else:
            return self
 
class Axes:
    def __init__(self):
        self.X = Dir.Right
        self.Y = Dir.Front
        self.Z = Dir.Bottom
 
    def __str__(self):
        return '{X=' + str(self.X) + ', Y=' + str(self.Y) + ', Z=' + str(self.Z) + '}'
 
    def apply(self, command):
        foo = None
        if command == '<':
            foo = Dir.TurnLeft
        elif command == '>':
            foo = Dir.TurnRight
        elif command == '|':
            foo = Dir.FlipVer
        elif command == '-':
            foo = Dir.FlipHor
        elif command == '\\':
            foo = Dir.FlipDiag1
        elif command == '/':
            foo = Dir.FlipDiag2
        else:
            raise 'command = [' + str(command) + ']'
 
        self.X = foo(self.X)
        self.Y = foo(self.Y)
        self.Z = foo(self.Z)
        #print(self)
 
def flip_horizontally(m, conv, axes):
    m = m[::-1]
 
    for k, v in conv.items():
        if v == '>':
            conv[k] = '<'
        elif v == '<':
            conv[k] = '>'
        elif v == '/':
            conv[k] = '\\'
        elif v == '\\':
            conv[k] = '/'
 
    axes.apply('-')
    return m
 
def rotate_right(m, conv, axes):
    n = len(m)
    new_m = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_m[i][j] = m[n-j-1][i]
 
    for k, v in conv.items():
        if v == '>':
            conv[k] = '^'
        elif v == 'v':
            conv[k] = '>'
        elif v == '<':
            conv[k] = 'v'
        elif v == '^':
            conv[k] = '<'
        elif v == '/':
            conv[k] = '\\'
        elif v == '\\':
            conv[k] = '/'
        elif v == '|':
            conv[k] = '-'
        elif v == '-':
            conv[k] = '|'
 
    axes.apply('>')
    return new_m
 
while True:
    try:
        n = int(input())
    except:
        break
 
    m = []
    for i in range(n):
        m.append(list(input()))
 
    commands = input().split()
 
    axes = Axes()
    for command in commands:
        axes.apply(command)

    print(axes)
 
    converter = {'<':'<',
                 '>':'>',
                 '^':'^',
                 'v':'v',
                 'o':'o',
                 'x':'x',
                 '|':'|',
                 '-':'-',
                 '/':'/',
                 '\\':'\\'}
 
    if axes.Y == Dir.Back:
        m = flip_horizontally(m, converter, axes)
 
    while axes.X != Dir.Right:
        m = rotate_right(m, converter, axes)
 
   # for i in range(n):
   #     for j in range(n):
   #         m[i][j] = converter[m[i][j]]
 
    for i in range(n):
        print(''.join(m[i]))

