import json
with open("DATAS.json", "r") as file:
    data = json.load(file)
print("welcome to admin mode")


def WRONG():
    print("there is something wrong !")


while True:
    try:
        QUEST = int(input("""1. for patients in an date
        2. know the information of an patient
        3. delete patient
        4. exit admin mode: """))
    except ValueError:
        print("you should enter an number !")
    else:

        if QUEST == 1:
            QUESTDATE = input("gave date: example(2 / august / 2026): ")
            if QUESTDATE in data:
                for KEY, VALUE in data[QUESTDATE].items():
                    print(KEY, ":", VALUE)
            else:
                WRONG()

        elif QUEST == 2:
            QUESTNAME1 = input("your patient name: ")
            for DATE in data:
                if QUESTNAME1 in data[DATE]:
                    print(data[DATE][QUESTNAME1])
                else:
                    WRONG()

        elif QUEST == 3:
            QUESTDATE2 = input("gave date: example(2 / august / 2026): ")
            if QUESTDATE2 in data:
                QUESTNAME2 = input("your patient name: ")
                if QUESTNAME2 in data[QUESTDATE2]:
                    del data[QUESTDATE2][QUESTNAME2]
                    with open("DATAS.json", "w") as file:
                        json.dump(data, file, indent=4)
                else:
                    WRONG()
            else:
                WRONG()
        elif QUEST == 4:
            print("Done !")
            break
