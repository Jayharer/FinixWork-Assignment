def main():

  data_list = []
  output_list =[]
  try:
    test_count = int(input())
    while (test_count > 100 or test_count < 1):
        test_count = int(input("errr in input test_counnt... try again:"))
    for k in range(0, test_count):
        colleague_count = int(input())
        while (colleague_count > 10000 or colleague_count < 1):
            colleague_count = int(input("errr in input colleague_count... try again:"))

        raw_data = input()
        raw_data = raw_data.strip(" ")
        while (len(raw_data.split(" ")) != colleague_count):
            raw_data = input("err in input colleague count... try again:")
            raw_data = raw_data.strip(" ")

        data = raw_data.split(" ")
        for  j in range(0,len(data)):
             data[j] = int(data[j])

        data_list.append(data)

  except ValueError:
      print("err input cannot be parsed as an integer")

  print(data_list)
  for data in data_list:
        result = no_Of_Operation(data)
        output_list.append(result)

  for j in range(0,len(output_list)):
        print("case#",j+1,":",output_list[j])


def no_Of_Operation(list1):
    length = len(list1)
    count =0
    while(len(set(list1)) != 1):
      max_data = max(list1)
      min_data = min(list1)
      difference = max_data - min_data
      index_max = list1.index(max_data)

      if(difference >= 5):
          for j in range(0,length):
              if(j == index_max):
                  continue
              list1[j] = list1[j] + 5
      elif ( difference >= 2):
          for j in range(0, length):
              if (j == index_max):
                  continue
              list1[j] = list1[j] + 2
      else :
          for j in range(0, length):
              if (j == index_max):
                  continue
              list1[j] = list1[j] + 1
      count = count +1

    return count

main()