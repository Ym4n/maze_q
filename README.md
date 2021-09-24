# maze challenge

Given maze 2D(NxN) represent floor , for exmple like this :
```
###  #
#    #
# #  #
     #
######
```

each wall represent as # </br>
open space represent as space(=>' ') </br>
the output of your code need to print this:

```
+-o  o
|    |
o o  | 
     | 
o----+
```


* Empty areas will remain as spaces.
* If a wall is neighbored directly above and below by walls (but not to the left or right), it will be represented as '|'

* If a wall is neighbored directly to the left and right by walls (but not above or below), it will be represented as '-'

* If a wall has no more than one neighboring wall, it will be represented as 'o' (the lowercase letter) 

* If a wall does not fall into one of the previous categories ,it will be represented as '+'
