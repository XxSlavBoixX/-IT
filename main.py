from  random import choice

print("Правила Игры:")
print("Задаётся случайное число из существующего списка, твоя задача - его угадать. ")
print("Ты это можешь делать постепенно (буквами) а можешь попытать удачу и сделать всё разом! (целым словом).")
print("Игра ведётся через консоль, для выбора метода гадания необходимо ввести с (слово) или б (буква), а затем, набирайте вашу букву/слово и жмите enter!")
print("У вас ограниченое количество жизней, жизнь отнимается при неравильно угаданой букве или слове, но если у вас никак не получается угадать, вы ")
print("можете выбать метод слова и туда ввести команду help_me (выводит первую букву слова и убирает попытку) а можете ввести dev_cheat_#1 (Выводит всё слово). Приятной игры!") 

z = ["мороженное", "подвал", "поля", "работа", "пельмени","билли", "школа", "машина", "мышка", "клавиатура", "попугай", "котики", "бананы", "мартышка", "гамак", "леденец", "бутылка", "котлета", "карабин", "пушка", "пистола", "ДИО", "крестоносцы", "египет", "вампир", "авдол", "полнарефф", "джосеф", "джотаро", "какьёин", "игги"] #создаём список из которого будет браться рандомное слово
a = 9
x = choice(z).lower()
y = x
x = list(x)
print("Игра Поле Чудес, удачи!")
u = ""
win = False
zv = z
u = len(x) #создаём всякие переменные
while a != 0:
    print("Твои жизни:", a)
    print("Слово:", u * "*")
    print("Будите угадывать слово или букву?")
    print("[с] Слово")
    print("[б] Буква") #гадание словом или буквами?
    var = input("Ты выбрал: ")
    if var not in "ёЁйЙцЦуУкКеЕнНгГшШщЩзЗхХФфыЫвВаАпПрРоОлЛдДжЖэЭяЯчЧсСмМиИтТьЬбБюЮ":
        print("Введите русскую букву, a не что то иное")
    if var == "с":
        var2 = input("Слово(пишите буквы через пробел): ").lower() #input слова
        if var2 == y:
            print("Победа! G G") #выйгрыш
            won = True
            break #завершение при победе
        if var2 == "help_me":
            print(x[0])
        if var2 == "dev_cheat_#1":
            print(x) #вспомогательные команды
        else:
            print("-1 жизнь :(") #вычитание жизни при ошибке
            a -= 1 #
    if var == "б":
        var2 = input("Буква: ").lower() #выбор метода "буква"
        if var2 in x:
            for c in range(len(x)):
                if var2 == x[c]:
                    u[c] = var2 
        else:
            print("Этой буквы/слова в загаданном слове нет")
            a -= 1 #проверка введённого слова и при ошибки вычитание жизни
        if u == x :
            win = True
            break #выигрыш и завершение игры
if win == True:
    print("Слово угадано! Победа! G G") #поздравления и т.д
else:
    print("Попытки исчерпаны, загаданное слово - ", y, "Yare yare daze, better luck next time...")

