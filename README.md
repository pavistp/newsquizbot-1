# newsquizbot
## Team mates:
  1. 19pa1a0562- Juttiga Mounika
  2. 19pa1a0564- kalla Bala Anusha
  3. 19pa1a0532- Chikkala Pavitra
  


a bot using python

## Objective of the news-quiz bot :

Quiz helps us to gain knowledge. Most of the compititive exams asks general questions, so it makes practice for them with in hands.No need to refer to websites. It makes us feel intreseted to continue knowing answers.
                As everyone now a days have their own busy schedule, there is no time to go through the news and newspappers.By this bot every one can get the news over the country with in seconds and there is no need to spend special time or even no need to carry newspapper any where. You can easily go through the news through the mobile or laptop.
                So it may be usefull for most of us and may be this is the only way in the future to go through the news.
            
## What news-quiz bot will do:
1. The quizbot starts with a welcome msg and asks for the person's name  
2. Next, the quizbot choice the option between[1-2] .The bot terminates if the choice is not between[1-2]
3. If the person selects the first option then quiz will start
   1. The quizbot suggests some topics to the person to take quiz
   2. After selecting the topic, the quizbot asks for the no. of question the person want to attempt the quiz
   3. Then the quiz will start
   4. After attempting all the questions the quizbot shows how many answers are correct and for wrong answers it will show the correct answers
   5. If the person want to continue the quiz then again the process from step - 1 will continue  else the chatbot ends with a msg... 
4. If the person select the second option then news will start
   1. Initially the  news_bot  asks  for  the  country's  code
   2. Then the bot shows some articles of the new
   3. The news_bot asks for the interested article to know extension
   4. Next the news_bot asks  whether to  continue to see another article if 'yes' (step 3) will continue else the news_bot asks whether to see another contry news
   5. If yes (step - 5) will continue else the news_bot terminates  
 ## Block diagram     
![Block diagram](https://github.com/pavistp/newsquizbot/blob/main/ss%20for%20ml.png)

## Video of demo for the news-quiz:
click the link to watch the video: <iframe width="560" height="315" src="https://www.youtube.com/embed/WlK4MbtL9TI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## websites we reffered to do this bot:
we went through some websites regarding the below mentioned uses.
1. cprint to make the output colorfull 
2. For news we went through the news api http://newsapi.org/v2/top-headlines?country=country&category=business&apiKey=72d6e0915737435d805d05ff0cda7cc0
3. Imported request package to use the api.
