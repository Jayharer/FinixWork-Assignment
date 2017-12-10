def main():
    output_list =[]
    master_list = []
    try:
       test_count = int(input())
       while (test_count > 100 or test_count < 1):
           test_count = int(input("errr in input test_counnt... try again:"))

       data_list = []
       for k in range(0, test_count):
           card_count = int(input())
           while (card_count > 10 or card_count < 1):
               card_count = int(input("errr in input card_count... try again:"))
           for j in range(0, card_count):
               str = input()
               str = str.strip(" ")  # remove beg and end blank spaces
               str = str.lower()  # convert into lower case
               while (len(str) > 100 or check_letter(str)):
                   str = input("err in input card name... try again:")

               if str not in data_list:
                   data_list.append(str)
           master_list.append(data_list)
           data_list = []
       print(master_list)
    except :
        print("err in input data")

    for data in master_list:
        result = cost(data)
        output_list.append(result)

    for j in range(0,len(output_list)):
        print("case#",j+1,":",output_list[j])

def check_letter(str):
    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']
    index = 0
    str = list(str)
    #print(str)
    for index in range(0, len(str)):
        if str[index] not in data:
            return True
    #print("index:", index)
    #print("length", len(str))
    if index == (len(str) - 1):
        return False


def cost(data):

   data_length = len(data)
   count = 0
   for j in  range(1,data_length) :
     key = data[j]
     i = j-1
     if(data[i]>key):
        count = count +1
     while( i>=0 and data[i]> key):
       data[i+1] = data[i]
       i = i-1
     data[i+1] = key
   return count

main()