from django.shortcuts import render, HttpResponse

# Create your views here.
import time, datetime


def showtime(request):
    t = datetime.datetime.now()

    # return HttpResponse("<h1>%s</h1>" % t)
    return render(request, "show_timea.html", locals())


import random


def query(request):
    class role:
        def __init__(self, name):
            self.Name = name
            self.Life_P = 100
            self.Attack_P = 4
            self.Weapon = "手"

        def equip(self, equip):
            equipments = {'斧頭': 20, '匕首': 8, '劍': 14, '刀': 10, '杖': 5,
                          }
            self.Attack_P = equipments[equip]
            self.Weapon = equip

        def attack(self, enemy, log):
            att = self.Attack_P + random.randrange(self.Attack_P - 4, self.Attack_P + 4)
            log.append("%s進行攻擊:" % (self.Name))
            enemy.attacked(att, log)

        def attacked(self, attv, log):

            if self.Life_P - attv <= 0:
                log.append("%s 受到致命攻擊 ,已經死亡" % self.Name)
            else:
                log.append("%s 受到%s攻擊！減少了<b style='color:red;'>% s</b>血量 , HP剩下: %s" % (
                    self.Name, self.Weapon, attv, self.Life_P - attv))
            self.Life_P = self.Life_P - attv

        def status(self):
            if self.Life_P <= 0:
                return False

    Hero0 = role("賽勒斯")
    Hero1 = role("巴頓")
    Hero2 = role("歐非莉雅")
    Hero0.equip("刀")
    Hero1.equip("斧頭")
    Hero2.equip("杖")
    log = []
    Heros = [Hero0, Hero1]
    while True:
        if Hero0.status() is False or Hero1.status() is False:
            log.append("戰鬥結束")
            break
        a = random.sample([0, 1], 2)
        locals()["Hero%s" % a[0]].attack(locals()["Hero%s" % a[1]], log)
        print(1)

    return render(request, "index.html", locals())
