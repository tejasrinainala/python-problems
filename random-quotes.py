# This program displays a random quote from a list of quotes.





import random
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The unexamined life is not worth living. - Socrates",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The journey of a thousand miles begins with one step. - Lao Tzu"
]
print(F"Random quote of the day : {quotes[random.randint(0,len(quotes)-1)]}")

