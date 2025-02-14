# 牌的点数：在21点中，每张牌都有一个特定的点数。数字2至10的牌按照其面值计算点数，J、Q、K均计为10点，A可以计为1点或11点，具体取决于玩家的策略。
# 发牌：游戏开始时，发牌员给每位玩家和庄家各发两张牌。玩家的牌面朝上，而庄家的第一张牌面朝下（暗牌），第二张牌面朝上（明牌）。
# 要牌：玩家可以根据自己的手牌点数决定是否要牌。如果玩家选择要牌，发牌员会继续发一张牌给玩家。玩家可以多次要牌，直到停止要牌或手中的牌点数超过21点（爆牌）。
# 停牌：如果玩家认为手中的牌点数已经足够接近21点，可以选择停牌。此时，庄家需要揭示暗牌，并根据规则进行操作。
# 庄家的规则：庄家在游戏中必须遵循特定的规则。通常，庄家必须继续要牌，直到手中的牌点数达到17点或更高。在某些规则中，庄家可能在软17点（包含A的17点）时停牌。
# 胜负判定：在庄家和玩家都完成操作后，比较双方的手中的牌点数。如果玩家手中的牌点数更接近21点且不爆牌，则玩家获胜。如果庄家手中的牌点数更接近21点，则庄家获胜。如果双方手中的牌点数相同，则判定为平局。
import random

faces = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
class Card:

    def __init__(self,face):
        self.face = face

    def __repr__(self):
        return f'{self.face}'

class Twentyone:

    def __init__(self):
        self.cards = [Card(face) for _ in range(4) for face in faces]
        self.current = 0

    def shuffle(self):
        random.shuffle(self.cards)
        self.current = 0

    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card

class Players:
    def __init__(self,name):
        self.name = name
        self.card = []

    def get_cards(self,card):
            self.card.append(card)

    def score(self):
        result = 0

        for i in self.card:
            if repr(i) in ('J','Q','K'):
                result += 10
            elif repr(i) == 'A':
                    result += 1
            elif int(repr(i)) in range(2, 11):
                result += int(repr(i))
        return result

class Banker(Players):
    def __init__(self,name):
        super().__init__(name)
        self.hide = 0

    def show_cards(self):
        self.hide = self.card[1]
        self.card[1] = '*'
        print(f'庄家:{self.card}')

    def show_hide(self):
        self.card[1] = self.hide
        print(f'庄家:{self.card}')
        return  self.card

class Player(Players):
    def __init__(self, name):
        super().__init__(name)

    def show_cards(self):
        print(f'闲家：{self.card}')

    def a_determine(self):
        determine_list = [j for j in self.card if repr(j) == 'A']
        count_a = len(determine_list)
        result_1 = 0
        if count_a == 1:
            fac1 = self.score()
            fac2 = self.score() + 10
            if fac2 > 21:
                result_1 = fac1
            else:result_1 = fac2
        elif count_a == 2:
            fac3 = self.score()
            fac4 = self.score() + 9
            if fac4 > 21:
                result_1 = fac3
            else: result_1 = fac4
        else:result_1 = self.score()
        return result_1


print('请创建角色')
i = input('闲家：')
j = input('庄家：')
p1, p2 = Player(i), Banker(j)
card_pile = Twentyone()
card_pile.shuffle()
print('游戏开始')
for _ in range(2):
    p1.get_cards(card_pile.deal())
    p2.get_cards(card_pile.deal())
p1.show_cards()
p2.show_cards()
if p1.a_determine() == 21:
    print('游戏结束，闲家胜')
while True:
    has_next = input('闲家是否继续要牌（y or n）：')
    if has_next == 'n':
        p2.show_hide()

        if p2.score() >= 17:
            if p2.score() < p1.a_determine():
                print('游戏结束，闲家胜')
            elif p2.score() > p1.a_determine():
                print('游戏结束，庄家胜')
            else:print('游戏结束，平局')
        else:
            print('庄家要牌')
            while p2.score() < 17:
                p2.get_cards(card_pile.deal())
            p1.show_cards()
            p2.show_hide()
            if p2.score() < p1.a_determine() or p2.score() > 21:
                print('游戏结束，闲家胜')
            elif p1.a_determine() < p2.score() <= 21 or p1.a_determine()>21:
                print('游戏结束，庄家胜')
            else:
                print('游戏结束，平局')
        break

    if has_next == 'y':
        print('闲家要牌')
        p1.get_cards(card_pile.deal())
        p1.show_cards()
        if p1.a_determine() > 21:
            print('庄家胜')
            break
        elif p1.a_determine() == 21:
            print('游戏结束，闲家胜')
            break