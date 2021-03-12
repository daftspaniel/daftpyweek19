
from gamelib.entities import RND, Tile, Beastie, Laser, Orb, TILE_WIDTH, HealthPack

class LevelMaker(object):

    def __init__(self):
        pass

    def CreateRoom(self, level, Tiles, Beasties, Lasers, Health):
        print(level)
        # Test Level for Dev
        if level == 0:
            for j in range(10):
                for i in range(10):
                    t = Tile(320 + TILE_WIDTH*i, 240 + TILE_WIDTH*j,
                             (55, 0, 0), (170+(i*3 + j*4), 20+(i*8+j*8), 0))
                    Tiles.append(t)

            Beasties.append(Beastie(300 + RND(100), 310))
            Beasties.append(Beastie(400 + RND(100), 390))
            Beasties.append(Beastie(500 + RND(100), 430))

            # Lasers
            l = Laser(700, 500)
            Beasties.append(l)
            Lasers.append(l)

        if level == 1:

            for j in range(2):
                for i in range(14):
                    t = Tile(220 + TILE_WIDTH*i, 340 + TILE_WIDTH*j,
                             (55, 0, 0), (170+(i*3 + j*4), 20+(i*5+j*5), 120))
                    Tiles.append(t)

            self.addBeasties(Beasties, 3)
            Health.append(HealthPack(50,300))

        elif level == 2 or level == 6:

            for j in range(10):
                for i in range(10):
                    if ((j == 0 or j == 9) or i == 0 or i == 9):
                        t = Tile(320 + TILE_WIDTH*i, 240 + TILE_WIDTH*j,
                                 (55, 0, 0), (170+(i*3 + j*4), 20+(i*8+j*8), 0))
                        Tiles.append(t)

            self.addBeasties(Beasties, 3)
            self.addOrbs(Beasties, 2)

            if level == 6:
                self.addLasers(Lasers, 1)
                self.addOrbs(Beasties, 1)

        elif level == 3:
            self.drawRect(Tiles, 200, 300, 5, 5)
            self.drawRect(Tiles, 350, 350, 5, 5)

            self.drawRect(Tiles, 500, 300, 5, 5)
            self.drawRect(Tiles, 650, 350, 5, 5)

            self.addBeasties(Beasties, 5)
            self.addOrbs(Beasties, 1)

        elif level == 4:

            self.drawRect(Tiles, 200, 300, 25, 4)
            self.addLasers(Lasers, 1)
            self.addBeasties(Beasties, 2)
            self.addOrbs(Beasties, 1)

        elif level == 5:

            r = 1
            for j in range(10):
                for i in range(r):
                    t = Tile(320 + TILE_WIDTH*i, 240 + TILE_WIDTH*j,
                             (55, 0, 0), (170+(i*3 + j*4), 20+(i*8+j*8), 0))
                    Tiles.append(t)
                r += 1
            self.addBeasties(Beasties, 7)
            self.addOrbs(Beasties, 2)

        elif level == 7:

            t = Tile(750, 380, (55, 0, 0), (30, 144, 255))
            Tiles.append(t)
            self.addBeasties(Beasties, 16)
            self.addOrbs(Beasties, 2)

        elif level == 8:

            t = Tile(750, 380, (55, 0, 0), (30, 144, 255))
            Tiles.append(t)
            self.addBeasties(Beasties, 16)
            self.addLasers(Lasers, 1)
            self.addOrbs(Beasties, 2)

        elif level == 9:

            self.drawRect(Tiles, 200, 300, 5, 5)

            self.drawRect(Tiles, 320, 340, 16, 1)

            self.drawRect(Tiles, 650, 300, 5, 5)

            self.addBeasties(Beasties, 4)
            self.addLasers(Lasers, 2)

        elif level == 10:

            while (len(Tiles) < 20):
                t = Tile(80 + RND(28) * TILE_WIDTH, 200 + TILE_WIDTH *
                         RND(10), (55, 0, 0), (RND(255), 144, 155))
                Tiles.append(t)
            self.addBeasties(Beasties, 8)
            self.addLasers(Lasers, 1)
            self.addOrbs(Beasties, 2)

        elif level == 11:
            r = 1
            for j in range(10):
                for i in range(r):
                    t = Tile(120 + TILE_WIDTH*i, 240 + TILE_WIDTH*j,
                             (55, 0, 0), (170+(i*3 + j*4), 20+(i*8+j*8), 0))
                    Tiles.append(t)
                    t = Tile(420 + TILE_WIDTH*i, 240 + TILE_WIDTH*j,
                             (55, 0, 0), (170+(i*3 + j*4), 20+(i*8+j*8), 0))
                    Tiles.append(t)
                r += 1
            self.addBeasties(Beasties, 7)
            self.addOrbs(Beasties, 3)

        else:
            self.drawRect(Tiles, 200, 200, min(
                level + RND(level), 30), min(5 + RND(level), 10))
            if RND(3) == 1:
                self.addOrbs(Beasties, 2)
            if RND(3) == 1:
                self.addLasers(Lasers, RND(3))
            self.addBeasties(Beasties, 4 + RND(level))

    def addLasers(self, Lasers, count):
        for b in range(count):
            Lasers.append(Laser(700, 515))

    def addBeasties(self, Beasties, count):
        for b in range(count):
            Beasties.append(Beastie(300 + RND(100), 250 + RND(100)))

    def addOrbs(self, Beasties, count):
        for b in range(count):
            Beasties.append(Orb(700 + RND(99), 120 + RND(200)))

    def drawRect(self, Tiles, x, y, w, h):
        for j in range(h):
            for i in range(w):
                t = Tile(x + TILE_WIDTH*i, y + TILE_WIDTH*j, (55, 0, 0),
                         (min(170+(i*3 + j*4), 255), min(20+(i*8+j*8), 255), 0))
                Tiles.append(t)
