#!/usr/bin/env python3
import random

global blts


def buy_blts():
    opt = input("Would you like to buy more bullets? [y/n]: ")
    while 1:
        if opt == "y":
            opt2 = input("How many would you like to buy: ")
            health -= int(opt2)
            blts += int(opt2)
            break
        elif opt == "n":
            break
        else:
            opt = input("Answer y or n: ")
    
    print("\n{}   Bullets".format(blts))
    print("{}%  Health\n".format(health))
    #return health, blts


def print_stats(zombs_left):
            print("")
            print("{}   Zombies left".format(zombs_left))
            print("{}   Bullets".format(blts))
            print("{}%  Health".format(health))
            print("")


def kill(num_zomb):

    opt = input("\nWould you like to attempt to kill all zombies or\nfire at each one once and hope for the best?: [all / hope]: ")
    while 1:

        if opt == "all":
            while num_zomb or blts == 0:
                dead = random.randint(0, 1)
                if dead:
                    num_zomb -= 1

                blts -= 1

            print_stats(num_zomb)

        elif opt == "hope":
            for i in range(num_zomb):
                dead = random.randint(0, 1)
                if dead:
                    num_zomb -= 1
                else:
                    health -= 10

                blts -= 1

            print_stats(num_zomb)

        else:
            opt = input("all or hope?: ")

        if health > 0:
            buy_blts()

        #return health, blts

def zombie(array):
    print(health)

    print("====================================================")

    while 1:
        room = random.randint(0, len(array) - 1)
        znum = random.randint(1, 8)
        print("{} and there are {} zombies" .format(array[room], znum))
        
        kill(znum)

        if health <= 0:
            print("You Died :(\n")
            break

        if room < len(array) - 3:
            break

    #return health, blts

def main():

    ins = ["You are now in a bedroom with a minibar",
           "You are now in a sun room with tinted windows",
           "You are now in a torture chamber with a rubber ducky on the table",
           "You are now in an indoor pool area with a Billiard ball table",
           "You are now in an observatory with toy telescope",
           "You are now in a kitchen filled knee deep with plastic sporks",
           "You are now in a library that contains a hard copy of Wikipedia",
           "You are now in a game room with Gears of Halo Theft Auto 364 on the TV",
           "You are now in a lab room with Kuzco's poison on the table",
           "You are now in a bathroom with a golden toilet",
           "You are now in a laundry room covered in mud",
           "You are now in a home office room with a 4 foot coffee machine",
           "You are now in the Chamber of Secrets with a wooden stick on the ground",
           "You are now in an art gallery with the original Mona Lisa",
           "You are now in a ballroom with the Monster Mash playing in the background",
           "You are now in a wine cellar with imported ancient Egyptian Kool-Aid"]
    outs = ["You are now next to a pool filled with sharks that have lazor shooting eyes",
            "You are now in a GI-Joe statue memorial",
            "You are now next to a large Chocolate Fountain",
            "You are now in a 3 foot tall hedge maze",
            "You are now in a red Green house with Yellow lights strobing",
            "You are now next to a sandbox with a diving board on the side",
            "You are now in a BBQ area with Hallo-Weenies on the grill",
            "You are now in a hermit's hut made from paper mache",
            "You are now in a children's playground with workout stations",
            "You are now in a Chia-pet garden"]

    global health
    health = 100
    blts = 25
    
    zombie(ins)

    if health > 0:
        zombie(outs)
        return 0

    print("\nYou made it to the get away car!! Score: {}".format(health))

    return 0


if __name__ == "__main__":
    main()
