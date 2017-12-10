def main():
    data_list =[]
    output_list =[]
    try:
       test_count = int(input())
       while (test_count > 100 or test_count < 1):
           test_count = int(input("errr in input test_counnt... try again:"))
       for k in range(0, test_count):
           str = input()
           str = str.strip(" ")           # remove beg and end blank spaces
           str = str.lower()              # convert into lower case
           while (len(str) > 5 or len(str) <1 or check_letter(str)):
               str = input("err in input string...  try again:")

           data_list.append(str)
    # print(data_list)
    except :
        print("err in input data")

    for data in data_list:
        result = pattern_Count(data)
        output_list.append(result)

    for j in range(0,len(output_list)):
        print("case#",j+1,":",output_list[j])



def check_letter(str):
    data =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index = 0
    str = list(str)
    #print(str)
    for index in range(0,len(str)):
        if str[index] not in data:
            return True
    #print("index:",index)
    #print("length",len(str))
    if index == (len(str)-1):
           return False

def pattern_Count(word):
    word_length = len(word)
    if(word_length == 1):
          return 1
    elif(word_length == 2):
        result = All_combination_length2(word)
        l1=set(result)
        return (len(l1))
    elif(word_length == 3):
        result = All_combination_length3(word)
        # check every element in result that satisfied pattern
        result = set(result)
        final_result =[]
        for data in result:
            if(  (data[0]== word[0] or data[0]== word[1]) and (data[1]== word[0] or data[1]== word[1] or data[1]== word[2]) and (data[2]== word[1] or data[2]== word[2]) ):
               final_result.append(data)
        #print(final_result)
        return (len(final_result))

    elif (word_length == 4):
        result = All_combination_length4(word)
        # check every element in result that satisfied pattern
        result = set(result)
        final_result = []
        for data in result:
            if ((data[0] == word[0] or data[0] == word[1]) and (data[1] == word[0] or data[1] == word[1] or data[1] == word[2]) and (data[2] == word[1] or data[2] == word[2] or data[2] == word[3]) and (data[3] == word[2] or data[3] == word[3])):
                final_result.append(data)
       #print(final_result)
        return (len(final_result))


    elif(word_length == 5):
        result = All_combination_length5(word)
        result = set(result)
        final_result = []
        for data in result:
            if ((data[0] == word[0] or data[0] == word[1]) and ( data[1] == word[0] or data[1] == word[1] or data[1] == word[2]) and ( data[2] == word[1] or data[2] == word[2] or data[2] == word[3]) and  ( data[3] == word[2] or data[3] == word[3] or data[3] == word[4]) and ( data[4] == word[3] or data[4] == word[4])):
                final_result.append(data)
        #print(final_result)
        return (len(final_result))
    else:
        print("error in data")





def All_combination_length2(word):
    result =[]
    new_word= word[0] + word[1]
    result.append((new_word))
    new_word = word[0] + word[0]
    result.append((new_word))
    new_word = word[1] + word[0]
    result.append((new_word))
    new_word = word[1] + word[1]
    result.append((new_word))
    return result

def All_combination_length3(word):
    result =[]
    substr = word[:2]
    temp_list1 = All_combination_length2(substr)
    substr = word[1:]
    temp_list2 = All_combination_length2(substr)
    final_list = set(temp_list1+ temp_list2)
    # print("final list",final_list)
    # find out all possible combination of word length 3
    for data in final_list:
        new_word = word[0]+ data
        result.append((new_word))
        new_word = word[1] + data
        result.append((new_word))
        new_word =  data + word[2]
        result.append((new_word))
        new_word = data + word[1]
        result.append((new_word))
    return result





def All_combination_length5(word):
    result = []
    substr1 = word[:2]
    temp_list1 = All_combination_length2(substr1)
    substr2 = word[2:]
    temp_list2 = All_combination_length3(substr2)
    for data1 in temp_list1:
       for data2 in temp_list2:
           new_word = data1 + data2
           result.append(new_word)

    substr1 = word[3:]
    temp_list1 = All_combination_length2(substr1)
    substr2 = word[:3]
    temp_list2 = All_combination_length3(substr2)
    for data2 in temp_list2:
        for data1 in temp_list1:
            new_word = data2 + data1
            result.append(new_word)

    substr2 = word[1:4]
    temp_list2 = All_combination_length3(substr2)
    for data in temp_list2:
        new_word = word[0] + data + word[4]
        result.append(new_word)
        new_word = word[0] + data + word[3]
        result.append(new_word)
        new_word = word[1] + data + word[4]
        result.append(new_word)
        new_word = word[1] + data + word[3]
        result.append(new_word)

    substr1 = word[1:]
    temp_list1 = All_combination_length4(substr1)
    for data in temp_list1:
       for j in range(0,2):
           new_word = word[j]+ data
           result.append(new_word)

    substr1 = word[:4]
    temp_list1 = All_combination_length4(substr1)
    for data in temp_list1:
        for j in range(3,5):
            new_word =  data + word[j]
            result.append(new_word)


    return result

def All_combination_length4(word):
    result = []
    substr1 = word[1:]
    temp_list1 = All_combination_length3(substr1)
    for data in temp_list1:
        for i in range(0,2):
          new_word = word[i] + data
          result.append(new_word)

    substr1 = word[0:3]
    temp_list1 = All_combination_length3(substr1)
    for data in temp_list1:
        for i in range(2,4):
            new_word = data + word[i]
            result.append(new_word)

    substr = word[:2]
    temp_list1 = All_combination_length2(substr)
    substr = word[2:]
    temp_list2 = All_combination_length2(substr)
    for data1 in temp_list1:
        for data2 in temp_list2:
            new_word = data1 + data2
            result.append(new_word)

    substr2 = word[1:3]
    temp_list2 = All_combination_length2(substr2)
    for data in temp_list2:
        new_word = word[0] + data + word[3]
        result.append(new_word)
        new_word = word[0] + data + word[2]
        result.append(new_word)
        new_word = word[1] + data + word[3]
        result.append(new_word)
        new_word = word[1] + data + word[2]
        result.append(new_word)

    return result

main()

