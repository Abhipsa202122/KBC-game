def f():
    questions=["How many continents are there?","What is the capital of India?","NG mein kaun se course padhaya jaata hai?"]
    options=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counselling","tourism","agriculture"]]
    solution=[3,4,1]
    i=0
    c=0
    while i<len(questions):
        print(questions[i])
        print(options[i])
        user=int(input("enter no./option!"))
        if user==solution[i]:
           print("congratulations your answer is correct")
           c+=1
        else:
           print("your answer is wrong")
           options=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counselling","tourism","agriculture"]]
        i+=1
    if c==len(solution):
       print("you win")
    else:
       print("you looser")
f()       
         



