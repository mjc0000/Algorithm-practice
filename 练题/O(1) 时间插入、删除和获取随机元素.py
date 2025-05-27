class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.vsl_to_index={}

    def insert(self, val: int) -> bool:
        if val in self.vsl_to_index:
            return False
        self.nums.append(val)
        self.vsl_to_index[val]=


    def remove(self, val: int) -> bool:

    def getRandom(self) -> int:

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()