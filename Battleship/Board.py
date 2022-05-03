class Board:

    """

        This class represents the overall board object of the Battleship game. It contains

        a variable tracking size, and a coordinate dictionary that maps (x, y) positions to misses

        and Ship objects. It can contain as many ship objects as will fit within the designated coordinates


        The constructor builds a completely empty board, with the size only acting to assert valid ship placements


       The class defines several helpful methods and fields:

           add_ship(): Passes position through Ship to calculate ship positions. Then asserts

                    attempted placements to check for validity. After assertions, maps coordinates

                    to the ship object in coords dictionary

           print(): Prints board starting at (0, ymax), using nested loops to iteratively print each position.

                    Adds axis numbering and border lines aswell.

           has_been_used(): Checks if supplied coordinates have been used by checking Board object

                            for 'o' values and ship objects for hits. Returns boolean value based on

                            results.

           attempt_move(): Asserts attempted move is within size boundaries, then asserts

                           move hasn't been attempted. If move is verified then the marker is updated.

                           An 'o' is mapped in the Board object for misses and an 'X' is mapped in the relevent

                           Ship object for hits

    """


    def __init__(self, size):

        '''

        Creates base Board object, with an empty coords dictionary.

        Assumes size is an integer

        '''

        assert size > 0

        self.size = size

        self.coords = {}


    def add_ship(self, ship, position):

        '''

        Passes position through Ship to calculate Ship positions. Then asserts

        attempted placements for validity. After assertions, maps coordinates

        to the Ship object in coords dictionary

        '''

        attemptPlace = ship.place(position[0], position[1])

        for i in attemptPlace:

            assert i not in self.coords

            assert i[0] <= self.size

            assert i[1] <= self.size

        for i in attemptPlace:

            self.coords[i] = ship


    def print(self):

        '''

        Prints board starting at (0, ymax), using nested loops to iteratively print each position.

        Adds axis numbering and border lines aswell.

        '''

        tracker = self.size-1

        temp = 0

        print("  +" + "--" * self.size + "-+")

        for i in range(self.size):      # first loop for y-row

            print(str(tracker) + " |", end="")

            while temp <= self.size-1:      # second loop for each x-coordinate in that row

                if (temp, tracker) in self.coords.keys():

                    if self.coords[(temp, tracker)] == "o":

                        print(" o", end="")

                    elif self.coords[(temp, tracker)]:

                        print(" "+ self.coords[(temp, tracker)].print_assist(temp, tracker),end="",)

                else:

                    print(" .", end="")

                temp += 1

            print(" |")

            temp = 0

            tracker -= 1


        print("  +" + "--" * self.size + "-+")

        print('    ', end='')

        if self.size < 11:

            for i in range(self.size):

                print(str(i)+' ', end='')


        else:

            print('                    1 1 1 1 1 1 1 1 1 1')

            print('    ', end='')

            for i in range(self.size):

                if i < 10:

                    print(str(i)+' ', end='')

                else:

                    print(str(i-10)+' ',end='')


    def has_been_used(self, position):

        '''

        Checks if supplied coordinates have been used by checking Board object

        for 'o' values and ship objects for hits.


        Returns boolean value based on

        results.

        '''

        if position in self.coords.keys() :

            if self.coords[position] == "o":

                return True

            elif self.coords[position].status[position] == "*":

                return True

        return False


    def attempt_move(self, position):

        '''

        Asserts attempted move tuple is within size boundaries, then asserts

        move hasn't been attempted. If move is verified then the position's marker is updated.


        Returns string based on move results.

        '''

        assert position[0] <= self.size

        assert position[1] <= self.size

        if position in self.coords.keys():

            if type(self.coords[position]) == str:

                assert self.coords[position] != "o"

            else:

                assert self.coords[position].status[position] != "*"

        if position in self.coords.keys():

            self.coords[position].status[position] = "*"

            if self.coords[position].icon in self.coords[position].status.values():

                return "Hit"

            else:

                for i in self.coords[position].status.keys():

                    self.coords[position].status[i] = 'X'

                return "Sunk (" + self.coords[position].name + ")"

        else:

            self.coords[position] = "o"

            return "Miss"
