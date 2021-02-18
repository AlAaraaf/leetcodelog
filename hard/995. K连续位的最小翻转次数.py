## 暴力贪心
## 从左到右逐个翻转0，直到最后（n-k,n）位检查是否还存在0，结束
## (for i in range(1,n))(minflip(i-1)+whetherflip(i))
## 最费时的是每次都修改k个位置上的数值，时间复杂度为O(K*N)
class Solution:
    def minKBitFlips(self, a:'List[int]', k: 'int') -> 'int':
    n = len(a)
    flipnums = 0
    for i in range(0,n-k+1):
        if (a[i] == 0):
        for j in range(i, i+k):
            a[j] ^= 1
        flipnums += 1
        
    for i in range(n-k+1, n):
        if a[i] == 0:
            return -1
    return flipnums

## 贪心+滑动区间
## 由于 1 ^ 1 = 0, 0 ^ 1 = 1，可以用此规律代替翻转修改过程，并记录每个数位上翻转之后的数值
## 每个位置上翻转后的数值 = （影响该位置的前置位翻转次数flipsum + 该位置的原数值a[i]) % 2
## flipsum为一个滑动区间内的翻转次数和
## 每向前滑动一位，需要修改flipsum数值（队列原理）
class Solution:
    def minKBitFlips(self, a:'List[int]', k: 'int') -> 'int':
        n = len(a)
        pref = [0 for i in range(0,n)]
        flipnums = 0
        indp = 0
        flipsum = 0
        
        for i in range(0, n-k+1):
            if (flipsum+a[i])%2 == 0:
                flipnums += 1
                flipsum += 1
                pref[i] = 1
            if i-k+1 >= 0:
                flipsum -= pref[i-k+1]
        
        for i in range(n-k+1, n):
            if (flipsum+a[i])%2 == 0:
                return -1
            if i-k+1 >= 0:
                flipsum -= pref[i-k+1]
            
        return flipnums
