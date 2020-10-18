import random                     # importing random
from datetime import datetime     # importing datetime for time
import colorama
from colorama import Fore,Back,Style     # importing colorama for font-color
import sys 
from termcolor import colored, cprint          
from questions import biodiversity,knowledge,computer,food,environment,indiaflims,plants,java,python,sports
from newsbot import news_bot
colorama.init()

"""
    This is a program for news and quiz bot ....

    1. The quizbot starts with a welcome msg and asks for the person's name  
    2. Next, the quizbot choice the option between[1-2] .The bot terminates if the choice is not between[1-2]
    3. If the person selects the first option then quiz will start
        3.1  The quizbot suggests some topics to the person to take quiz
        3.2  After selecting the topic, the quizbot asks for the no. of question the person want to attempt the quiz
        3.3  Then the quiz will start
        3.4 After attempting all the questions the quizbot shows how many answers are correct and for wrong answers it will show the correct answers
        3.5 If the person want to continue the quiz then again the process from step - 3.1 will continue  else the chatbot ends with a msg... 
    4. If the person select the second option then news will start
        4.1 Initially the  news_bot  asks  for  the  country's  code
        4.2 Then the bot shows some articles of the news
        4.3 The news_bot asks for the interested article to know extension
        4.4 Next the news_bot asks  whether to  continue to see another article if 'yes' (4.3) will continue else the news_bot aska whether to see another contry news
        4.5 If yes (step - 4.5) will continue else the news_bot terminates  

"""
def introduction():
    # declare some list of responses
    responses=["Hello, Welcome to our news-quizbot .I can help you to know about particular country news and to check your knowledge by attempting the quiz. May I know your name pls ?",
              "Hii, Welcome to mews-quizbot .I can help you to know about particular country news and  also attempt the quizes and acquire knowledge.Can I know Your name?"]
    print()
    # pick a responses at random 
    cprint(random.choice(responses),'yellow',end=" ")  # cprint is used for font-color of the text 
    return input()

def greeting_msg(name):
    msg=["Nice to meet you.Pls select the options you are interested in ['1. Quiz','2. News'] ",
        "Lets have some time together.Pls select the options you are interested in ['1. Quiz','2. News'] "]

    time=datetime.now()
    greeting="Good Morning"
    if(time.hour >= 12 and time.hour < 17):
        greeting = "Good Afternoon"
    elif(time.hour >= 17 and time.hour < 22):
        greeting = "Good Evening"
    elif(time.hour >= 22):
        greeting = "Hii, Thats too late"

    print(f"{greeting} {name},{random.choice(msg)}",end="  ")

    return input()

def topics():
    print()
    cprint("Here are some topics --- ",'magenta')
    print()
    # some topics to take quiz
    cprint("1.General knowledge",'cyan')
    cprint("2.Biodiversity",'cyan')
    cprint("3.About computer",'cyan')
    cprint("4.Food and Nutrition",'cyan')
    cprint("5.Environment",'cyan')
    cprint("6.IndiaFlims",'cyan')
    cprint("7.Plants",'cyan')
    cprint("8.JavaBasics",'cyan')
    cprint("9.PythonBasics",'cyan')
    cprint("10.sports",'cyan')

def selection(a):
    # users selection of the topic
    if(a=="1"):
        return knowledge()
    elif(a=="2"):
        return biodiversity()
    elif(a=="3"):
        return computer()
    elif(a=="4"):
        return food()
    elif(a=="5"):
        return environment()
    elif(a=="6"):
        return indiaflims()
    elif(a=="7"):
        return plants()
    elif(a=="8"):
        return java()
    elif(a=="9"):
        return python()
    elif(a=="10"):
        return sports()


def error_1():          # Error Handling 
    try:
        c=int(input("Please select the number of topic on which you want to take quiz  "))
        if(c>=1 and c<=10):
            return c
        else:
            print()
            cprint("Please select the number between [1-10]",'red')
            return 0
    except Exception as e:
        print()
        cprint("Sorry,I cant get u.PLease select the number between [1-10]",'red')
        return 0

def error_2():          # Error Handling 
    try:
        c=int(input("Please enter the no of question you want attempt  "))
        if(c>=1 and c<=10):
            return c
        else:
            print()
            cprint("Please select the number between [1-10]",'red')
            return 0
    except Exception as e:
        print()
        cprint("Sorry,I cant get u.PLease select the number between [1-10]",'red')
        return 0

def quizprocess(topic_selection,name):         # process of the quiz
    d=selection(str(topic_selection))
    l = []        # list for appending weather the user answers correct or wrong
    l1 = []         # list for appending correct answers for the question
    count,i = 0,1       
    print() 
    no_of_questions = error_2()
    while(no_of_questions == 0):
        no_of_questions = error_2()
    temp  = no_of_questions
    t = no_of_questions      # storing no_of_question in the variable t for iteration
    print()
    cprint("NOTE : Only one word answers are allowed eg-->> class otherwise it is consider as wrong as well as misspelled words",'red')
    print()
    cprint("--- Quiz is going to start ---",'magenta')
    print()
    while(t>0):
        c = random.choice(d[0])      # pick random question and store in c
        print(f"{i}. {c}",end="   ")
        i+=1
        index1 = d[0].index(c)              # Finding the index of the question
        answer = input()               # Answers from the user is stored in answer variablr
        ans_list = answer.lower().split(" ")
        if(d[1][index1].lower() in ans_list):  # checking whether the answers are correct or not
            count+=1
            l.append("correct")
            t-=1
        else:
            l.append("wrong x")
            l1.append(d[1][index1])
            t-=1
    print()
    cprint("------------------*****----------------------",'blue')
    print("quiz result :", f"{count}/{temp}")                # Shows the quiz marks
    if(count == temp):
        cprint(f"Congratulations!!   {name}. All questions are correct..",'yellow')
    else:
        cprint(f"Better luck next time {name}, {temp-count} answers are wrong....",'yellow')
    j=0
    for i in range(0,len(l)):                           # Shows the weather the answers are correct or wrong
        if(l[i] == "wrong x"):
            cprint(f"{i+1}. {Fore.RED+l[i]}",end=" ")               #Fore is used for font-color  along with cprint
            print("  --->>  correct answer --- ",l1[j])
            j+=1
        else:
            cprint(f"{i+1}. {Fore.GREEN+l[i]}",'white')
    cprint("-------------------****-----------------------","blue")
    print()
    print("Do u want to continue the quiz again 'yes' or 'no'?",end="  ") 
    if(input().lower() == "yes"):                                   
        quiz_bot(name)                                              # This will Continue the quiz again
    else:
        print()
        cprint("Thank you, for attempting the quiz.Hope you enjoyed lot.. bye",'green')   # ending msg
        print()

def quiz_bot(name):
    topics()
    print()
    topic_selection = error_1()
    while(topic_selection == 0):
        topic_selection = error_1()
    quizprocess(topic_selection, name)

def main():
    name = introduction()
    print()                              # giving cap between each line for clear understanding
    reply = greeting_msg(name)
    if(reply=="1"):
        quiz_bot(name)
    elif(reply=="2"):
        news_bot()
    else:
        print()
        cprint("Sry,I cant get you.Thanks for using news-quiz bot",'green')

main()
