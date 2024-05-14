class StringBuilder():
    def __init__(self, str=""):
        self.__strings = [str] # hranate, protoze nevim kolik jich bude a ukladam tedy jako seznam

    def append(self, new_str):
        self.__strings.append(new_str)
        return self # vrati sebe a nakonec to buildem  vyplivnu

    def show_data(self):
        print(self.__strings)

    def build(self):
        result=""
        for str in self.__strings:
            result += str

        return result

sb = StringBuilder("Začátek")
sb.append("prostředek").append("prostředek2")
sb.append("konec.")
sb.show_data() # ted jen mrknu na ty data
sentence = sb.build() # shromazduji data a ted to vytisknu
print(sentence)

