class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []
        # time = (target - position)/speed
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        print(pairs)
        pairs.sort(reverse=True)
        for i in range(len(position)):
            pos,spd = pairs[i]
            time = (target - pos)/spd
            if not stack or time>stack[-1]:
                stack.append(time)
                print(stack)
        return(len(stack))
            
            
