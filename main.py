#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#coding=utf-8

import re 
# The first digit of the sum in the first 10 numbers gives the 11th digit.
def first_10_num_sum(str_len, the_last_number): 
    number_sum_to_ten = 0 
    sum_len = []
    for n in range(0,10):
        number_sum_to_ten += int(str_len[n])
    number_sum_to_ten = str(number_sum_to_ten)

    for n2 in range(0, len(number_sum_to_ten)):
        sum_len.append(number_sum_to_ten[n2])

    if int(the_last_number) == int(sum_len[1]):
        print("Second check is completed !")
    else: 
        print("There is the error that first number sum")
        exit(0)
def other_sum(str_len): 
    multi_7 = 0 
    multi_9 = 0 
    multi_8 = 0 
    total_sum_len = list()
    total_for_found_eleven=[]
    for n in range(0,len(str_len)):
        multi_7 = int(str_len[0])  +int(str_len[2]) +int(str_len[4])+int(str_len[6])+int(str_len[8])
        multi_9 = int(str_len[1])+int(str_len[3])+int(str_len[5])+int(str_len[7])
        multi_8=  int(str_len[0])+int(str_len[2])+int(str_len[4])+int(str_len[6])+ int(str_len[8])

    multi_7 = multi_7 * 7
    multi_9 = multi_9 * 9 
    multi_8 = multi_8 * 8
    multi_8 = str(multi_8)
    for i in range(0,len(multi_8)):
        total_for_found_eleven.append(multi_8[i])
    total_sum = multi_9 + multi_7
    total_sum = str(total_sum)
    for j in range(0,len(total_sum)):
        total_sum_len.append(total_sum[j])
    if  int(total_sum_len[-1]) == int(str_len[9]): 
        print("Third check is completed !")
    if int(total_for_found_eleven[-1]) == int(str_len[10]):
        print("Fourth check is completed ! ")

def number_sum(tcno):
    str_len = list()

    for i in range(0,len(tcno)):
        str_len.append(tcno[i])

    the_last_number = str_len[-1]
    first_10_num_sum(str_len,the_last_number)
    other_sum(str_len)

# length checking
def check_length_11(tcno): 
    if len(tcno) != 11: 
        print("tcno is wrong !!")
    else: 
        number_sum(tcno)

if __name__ == "__main__":
    print("the program is good")
    tcno = None 
    while True:
        tcno = input("please enter the tcno:\t")
        tcno = tcno.lower()

        # check that user does not enter the string variable
        # and tc's lenght is equl to 11
        if len(tcno) != 11:
            continue
        elif  re.search('[a-z]',tcno) is not None:
            continue
        else: 
            break
    print("First check is completed !")
    # number sum 
    number_sum(tcno)








