import requests
from termcolor import cprint,colored
import colorama
from colorama import Fore
colorama.init()
def inputs(country):
    r = requests.get('http://newsapi.org/v2/top-headlines?country='+country+'&category=business&apiKey=72d6e0915737435d805d05ff0cda7cc0')
    c =r.json()['totalResults']
    while(c==0):
        country = input(Fore.RED+"Enter the valid country code :")
        r = requests.get('http://newsapi.org/v2/top-headlines?country='+country+'&category=business&apiKey=72d6e0915737435d805d05ff0cda7cc0')
        c =r.json()['totalResults']
    return r
def news_intrested(country):
    r = inputs(country)
    l = len(r.json()['articles'])
    for i in range(0,l):
        cprint(f"{i+1} {r.json()['articles'][i]['title']}  ",'green')
def news_bot():
    print()
    country=input("Enter the country code of the news you are intrested in: ")
    inputs(country)
    news_intrested(country)
    print()
    number = int(input("Enter the number of the news which you are interested to know in extension :"))
    try:
        def extended_news(number,country):
            r = inputs(country)
            print()
            cprint(f"DESCRIPTION OF THE NEWS : {Fore.WHITE+r.json()['articles'][number-1]['description']}  ","cyan")
            print()
            cprint(f"CONTENT OF THE NEWS: {Fore.WHITE+r.json()['articles'][number-1]['content']}  ","cyan")
            print()
            cprint(f"To get more information visite the WEBSITE :{Fore.YELLOW+r.json()['articles'][number-1]['url']}  ",'cyan')
            print()
            cprint(f"It was PUBLISHED ON: {Fore.WHITE+r.json()['articles'][number-1]['publishedAt']}  ",'cyan')
            print()
            cprint("-------***Do you want to know about any other news say yes or no****-------")
            print()
            boole = input()
            if(boole.lower()=="yes"):
                number1= int(input("Enter the number of the news you want to know about :"))
                extended_news(number1,country)
            else:
                print("-------***Do you want to know about any other country news say yes or no***-----")
                boole=input()
                if(boole.lower()=="yes"):
                    country1 = input("Enter the country code:")
                    inputs(country1)
                    news_intrested(country1)
                    number2= int(input("Enter the news you are interested in:"))
                    extended_news(number2,country1)
                else:
                    print()
                    cprint("Thanks for showing interest in watching news from our bot. please visit again  ","yellow")
        extended_news(number,country)
    except Exception:
        cprint("Enter valid number :",'red')
        num = int(input())
        extended_news(num,country)





