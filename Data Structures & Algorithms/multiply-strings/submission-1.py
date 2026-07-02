class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if num1[0] == '0' or num2[0] == '0':
        #     return 0

        # total_num1 = 0
        # total_num2 = 0
        # for i in range(len(num1)-1, -1, -1):
        #     total_num1 += num1[i]*pow(10, len(num1)-1-i)
        
        # for j in range(len(num2)-1, -1, -1):
        #     total_num2 += num2[i]*pow(10, len(num2)-1-i)
        
        # total = total_num1*total_num2
    
        int_num1 = int(num1)
        int_num2 = int(num2)
        temp = int_num1*int_num2
        return str(temp)





        