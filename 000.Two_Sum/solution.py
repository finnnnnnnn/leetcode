#!python3

def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j

if __name__=="__main__":
    nums=[2,7,11,15]
    target=9
    assert(twoSum(nums,target)==(0,1))
    print(twoSum(nums,target)==(0,1))
