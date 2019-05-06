#Write a function that takes a positive integer and returns the
#next smaller positive integer containing the same digits.

#For example:

#next_smaller(21) == 12
#next_smaller(531) == 513
#next_smaller(2071) == 2017
#Return -1 (for Haskell: return Nothing), when there is no smaller
#number that contains the same digits. Also return -1 when the
#next smaller number with the same digits would require the
#leading digit to be zero.

#next_smaller(9) == -1
#next_smaller(135) == -1
#next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
#some tests will include very large numbers.
#test data only employs positive integers.


def next_smaller(n):
    n_str=str(n)
    for index in range(len(n_str)-1, -1, -1):
        temps=[(int(n_str[i]), i) for i in range(index+1, len(n_str)) if int(n_str[i])<int(n_str[index])]
        if len(temps)==0: continue
        temps=sorted(temps, key=lambda x:x[0], reverse=True)

        pivot, j=temps[0][0], temps[0][1]
        new_temp=n_str[0:index]+str(pivot)+"".join(sorted(n_str[index:j]+n_str[j+1:], reverse=True))
        if new_temp[0]=='0':
            return -1
        elif (int(new_temp)<n):
            return int(new_temp)
    return -1
