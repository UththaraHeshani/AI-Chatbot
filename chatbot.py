import re
import long_responses as long

def message_Probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_word=True
    
    #Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty+=1

    #Calculate the percent of recognised words in a user message
    percentage=float(message_certainty)/float(len(recognised_words))     

    for word in required_words:
        if word not in user_message:
            has_required_word=False
            break

    if has_required_word or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_Probability(message,list_of_words,single_response,required_words)

    #Response ....................................
    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response('I\'m doing fine, and you?',['how','are','you','doing'],required_words=['how'])
    response('Thank you!',['i','love','code','palace'],required_words=['love'])
    response('Nice name',['my','name','is',' '],required_words=['name'])
    response('Certainly! What genre are you in the mood for? I can suggest some great films based on your preferences.',['tell','good','movie',' '],required_words=['movie','good'])
    response(' Im sorry, I dont have real-time data. You can check a weather website or app for the latest updates.',['what','is','the','weather'],required_words=['weather'])
    response('Why dont scientists trust atoms? Because they make up everything!',['tell','me','a','joke'],required_words=['joke'])
    response('I dont have personal preferences, but Im here to help with any questions you have.',['what','is','your','favourite'],required_words=['your','favourite'])
    response(' Im just a computer program, but Im here and ready to assist you!',['how','are','you','doing'],required_words=['how'])
    response('Great! Checking the weather for ... It looks like the current temperature is 25°C with clear skies. Is there anything else you like to know?',['I m', 'in'],required_words=['in'])
    response('Im just a chatbot so I cant sing',['sing','a','song'],required_words=['song'])
    response('just like you',['you','are','a','idiot'],required_words=['idiot'])
    response('Drink water, take a break, or rest in a quiet, dark room. If the headache persists, consider over-the-counter pain relievers.',['I','have','a','headache.'],required_words=['headache'])
    response(long.R_EATING,['what','you','eat'],required_words=['you','eat'])
    

    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match]< 1  else best_match                  

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response
while True:
    print('Elysia: ' + get_response(input('You: ')))