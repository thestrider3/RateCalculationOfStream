# RateCalculationOfStream
To calculate the rate of any streaming data

#####TASK APPOINTED
In this assignment, we were asked to calculate the rate of a stream of a data and to build an alerting system to know when the rate does something interesting. 
#####STORY BACKGROUND
For this assignment, I chose to analyze Indian citizen's reaction to the Jawaharlal Nehru University(JNU) row happening in India. Jawaharlal Nehru University is an acclaimed public central university in India. It is ranked as the second best public university in India by India Today magazine and has a rating of 3.9/4.0 which is the highest rating awarded to any university in India by the National Assessment and Accreditation Council.

On 9th Febuary, a cultural meeting was organized in JNU against the execution of Afzal Guru, a terrorist convicted for December 2001 attack on the Indian parliament, and Maqbool Bhat, a separatist leader as well as Kashmir's right to self-determination. It was alleged that during this meeting, “Anti-India” slogans were raised.

Following this incident, a furore broke out and it lead to the arrest of JNU Student's Union President Kanhaiya Kumar on the charges of sedition and criminal conspiracy according to Section 124 of the Indian Penal Code. This arrest further snowballed into a major political controversy with several political leaders and activists coming forward to support JNU students on the grounds of “Freedom of Speech” while others condemning it on the grounds of raising “Anti-Nationalist” slogans.

I decided to use this incident as my assignment topic. While this incident was occuring in India, there were several claims that these slogans were raised by Kashmiri students; so I wanted to analyze how people in Jammu and Kashmir are reacting to this event. I have not done any sentiment analysis to check how many people are supporting JNU or are against it. My aim to is just check the volume rate of tweets arising from this region and comparing it to that from rest of India.
##### DATA SOURCE USED
I have used Twitter Streaming API to gauge the volume of tweets in reaction to this incident.Twitter is a good source of obtaining public's view and is easy to implement. With its Streaming API, we can get any public tweets along with the meta data associated with the tweet. Despite its benefits, API has its own disadvantage of being difficult to filter relevant and irrelevant tweets.
##### TECHNOLOGY USED
I am writing this assigment in Python and I have used Redis database for storage purpose. Also, I have used Twitter Streaming API as the data source and finally made a Twitter bot to publish rates to my Twitter account @tulika92.
#####HOW TO RUN
*Replace your own Twitter Access Token, Secret Access token, API key and API Key Secret in twitter_getdata.py and avg.py

*Run redis-cli on your terminal

*Open another terminal and run python twitter_getdata.py | python delta.py | python insert. py | python avg.py
