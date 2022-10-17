#Create list
>>> L=[]
>>> L
[]
>>> L.append(1)
>>> L
[1]
>>> L.append(2)
>>> L.append(3)
>>> L.append(4)
>>> L.append(5)
>>> L
[1, 2, 3, 4, 5]
>>> L=[1, 2, 3, 4, 5, 6]
>>>
>>> L
[1, 2, 3, 4, 5, 6]
>>> print(L)
[1, 2, 3, 4, 5, 6]
>>> len(L)
6
>>> n = len(L)
>>> n
6
>>> type(n)
<class 'int'>

#List, slices
>>> L[0]
1
>>> L[2]
3
>>> L[5]
6
>>> L[-1]
6
>>> L[-1]==L[5]
True
>>> L[-6]
1
>>> L[-7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> L[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> L[0:2]
[1, 2]
>>> L[0:3]
[1, 2, 3]
>>> L2 = L[0:3]
>>> L2
[1, 2, 3]
>>> L.append(20)
>>> L[1:5]
[2, 3, 4, 5]
>>> L[1]=47
>>> L2 = L[0:3]
>>> L2
[1, 47, 3]
>>> L[:5]
[1, 47, 3, 4, 5]
>>> L[0:]
[1, 47, 3, 4, 5, 6, 20]
>>> L[2:]
[3, 4, 5, 6, 20]
>>> L[0:5:2]
[1, 3, 5]
>>> L[0:5:1]
[1, 47, 3, 4, 5]
>>> L[0:5:2]
[1, 3, 5]

#List, other operations
>>> 5 in L
True
>>> 68 in L
False
>>> L
[1, 47, 3, 4, 5, 6, 20]
>>> L2
[1, 47, 3]
>>> L3 = L + L2
>>> L3
[1, 47, 3, 4, 5, 6, 20, 1, 47, 3]
>>> L[1]='bye'
>>> L
[1, 'bye', 3, 4, 5, 6, 20]
>>> L[1]=L2
>>> L
[1, [1, 47, 3], 3, 4, 5, 6, 20]

#String, slices
>>> S='Hello world'
>>> S[0]
'H'
>>> len(S)
11
>>> S[11]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> S[10]
'd'
>>> S[4:]
'o world'
>>> S[3:]
'lo world'
>>> S[:8]
'Hello wo'
>>> S[-2]
'l'
>>> S[0:10:2]
'Hlowr'
>>> S[0:10:3]
'Hlwl'
>>> S[::3]
'Hlwl'
>>> S[::1]
'Hello world'
>>> S[::-1]
'dlrow olleH'
>>> S[::-2]
'drwolH'

#Stack, properties
>>> S=[]
>>> S.append('Monday')
>>> S.append('Tuesday')
>>> S.append('Wednesday')
>>> S.append('Thursday')
>>> S
['Monday', 'Tuesday', 'Wednesday', 'Thursday']
>>> item = S.pop()
>>> item
'Thursday'
>>> S
['Monday', 'Tuesday', 'Wednesday']
>>> item = S.pop()
>>> item
'Wednesday'
>>> S
['Monday', 'Tuesday']
>>> item = S.pop()
>>> S
['Monday']
>>> item = S.pop()
>>> item
'Monday'
>>> S
[]
>>> item = S.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list

#Queue, properties
>>> Q=[]
>>> Q.append('Monday')
>>> Q.append('Tuesday')
>>> Q.append('Wednesday')
>>> Q.append('Thursday')
>>> Q
['Monday', 'Tuesday', 'Wednesday', 'Thursday']
>>> item = Q.pop(0)
>>> item
'Monday'
>>> Q
['Tuesday', 'Wednesday', 'Thursday']
>>> item = Q.pop(0)
>>> item
'Tuesday'
>>> Q
['Wednesday', 'Thursday']
>>> item = Q.pop(0)
>>> item
'Wednesday'
>>> Q
['Thursday']
>>> item = Q.pop(0)
>>> item
'Thursday'
>>> Q
[]
>>> item = Q.pop(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list

#Priority queue
>>> import queue
>>> PQ = queue.PriorityQueue()
>>> PQ.put((1, 'Monday'))
>>> PQ
<queue.PriorityQueue object at 0x00000289B789D9C0>
>>> PQ.put((3, 'Tuesday'))
>>> PQ.put((0, 'Wednesday'))
>>> item = PQ.get()
>>> item
(0, 'Wednesday')
>>> item = PQ.get()
>>> item
(1, 'Monday')
>>> item = PQ.get()
>>> item
(3, 'Tuesday')

#Tuple
>>> N=(1,2,3,4,5,6)
>>> N[0]
1
>>> N[5]
6
>>> N[0]=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


#Set
>>> S={'Jan','Lukas','Jana','Petra', 'Marketa'}
>>> S
{'Lukas', 'Jana', 'Jan', 'Petra', 'Marketa'}
>>> S[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> S1 = S
>>> S1
{'Lukas', 'Jana', 'Jan', 'Petra', 'Marketa'}
>>> S2 = {'Lukas', 'Jan','Teodor'}
>>>
>>> S2
{'Teodor', 'Lukas', 'Jan'}
>>> len(S2)
3
>>> 'Jan' in S2
True
>>> 'Jan' in S1
True
>>> 'Jana' in S1
True
>>> 'Jana' in S2
False
>>> S2.insert('Olivie')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'insert'
>>> S2
{'Teodor', 'Lukas', 'Jan'}

#Set, boolean operations
>>> U = S1.union(S2)
>>> U
{'Teodor', 'Lukas', 'Jana', 'Jan', 'Petra', 'Marketa'}
>>> S1
{'Lukas', 'Jana', 'Jan', 'Petra', 'Marketa'}
>>> S2
{'Teodor', 'Lukas', 'Jan'}
>>> U
{'Teodor', 'Lukas', 'Jana', 'Jan', 'Petra', 'Marketa'}
>>> U2 = S2.union(S1)
>>> U2
{'Lukas', 'Petra', 'Marketa', 'Teodor', 'Jana', 'Jan'}
>>> I = S1.intersection(S2)
>>> I
{'Lukas', 'Jan'}
>>> D1 = S1.differnce(S2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
>>> D1 = S1.difference(S2)
>>> D
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'D' is not defined. Did you mean: 'D1'?
>>> D1
{'Petra', 'Jana', 'Marketa'}
>>> D2 = S2.difference(S1)
>>> D2
{'Teodor'}

#Dictionary
>>> D={1234:['Jan', 'Novak'], 4567:['Eliska','Novotna']}
>>> D
{1234: ['Jan', 'Novak'], 4567: ['Eliska', 'Novotna']}
>>> len(D)
2
>>> 1234 in D
True
>>> D.get(1234)
['Jan', 'Novak']
