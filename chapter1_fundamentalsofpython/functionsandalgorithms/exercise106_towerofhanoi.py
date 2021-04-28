## The Tower of Hanoi is a well-known mathematical problem
# There are three disk stacks where the disks can be placed in, and n disks of different sizes.
# At the start of the game, the three disks are placed in one single stack in ascending order. You are asked to move the disks from one stack to another, by moving one disk at a time and are not allowed to place a disk on top of another disk, if it's larger than the one below it.


# We need to compute the minimum number of moves necessary to move the entire stack of n disks from one stack to another. This problem can become quite simpler when we apply recursive thought.
# In order to move n disks, we need to move the top n-1 disks to another stack, then the bottom disk, the biggest disk to the last stack, and finally move the n-1 disks in the other stack to the same stack as the biggest disk.
# If we imagine that we can compute the minimum number of steps taken to move (n-1) disks from one stack to another as S(n-1), then to move n disks, we need 2 * S(n-1) + 2 steps.

def solve(n):
    if n == 1:
        return 1
    return 2 * solve(n - 1) + 1

print(solve(3))
print(solve(3) == 2 ** 3 - 1)