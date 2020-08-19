from random import choice
from playsound import playsound

print('1. Warm up')
print()
print('What unusual ways to say hello do you know?')
playsound('lesson_1_Warm_up/What unusual ways to say hello do you know.mp3')
unusual_say_hello_dict = {"what's up?": 'no', "how's it going?": 'no', "howdy!": 'no', "greetings!": 'yes',
                          "look who it is!": 'no', "good day!": 'yes', "yo!": 'no', "how do you do?": 'yes'}
u_s_h_l = list(unusual_say_hello_dict.keys())

while u_s_h_l:
    say_hello = input("Input unusual ways to say hello: ").lower()
    if say_hello in u_s_h_l:
        print(f'yes {say_hello} is unusual ways to say hello, remained - {len(u_s_h_l) - 1}')
        u_s_h_l.remove(say_hello)

print('Bravo!')
print()

u_s_h_l = list(unusual_say_hello_dict.keys())
while u_s_h_l:
    say_hello = choice(u_s_h_l)
    playsound(f'lesson_1_Warm_up/{say_hello[:-1]}.mp3')
    if unusual_say_hello_dict[say_hello] == input(f'Do you think the greeting "{say_hello}" is formal?: ').lower():
        print(f'Yes, greeting "{say_hello}" is {"not" if unusual_say_hello_dict[say_hello] == "no" else ""} formal')
        u_s_h_l.remove(say_hello)
    else:
        print("The answer is not correct")
