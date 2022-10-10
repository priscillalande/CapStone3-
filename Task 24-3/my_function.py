


def days_weekdays():#Days of the week 
    print('Monday\nTuesday\nWensaday\nThursday\nFriday\nSaturday\nSunday')

days_weekdays()


def rep_helo(sentence):
    new_sentence = ""

    index = 0

    for word in sentence.split():

        if index % 2 == 1:
            new_sentence += "hello "#replacement by the word hello in every second word 
        else:
            new_sentence += word + " "

        index += 1

    # remove the last space at the end
    sentence = sentence[:-1]

    print(new_sentence)

sent = "my name is , and i love programming ."#Testing statement 
rep_helo(sent)