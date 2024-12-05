# // Time Complexity :O(1) for next and HasNext
# // Space Complexity :O(d) max stack for depth inside the Nested List
# // Did this code successfully run on Leetcode :Yes
# // Any problem you faced while coding this : self.nextEl = Can't check "next(self.st[-1])" since calling the function uses the next element.

# Also Tried isInstance(list,None). Not workign with iterators.
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = [iter(nestedList)]
        self.nextEl = 0

    def next(self) -> int:
        return self.nextEl.getInteger()
    
    def hasNext(self) -> bool:
        while self.st:
            curr = self.st[-1]                                      # peek//store it to not lose it
            nextE = next(curr,None)                                 # store 

            if not nextE:                                           # if iteration on top of stack has no elements left
                self.st.pop()
            else:
                if nextE.isInteger():                               # its an Integer
                    self.nextEl = nextE
                    return True
                else:                                               # its a list
                    self.st.append(iter(nextE.getList()))           # add the list on top of stack and iterate 
        return False