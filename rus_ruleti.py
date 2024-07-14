import random



class RuletGameOperations:

    def __init__(self):
        self.bullet_pos = None
        self.chamber_pos_now = None

    def add_Bullet(self):
        self.bullet_pos = random.randint(1,6)


    def spin(self):
        self.chamber_pos_now = random.randint(1,6)

    def fire_gun(self):

        if self.chamber_pos_now < 6:

            self.chamber_pos_now += 1

        elif self.chamber_pos_now == 6:
            self.chamber_pos_now = 1


yenioyun = RuletGameOperations()

yenioyun.add_Bullet()
yenioyun.spin()


while yenioyun.chamber_pos_now < 7:

    input("şansınızı denemek ister misiniz ? ")

    print("anlık merminin yeri ", yenioyun.bullet_pos)


    yenioyun.fire_gun()
    print("anlık pozisyonunuz ", yenioyun.chamber_pos_now)

    if yenioyun.chamber_pos_now == yenioyun.bullet_pos:
        print("Kötü oldu!! öldünüz !!")
        break
    else:
        print("huuf!! ucuz atlattın")

