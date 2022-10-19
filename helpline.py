# random correct answer

from tkinter import *
import requests
import random
from matplotlib import pyplot as plt
from matplotlib import style

root = Tk()
root.title("ARE  YOU  GENIUS")
root.geometry("1300x500")

game_frame = Frame(root,bg="#4E4C45")
game_frame.place( relheight= 1 , relwidth = 1 )


url ="https://opentdb.com/api.php?amount=10&category=21&type=multiple"

response = requests.get(url)

data = response.json()


x = score = 0
help_1_con = help_2_con = help_3_con = TRUE



def questions_creator (y,op) :

    if op :

        global options , position_over , j , template_options , answer

        template_options = [data["results"][y]["correct_answer"],data["results"][y]["incorrect_answers"][0],data["results"][y]["incorrect_answers"][1],data["results"][y]["incorrect_answers"][2]]

        for index in range(4) :
            print("\n" + template_options[index])

        print("\n\n\n")

        options = [None]*4
        position_over = [None]*4
        j = 0

        def option_rand () :

            global j ,  position , options , answer

            position = random.randrange(4)

            for r in range(4) :

                if not(position_over[0] == None) and not(position_over[1] == None) and not(position_over[2] == None) and not(position_over[3] == None) :
                    break

                if position == position_over[0] or position == position_over[1] or position == position_over[2] or position == position_over[3] :
                    option_rand()

                else :
                    position_over[j] = position
                    options[j] = template_options[position]

                    if position == 0 :
                        answer = j

                    j += 1

        option_rand()

        for index in range(4) :
            print("\n" + options[index])

        print("\n\nANSER IS : " + options[answer] + "\n\n")

        display_q(globals()["x"])

    else :

        globals()["help_1_con"] = FALSE

        def funnn () :

            number = random.randrange(4)

            if number == answer or options[number] == " " :
                funnn()

            else :
                options[number] = " "

        for runner in range(2) :
            funnn()

        display_q(globals()["x"])


def retry_game () :

    global response , data , game_frame

    globals()["x"] = globals()["score"] = 0

    response = requests.get(url)

    data = response.json()

    game_frame = Frame(root,bg="#4E4C45")
    game_frame.place( relheight= 1 , relwidth = 1 )

    questions_creator(0,TRUE)


def claculation (ans) :

    if ans == answer :
        globals()["score"] += 10

    else :
        globals()["score"] -= 5

    if globals()["x"] < 9 :
        globals()["x"] += 1
        questions_creator(globals()["x"],TRUE)

    else :

        text = "\n\nFINAL SCORE IS \n" + str(globals()["score"])

        game_over_frame = Label(game_frame,bg="#10D979",fg="#4E4C45",text=text,font=("acme",20),justify=CENTER)
        game_over_frame.place( relheight= 1 , relwidth = 1  )

        retry_b =  Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",18),text="RETRY",command=retry_game)
        retry_b.place(relx=0.875 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )


def call_creator (caller) :

    globals()["help_3_con"] = FALSE

    heelp_3 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),command=lambda:call_creator(y),text="CALL",state=DISABLED)
    heelp_3.place(relx=0.875 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    call_text = "HEY !!\nI THINK THE\nANSWER IS\n\n" + options[answer]

    root_n = Tk()
    root_n.title("CALLING  FRIEND")
    root_n.geometry("300x300")

    game_frame_n = Frame(root_n,bg="#4E4C45")
    game_frame_n.place( relheight= 1 , relwidth = 1 )

    que_l = Label(game_frame_n,bg="#10D979",fg="#4E4C45",justify=CENTER,font=("acme",17),text=call_text)
    que_l.place(relx=0.05 ,rely=0.05 ,relheight=0.9 ,relwidth=0.9 )


def poll_creator (poller) :
    
    #globals()["help_2_con"] = False

    percentage = [0]*4
    bar_per = [None] * 4

    def divider (xx) :

        num = random.randrange(86)

        if xx :

            if xx == 3 :

                percentage[3] = 100 - (percentage[0]+percentage[1]+percentage[2])


            else :
            
                if percentage[0]+percentage[1]+percentage[2]+percentage[3]+num > 100 :
                    divider(xx)

                else :
                    percentage[xx] = num

        if xx == 0 :
            percentage[xx]  = num

    for xy in range(4) :

        divider(xy)


    bar_per[answer] = max(percentage)

    jc = False
    jr = True

    for res in range(4) :

        if res == answer :
            jr = False

        else :

            if percentage[res] == bar_per[answer] :
                jc = True
                pip =  res + 1

            bar_per[res] = percentage[res]

            if jc and jr :
                bar_per[res] = percentage[pip]
                pip += 1

                
                

    options_alp = ["a","b","c","d"]

    plt.ylabel("PERCENTAGE")

    plt.bar(options_alp,bar_per,color="#B152C4")

    plt.title("AUDIENCE CHOICE IS "+options[answer]+"\n")
    plt.legend()
    plt.show()



def display_q (y) :

    que_l = Label(game_frame,bg="#10D979",justify=CENTER,font=("acme",17),text=data["results"][y]["question"])
    que_l.place(relx=0.025 ,rely=0.2 ,relheight=0.2 ,relwidth=0.95 )

    ques_no = Label(game_frame,bg="#7FC9F1",justify=CENTER,font=("acme",15),text= str(y+1)+"/10" )
    ques_no.place(relx=0.025 ,rely=0.03 ,relheight=0.1 ,relwidth=0.08 )

    if globals()["help_1_con"] :
        help_1 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),text="50-50",command=lambda:questions_creator(y,FALSE))
        help_1.place(relx=0.575 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    else :
        help_1 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),text="50-50",command=lambda:questions_creator(y,FALSE),state=DISABLED)
        help_1.place(relx=0.575 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    if globals()["help_2_con"] :
        help_2 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),command=lambda:poll_creator(y),text="POLL")
        help_2.place(relx=0.725 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    else :
        help_2 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),command=lambda:poll_creator(y),text="POLL",state=DISABLED)
        help_2.place(relx=0.725 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    if globals()["help_3_con"] :
        help_3 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),command=lambda:call_creator(y),text="CALL")
        help_3.place(relx=0.875 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    else :
        help_3 = Button(game_frame,bg="#7FC9F1",activebackground="#128AC9",justify=CENTER,font=("acme",15),command=lambda:call_creator(y),text="CALL",state=DISABLED)
        help_3.place(relx=0.875 ,rely=0.03 ,relheight=0.1 ,relwidth=0.1 )

    opt_1 = Button(game_frame,bg="#0E9870",activebackground="#2EC3B1",justify=CENTER,font=("acme",18),text=options[0],command=lambda:claculation(0))
    opt_1.place(relx=0.025 ,rely=0.47 ,relheight=0.2 ,relwidth=0.45 )

    opt_2 = Button(game_frame,bg="#0E9870",activebackground="#2EC3B1",justify=CENTER,font=("acme",18),text=options[1],command=lambda:claculation(1))
    opt_2.place(relx=0.525 ,rely=0.47 ,relheight=0.2 ,relwidth=0.45 )

    opt_3 = Button(game_frame,bg="#0E9870",activebackground="#2EC3B1",justify=CENTER,font=("acme",18),text=options[2],command=lambda:claculation(2))
    opt_3.place(relx=0.025 ,rely=0.75 ,relheight=0.2 ,relwidth=0.45 )

    opt_4 = Button(game_frame,bg="#0E9870",activebackground="#2EC3B1",justify=CENTER,font=("acme",18),text=options[3],command=lambda:claculation(3))
    opt_4.place(relx=0.525 ,rely=0.75 ,relheight=0.2 ,relwidth=0.45 )


questions_creator(globals()["x"],TRUE)

root.mainloop()