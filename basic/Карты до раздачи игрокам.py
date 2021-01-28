import random


class Card(object):

    def __init__(self,data=None,data1=None,data2=None):
        data=data if data else []
        data1 = data1 if data1 else []
        data2 = data2 if data2 else []
        self.data=data
        self.data1=data1
        self.data2=data2
        self.columns=4  # 4 масти
        self.rows=9    #  9 карт



    def print1_matrix(self):   #  Печать матрицы с форматом строки
        #   Показываем то,как колода карт описана в игре
        print("Матрица для игры в дурака")
        for i in range(0,self.columns):
            row = ""
            for j in range(0,self.rows):
                x = self.data[i][j]
                x_formated  = f"{x:>8}"
                row = row + x_formated
            print(row)



    def cell(self,cell):    #  определение названия карты из матрицы по номеру карты

        if cell == 16:
            cell = "6 вини       "
        if cell == 17:
            cell = "7 вини       "
        if cell == 18:
            cell = "8 вини       "
        if cell == 19:
            cell = "9 вини       "
        if cell == 110:
            cell = "10 вини      "
        if cell == 111:
            cell = "Валет вини   "
        if cell == 112:
            cell = "Дама вини    "
        if cell == 113:
            cell = "Король вини  "
        if cell == 114:
            cell = "Туз вини     "
        if cell == 26:
            cell = "6 черви      "
        if cell == 27:
            cell = "7 черви      "
        if cell == 28:
            cell = "8 черви      "
        if cell == 29:
            cell = "9 черви      "
        if cell == 210:
            cell = "10 черви     "
        if cell == 211:
            cell = "Валет черви  "
        if cell == 212:
            cell = "Дама черви   "
        if cell == 213:
            cell = "Король черви "
        if cell == 214:
            cell = "Туз черви    "
        if cell == 36:
            cell = "6 крести     "
        if cell == 37:
            cell = "7 крести     "
        if cell == 38:
            cell = "8 крести     "
        if cell == 39:
            cell = "9 крести     "
        if cell == 310:
            cell = "10 крести    "
        if cell == 311:
            cell = "Валет крести "
        if cell == 312:
            cell = "Дама крести  "
        if cell == 313:
            cell = "Король крести"
        if cell == 314:
            cell = "Туз крести   "
        if cell == 46:
            cell = "6 Буби       "
        if cell == 47:
            cell = "7 Буби       "
        if cell == 48:
            cell = "8 Буби       "
        if cell == 49:
            cell = "9 Буби       "
        if cell == 410:
            cell = "10 Буби      "
        if cell == 411:
            cell = "Валет Буби   "
        if cell == 412:
            cell = "Дама Буби    "
        if cell == 413:
            cell = "Король Буби  "
        if cell == 414:
            cell = "Туз Буби     "
        return cell
        cell1=cell
        return cell1


    def print_all_Card(self):  # Печать матрицы   (КОЛОДА  КАРТ )
        #  Просто   печать карт  с определением масти
        print("   Колода карт :")
        for i in range(0,self.columns):
            row = ""
            for j in range(0,self.rows):
                cell = self.data[i][j]
                cell1 = self.cell(cell)
                row=row+cell1+"     "
            print(row)




    def shuffle(self):   #    Перемешиваем колоду 
        print(" перемешиваем хорошенько ")
        for i in range(1,100):
             #       генерируем две ячейки в колоде и меняем местами их содержимое
             #       и  так 100 раз, думается достаточно  )))
            x = random.randint(0,self.columns-1)
            y = random.randint(0,self.rows-1)
            qqq=self.data[x][y]
            sss=self.data[x][y]
            n= random.randint(0,self.columns-1)
            m = random.randint(0,self.rows-1)
            eee=self.data[n][m]
            self.data[x][y]=self.data[n][m]
            self.data[n][m]=sss




    def random_cards(self):    #  Вытаскиваем случайную карту--  КОЗЫРЬ
        print ( " Сегодня козырь :")
        #  Генерируем случайную ячейку в матрице-колоде
        x = random.randint(0,self.columns-1)
        y = random.randint(0,self.rows-1)
        cell=self.data[x][y]

        cell1=self.cell(cell)
        print(cell1)
        return cell1



    def input_players (self):
        #  ввод количества игроков с проверкой
        players = ""
        print("давай определимся на сколько игроков раздаём карты ")
        print("поскольку один не играет,а в шестером не остаётся колоды, то оптимально  от 2 до 5 ))  ")
        while ((not players.isdigit()) or (int(players) <2) or (int(players) > 5 )):
            players = input(" ВВедите количество игроков (от 2 до 5 )  = ")
            if (not players.isdigit()):
                print("." * 27 + " ВВедите цифру !!!! ")
        players = int(players)
        print( f" Раздаём колоду на {players} игроков")
        return players




    def six_card (self):   #  Извлекаем 6 случ карт из колоды
        igrok = []
        s=0
        sss=0
        for i in range(0,36):   #   цикл на извлечение 36 карт
                                #     Генерируем случайную ячейку-карту
            x = random.randint(0,self.columns-1)
            y = random.randint(0,self.rows-1)
            qqq=self.data[x][y]

            if (qqq!=0) and (s!=6):   #  Если  ячейка не 0 ( есть карта)  то извлекаем
                igrok.append(qqq)     #   Создаём список из шести карт
                self.data[x][y]=sss   #   Зануляем ячейку  из которой извлекли карту
                s=s+1                 #   счётчик карт
        return igrok



    def players_card(self,ppp,s):      #       Форматированный вывод карт у игрока
        p1111=[]
        for i in range (0,6):
            p11 = ppp[i]
            p111=self.cell(p11)   #  Определяем тип карты
            p1111.append(p111)    #  Формируем  строку
        print(130 * "+")
        print(f" Карты у  игрока  номер { s}")
        print(p1111)
        print(130 * "+")





def main():
    #  первая цифра-масть 1-вини.2-черви.3-крести.4-буби
    # следующие цифры-карта(11-валет.12-Дама.13-король.14-туз
    #   Пока пусть так будет матрица колоды, потом переделаю )))
    card=Card(data=[[16,17,18,19,110,111,112,113,114] ,[26,27,28,29,210,211,212,213,214],
              [36,37,38,39,310,311,312,313,314] ,[46,47,48,49,410,411,412,413,414]])

    card.print1_matrix()   #   Печатаем колоду
    print(130*"+")
    card.print_all_Card()  #    Печатаем колоду
    print(130*"+")
    card.shuffle()         #    Перемешиваем

    print(130*"+")
    card.print_all_Card()  #     Печатаем колоду
    print(130 * "+")
    kozir=card.random_cards()     #  козырь


    print(130*"=")
    s=card.input_players()  #   ввод количества игроков

    if (s>=2):                        #    Вывод   карт у   игроков  1 и 2
        player1 = card.six_card()
        card.players_card(player1,1)
        player2 = card.six_card()
        card.players_card(player2,2)

    if (s>=3):                         #    Вывод   карт у   игроков  1 , 2 ,3
        player3 = card.six_card()
        card.players_card(player3, 3)
    if (s>=4):                         #    Вывод   карт у   игроков  1 , 2  ,3 ,4
        player4 = card.six_card()
        card.players_card(player4, 4)
    if (s>=5):                         #    Вывод   карт у   игроков  1 ,2 ,3  ,4 ,5
        player5 = card.six_card()
        card.players_card(player5, 5)





main()








