class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        combine_list = []
        for i in range(len(position)):
            combine_list.append([position[i], speed[i]])
        
        combine_list.sort()
        last_car = combine_list[0]

        while len(combine_list) > 1:
            first_car = combine_list.pop()
            if first_car[0] > target:
                continue

            second_car = combine_list[-1] 
            if (target - first_car[0]) / first_car[1] >= (target - second_car[0]) / second_car[1]:   
                combine_list[-1] = first_car
            else:
                fleet += 1
            
        return fleet+1

                
        
        