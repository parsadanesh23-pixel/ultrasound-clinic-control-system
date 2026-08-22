import json
with open("DATAS.json", "r") as file:
    data = json.load(file)
SONOS = ["abdomen", "kidny", "liver", "brain", "thyroid", "pregnancy"]
PRICES = [950000, 900000, 750000, 800000, 1100000, 1150000]
QUESTDAY = input("what is the day of this month: ")
QUESTMONTH = input("what is month: ")
QUESTYEAR = input("enter year: ")
FINAL = f"{QUESTDAY} / {QUESTMONTH} / {QUESTYEAR}"
data[FINAL] = {}
print("wish you an great workday !")
while True:
    QUEST = input("""enter patient name:
    type exit to end your day
    type: """).lower()
    if QUEST != "exit":
        for SONO, PRICE, NUMBER in zip(SONOS, PRICES, range(0, 6)):
            print(f"n.{NUMBER} / SONO: {SONO} / PRICE: {PRICE}")
        while True:
            try:
                QUESTSONO = int(input("gave the number of your sono: "))
            except ValueError:
                print("enter number !")
            else:
                if QUESTSONO >= 0 and QUESTSONO < 6:
                    data[FINAL][QUEST] = {"NAME": QUEST,
                                          "SONO": SONOS[QUESTSONO],
                                          "PRICE": PRICES[QUESTSONO],
                                          "DATE": FINAL
                                          }
                    with open("DATAS.json", "w") as file:
                        json.dump(data, file, indent=4)
                    print("process done !")
                    break
                else:
                    print("there is an problem !")
    if QUEST == "exit":
        break
