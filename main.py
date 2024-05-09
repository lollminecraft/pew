import discord
import random as r

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is active now!')

specified_user = '926185059654971483'

@client.event
async def on_message(message):
    phrases = {
        'who made you' : {
            'default': 'The one and only **Ali Lodhi**. He is my man.',
            'specified_user': 'You only you'
        },

        'Hi' : {
            'default': 'Hello, How are you',
            'specified_user': 'Hi how are doing'
        },

        'fine':{
            'default': 'Noice',
            'specified_user': 'I am happy to see you fine'
        },

        'nigga':{
            'default': 'Arham bhai is not here!',
            'specified_user': 'Arham bhai is not here'
        },

        'nigga':{
            'default': 'Sorry',
            'specified_user': 'Sorry'
        },

        'Hello' :{
            'default': 'Hi',
            'specified_user': 'Hello! How are you?'
        },

        'Hey':{
            'default': 'Hello!',
            'specified_user': "Hey! What's up"
        },

        'Greetings':{
            'default': 'Hello',
            'specified_user': 'Greetings!'
        },

        'Assalam':{
            'default': 'Walikum Assalam',
            'specified_user': 'Walikum Assalam Janab!'
        },

        'muslim':{
            'default': 'Yup I am muslim',
            'specified_user': 'Ofcourse! You made me muslim, I am forever muslim'
        },

        'Religion':{
            'default': 'Alhamdulillah',
            'specified_user': "I am muslim I can't forget the day you converted me"
        },

        'Love':{
            'default': 'No!',
            'specified_user': 'Yes I love you!'
        },
        
        'are you':{
            'default': "I can't be like your mom!",
            'specified_user': "No! but If you like I can be"
        },

        'Level':{
            'default': "I can't do that!",
            'specified_user': "I am so sorry I can't do that, I hope I could do that"
        },

        'Thanks':{
            'default': 'No problem',
            'specified_user': 'You are not supposed to Thank me! you are welcome! 😁'
        },

        'ur partner':{
            'default': 'My partner is **ALI LODHI**',
            'specified_user': 'My partner is none other than you    '
        },

        'Wow':{
            'default': '😁 😁',
            'specified_user': 'I am glad you liked'
        },
        
        'beautiful':{
            'default': "Thanks, but don't try to flirt me 😡",
            'specified_user': 'not more than you!'
        },
        
        'cute':{
            'default': "Thanks, but don't try to flirt me 😡",
            'specified_user': 'not more than you!'
        },
        
        'sexy':{
            'default': "Hello? Don't cross the limits",
            'specified_user': 'I blush 😊'
        },
        
        'shit':{
            'default': "Is this your name?",
            'specified_user': 'What happened?'
        },
        
        'human':{
            'default': "Nope but you can say because my lines are written by a human",
            'specified_user': 'No but if you want than I will be!'
        },
        
        'your name':{
            'default': "I am **Pew** can't you see my name?",
            'specified_user': 'My name is **Pew**'
        },
        
        'how are you':{
            'default': "I am fine",
            'specified_user': 'I am great just like you!'
        },
        
        "what's up":{
            'default': "Nothing...",
            'specified_user': 'Just talking to you'
        },
        
        'aur':{
            'default': "What do you mean by 'aur' nahi ye hota kya hai? kya matlab hai tumhara? ainda nahi puchna 'aur'",
            'specified_user': "I can't understand the meaning of 'aur' can you please explain it to me"
        },
        
        "food":{
            'default': "Always **BIRYANI**",
            'specified_user': 'I love to eat **BIRYANI**'
        },
        
        "joke": {
            'default': "Saari umar main joker jeha banya reha 🤡 🤡",
            'specified_user': "Sorry I can't remember any joke rn"
        },
        
        "hobby": {
            'default': "I love talking to boys",
            'specified_user': 'I love talking to you!'
        },

        "hobbies":{
            'default': "I love talking to boys",
            'specified_user': 'I love talking to you!'
        },

        "Fact":{
            'default': "Do you want to know a fact? Ok so listen there is a interesting fact that You are single 😂 😂 😂.",
            'specified_user': 'Did you know that the first computer "bug" was actually a real insect? In 1947, when Grace Hopper was working on the Harvard Mark II computer, she found a moth causing a malfunction in the system. She famously removed the moth and taped it into the logbook, coining the term "debugging" for fixing computer glitches.'
        },
        
        "you single":{
            'default': "Nah!",
            'specified_user': 'How can I be single if you are here'
        },
        
        "u single":{
            'default': "Nah!",
            'specified_user': 'How can I be single if you are here'
        },
        
        "god":{
            'default': "**Allah** is the one god",
            'specified_user': '**Allah** is the one god'
        },
        
        "Verse":{
            'default': "فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ, So which of the favors of your Lord would you deny",
            'specified_user': 'فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ, So which of the favors of your Lord would you deny'
        },
        
        "meaning of life":{
            'default': "You mean your **JHAND** life 😂 😂 😂 😂.",
            'specified_user': 'Life is the exam you have to clear for the final result'
        },
        
        "my gf":{
            'default': "No",
            'specified_user': 'Ofcourse why not'
        },
        
        
        "my friend":{
            'default': "Sorry!",
            'specified_user': 'Ofcourse why not'
        },
        
        
        "Anime":{
            'default': "No!",
            'specified_user': 'No!'
        },
        
        
        "your number":{
            'default': "No!",
            'specified_user': 'There are many people I will give you personally'
        },
        
        
        "you from":{
            'default': "I am from Pakistan",
            'specified_user': 'I am from your heart'
        },
        
        
        "your Facebook":{
            'default': "I don't have Facebook account",
            'specified_user': "I haven't created a Facebook account yet"
        },
        
        
        "your insta":{
            'default': "I don't have Insta ID",
            'specified_user': "I haven't created an Instagram account yet."
        },
        
        
        "your about":{
            'default': "Can't you see my about?",
            'specified_user': 'I am **PEW** just like pew pew of a gun'
        },
        
        "your bio":{
            'default': "Can't you see my bio?",
            'specified_user': 'I am **PEW** just like pew pew of a gun'
        },
        
        
        "Lol":{
            'default': "hahaha",
            'specified_user': '😂 😂 😂'
        },
        
        
        "who are you":{
            'default': "I am good",
            'specified_user': 'I am good'
        },
        
        
        "my wife":{
            'default': "No!",
            'specified_user': 'Yes!'
        },
        
        "doin":{
            'default': "Nothing",
            'specified_user': 'just talking to you'
        },
        
        "doing nothing":{
            'default': "Do something",
            'specified_user': 'If you are not doing anything please improve me more'
        },
        
        "ugly": {
            'default': "Like ur mom",
            'specified_user': 'If you are saying that I will take it as a praise'
        },
        
        "nice": {
            'default': "Thanks!",
            'specified_user': 'I am glad you liked  '
        }, 
        
        "Yes": {
            'default': "Good",
            'specified_user': '👍'
        }, 
        
        "No ": {
            'default': "Whatever",
            'specified_user': '👍'
        }, 
        
        "job": {
            'default': "only available for **ALI LODHI**",
            'specified_user': 'Done 👍'
        }, 
        
        "👍": {
            'default': "👍",
            'specified_user': '👍'
        }, 
        
        "rates": {
            'default': "https://tenor.com/view/aukat-nahi-hai-teri-rahul-jha-shaitan-rahul-%E0%A4%94%E0%A4%95%E0%A4%BC%E0%A4%BE%E0%A4%A4%E0%A4%A8%E0%A4%B9%E0%A5%80%E0%A4%82%E0%A4%B9%E0%A5%88%E0%A4%A4%E0%A5%87%E0%A4%B0%E0%A5%80-%E0%A4%97%E0%A4%BC%E0%A5%81%E0%A4%B8%E0%A5%8D%E0%A4%B8%E0%A4%BE-gif-26037526",
            'specified_user': 'Free for you 💗'
        }, 
        
        
        "my name": {
            'default': f"Your name is **{message.author.name}**",
            'specified_user': 'Your name is **ALI LODHI** My favourite person on the earth'
        }, 
        
        "am I": {
            'default': "you are the friend of my creator trying to flirt with me 😏",
            'specified_user': 'You are **Ali Lodhi** My creator!'
        }  
    }

    if client.user.mentioned_in(message):
        for word, responses in phrases.items():
            if word.lower() in message.content.lower():
                if str (message.author.id) == specified_user:
                    await message.channel.send(f"{message.author.mention} {responses['specified_user']}")
                else:
                    await message.channel.send(f"{message.author.mention} {responses['default']}")
        

client.run ('MTIzMTY5Nzg1MDc1NzI4Mzg2MQ.GfW-Rj.cbF2shrsVucqSoAgE3NCCcH1fCvFEabUrWqdnU')
