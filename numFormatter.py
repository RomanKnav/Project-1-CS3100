

def numFormatter(num):
    # will need to use insert() to stop deletion
    numList = list(str(num))
    listLen = len(numList)
    
    # if we have even number of digits, add a "," every 3 digits
    if listLen % 3 == 0 and listLen > 3:
        
        for i in range(3, listLen, 4):

            numList.insert(i, ",")
            # print(i)

        print("".join(numList)) 
    # return numList

#print(numFormatter(10000000))
# numFormatter(100000)
# numFormatter(100000000)     # 100,000,000
# numFormatter(100000000000)

print("{:,}".format(1000))
print("{:,}".format(100000))
print("{:,}".format(10000000))
print("{:,}".format(100000000000))