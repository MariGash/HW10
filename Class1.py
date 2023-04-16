##Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы: рост, огнеопасность, цвет.
##Класс обеспечивает выполнение методов (dr — экземпляр класса)
#экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту

#экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
#цвет меньший по алфавиту;
#рост - среднее арифметическое из двух округлённое до целого вниз,
#огнеопасность - большее из двух;

#из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
#огнеопасности прибавляется остаток от деления огнеопасности на число;

##Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
##значению атрибута огнеопасность;

#change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

##str- возвращает строку:
##Dragon with height «рост», flammability <огнеопасность> and color «цвет».

#repr- возвращaет строку:
#Dragon(‹рост>, <огнеопасность>, <цвет>)

#Пример
##dr = Dragon(69, 5, “brown™)
##dr1 = Dragon(69, 5, “gray")
##print (dr > dr1, dr != dr1, dr <= dr1)
##print(dr, dr1, sep="\n")
##print()

#dr.change_color("white")
#dr -= 23
#dr1 -= 2
#dr2 = dr+dr1
#print(dr, dr1, dr2, sep="\n")

#print(dr("Welcome")

#Вывод

#False True True
#Dragon with height 69, flammability 5 and color brown.
#Dragon with height 69, flammability 5 and color gray.

#Dragon with height 66, flammability 10 and color white.
#Dragon with height 35, flammability 6 and color gray.
#Dragon with height 50, flammability 10 and color brown.
##WelcomeWelcomeWelcomeWelcomeWelcome


class Dragon:
    def __init__(self, height, flammability, color):
        self.height = height
        self.flammability = flammability
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def __call__(self, string):
        return string * self.flammability

    def __str__(self):
        return f"Dragon with height {self.height}, flammability {self.flammability} and color {self.color}"

    def __lt__(self, other):
        return self.height < other.height or self.flammability < other.flammability or self.color < other.color

    def __le__(self, other):
        return self.height <= other.height or self.flammability <= other.flammability or self.color <= other.color

    def __eq__(self, other):
        return self.height == other.height or self.flammability == other.flammability or self.color == other.color

    def __gt__(self, other):
        return self.height > other.height or self.flammability > other.flammability or self.color > other.color

    def __ge__(self, other):
        return self.height >= other.height or self.flammability >= other.flammability or self.color >= other.color

    def __ne__(self, other):
        return self.height != other.height or self.flammability != other.flammability or self.color != other.color

    def __add__(self, other):
        new_height = (self.height + other.height) // 2
        new_flammability = self.flammability if self.flammability > other.flammability else other.flammability
        new_color = self.color if self.color < other.color else other.color
        return Dragon(height=new_height, flammability=new_flammability, color=new_color)

    def __isub__(self, value):
        self.height -= self.height // value
        self.flammability += self.flammability % value
        return self
    def __repr__(self):
        return f"Dragon ({self.height},{self.flammability},{self.color})"

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")

print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")

print(dr.height, dr.flammability, dr.color)
print(dr1.height, dr1.flammability, dr1.color)

print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")

print(dr("Welcome"))