class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        length = len(gas)
        start_i = 0
        end_i = 0
        
        def check(index) -> bool:
            curr_gas = 0
            for i in range(index, length):
                curr_gas += gas[i] - cost[i]
                if curr_gas < 0:
                    return False
            
            for i in range(0, index):
                curr_gas += gas[i] - cost[i]
                if curr_gas < 0:
                    return False
                
            return True
        
        def check2(index) -> bool:
            tmp_gas = gas[index:] + gas[:index] + [gas[index]]
            tmp_cost = cost[index:] + cost[:index] + [cost[index]]
            curr_gas = 0
            # print(tmp_gas, tmp_cost)
            for i in range(length):
                curr_gas += tmp_gas[i] - tmp_cost[i]
                if curr_gas < 0:
                    return False
            return True
        
        while True:
            if start_i >= length:
                return -1
            elif start_i + 1 < length:
                end_i = start_i+1
                g = gas[start_i] + gas[end_i]
                c = cost[start_i]
            elif start_i + 1 == length:
                end_i = 0
                g = gas[start_i] + gas[end_i]
                c = cost[start_i]
            print(f"[{start_i}] gas = {g}", "<" if g < c else ">", f"cost = {c}")
            if gas[start_i] + gas[end_i] > cost[start_i]:
                if check(start_i): return start_i
            start_i += 1

s = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gas = [2,3,4]
# cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))