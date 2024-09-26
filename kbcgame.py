ques=[['what is the capital of punjab','chandigarh','patiyala','punjab','gioes',1],
      ['cpaital of india','delhi','goa','up','mp',1],
      ['leap year total days',365,364,363,366,4]]
level=[1000,2000,3000]
money=0
for i in range(0,len(ques)):
   #we are using list of list which just like a matrix 
   # to access question from the list of list we have used ques[i][1], 
   # because list has three lists in it, so first we will acess the sublist using [i]
   # then in the sublist to acess the question we will use the index of that specific ques which [1]
   # like ques[1][1] in the ques list at [1] we have ['what is the capital of punjab','chandigarh','patiyala','punjab','gioes',1] this sublist
   # in this sublist at index[0] we have thw main question 
    #print(f"question for Rs: {level[i]}")
    print(f"your question for Rs.{level[i]} is:\n {ques[i][0]}")
    print(f" a.{ques[i][1]}     b.{ques[i][2]}")
    print(f" c.{ques[i][3]}     d.{ques[i][4]}")
    reply = int(input("enter your answer from (1-4)"))
    if(reply==ques[i][5]):
        print("coreect answer!")
        print(f"you have won the Rs.{level[i]}")
        money+=level[i]
    else:
        print("wrong answer!")
print(f"total amount you won is: {money}")        