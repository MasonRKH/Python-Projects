class Ship:

    """

        This class represents a single Ship object to be used in the Battleship game.

        It requires a name and a shape of any variety, defined by a list of (x, y) coordinates

        surrounding (0,0). It uses the status dictionary to track health (which parts are hit,

        not hit) and the coords list to track it's placement on the Board object.


       The class defines several helpful methods and fields:

           place(): Given (x, y) coordinates, this function creates an entry in the status

                    dictionary. It is placed by adding the ship's shape to the (x, y) coordinates.

                    Adding (x, y) from the shape to the requesting (x, y) placement, each result is

                    mapped to the ship's icon. Returns coords, a list of the (x, y) results for use in

                    the board class

           print(): Prints the ship's form including any damage, followed by it's name.

           is_sunk(): Tests if ship is fully damaged, returning boolean based on results.

           rotate(): Rotates ship 90 degrees per iteration by changing (x, y) to (y, -x).

           print_assist(): Returns Ship icon for use in printing Board

    """

    def __init__(self, name, shape):

        '''

        Creates basic Ship object, with name string and a list of tuples for shape. The icon

        is created from the first letter of the Ship's name string.

        '''

        self.name = name

        self.icon = name[0]

        self.shape = shape


    def place(self, x, y):

        '''

        Given (x, y) coordinates, this function creates an entry in the status

        dictionary. It is placed by adding the ship's shape to the (x, y) coordinates.


        Adding (x, y) from the shape to the requested (x, y) placement, each result is

        mapped to the ship's icon.


        Returns coords, a list of the (x, y) results for use in

        the board class

        '''

        self.status = {}

        self.coords = []

        for i in self.shape:

            i = (i[0] + x, i[1] + y)

            self.coords.append(i)

        for i in self.coords:

            self.status[i] = self.icon

        return self.coords


    def print(self):

        '''

        Prints the Ships shape using the status dictionary's values.

        '''

        temp = ''

        for x in self.status.values():

            if x == 'X': # replaces X with *

                temp += '*'

            else:

                temp += x

        print(temp, end = '')

        temp = len(temp)

        print(" "*(9-temp), end="") # Space calculator for correct formatting

        print(self.name)


    def is_sunk(self):

        '''

        Tests if ship is fully damaged (i.e. all status values are 'X')

        Returns boolean based on results.

        '''

        if self.icon in self.status.values():

            return False

        else:

            return True


    def rotate(self, amount):

        '''

        Rotates ship 90 degrees per iteration by changing (x, y) to (y, -x).

        Iterates (amount) times, assumes integer

        '''

        for i in range(amount):

            for i in range(len(self.shape)):

                coord = self.shape[i]

                coord = (coord[1], -coord[0])

                self.shape[i] = coord


    def print_assist(self, x, y):

        '''

        Helper function for Board printing, returns icon for Ship object in supplied coordinate.

        '''

        return self.status[x, y]
