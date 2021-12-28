import itertools
import random
from copy import deepcopy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True
        
        # DEBUG PURPOSE (sample values)
        # self.board[1][1] = True
        # self.board[1][6] = True
        # self.board[3][6] = True
        # self.board[4][1] = True
        # self.board[4][2] = True
        # self.board[6][2] = True
        # self.board[6][5] = True
        # self.board[7][7] = True
        
        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if self.count == len(self.cells):
            return self.cells
        return {}

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        return {}

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count = self.count - 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)
            
    # Return surrounding cells whose state is indetermined with appropriate count
    def new_sentence(self, cell, count):
        new_count = count
        surrounding_cells = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (i != 0 or j != 0) and 0 <= cell[0] + i < self.height and 0 <= cell[1] + j < self.width:
                    if (cell[0] + i, cell[1] + j) in self.mines:
                        new_count = new_count - 1
                    elif (cell[0] + i, cell[1] + j) not in self.safes:
                        surrounding_cells.append((cell[0] + i, cell[1] + j))
        return surrounding_cells, new_count
    
    # For all knowledge, mark new cells as safe or mines and update the internal knowledge
    def check_safes_and_mines(self):
        for knowledge in self.knowledge:
            new_mines = list(knowledge.known_mines())
            new_safes = list(knowledge.known_safes())
            for mine in new_mines:
                self.mark_mine(mine)
            for safe in new_safes:
                self.mark_safe(safe)
        for knowledge in self.knowledge:
            for mine in self.mines:
                knowledge.mark_mine(mine)
            for safe in self.safes:
                knowledge.mark_safe(safe)
                
    # Using sample values to spot bugs and errors
    def debug(self, breakpoint, show):
        print(f"********** Checkpoint {breakpoint} **********")
        if show:
            for knowledge in self.knowledge:
                print(knowledge)
            print(f"mines: {self.mines}")
            print(f"safes: {self.safes - self.moves_made}")
            print(f"moves made: {self.moves_made}")
        bug = False
        all_mines = {(1, 1), (1, 6), (3, 6), (4, 1), (4, 2), (6, 2), (6, 5), (7, 7)}
        all_safes = {(i, j) for i in range(8) for j in range(8)} - all_mines
        for knowledge in self.knowledge:
            cells = list(knowledge.cells)
            count = 0
            for cell in cells:
                if cell in all_mines:
                    count = count + 1
            if knowledge.count != count:
                print("ERROR KNOWLEDGE")
                bug = True
                print(f"Knowledge: {knowledge}, expected count: {count}")
        if self.mines.issubset(all_mines) == False:
            print("ERROR MINES")
            bug = True
        if self.safes.issubset(all_safes) == False:
            print("ERROR SAFE")
            bug = True
        if bug == False:
            print("DEBUGGING COMPLETE - NO BUG SPOTTED!\n")
        else:
            print("WARNING!!! THERE ARE ERRORS SPOTTED!")
            print(f"Breakpoint: {breakpoint}\n")
            
    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`qg
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        
        # (1) & (2): mark the cell as a move that has been made and safe
        self.moves_made.add(cell)
        self.safes.add(cell)
        for knowledge in self.knowledge:
            knowledge.mark_safe(cell)
        #self.debug("1", False)
        
        # (3): add new sentence to the AI's knowledge base
        surrounding_cells, updated_count = self.new_sentence(cell, count)
        new_sentence = Sentence(surrounding_cells, updated_count)
        if new_sentence not in self.knowledge and new_sentence.cells != set():
            self.knowledge.append(new_sentence)
        #self.debug("2", False)
        
        # (4): mark additional cells as safe or mine if it can be concluded
        self.check_safes_and_mines()
        #self.debug("3", False)
        
        # (5): keep on adding knowledge as long as there are still inferences from existing knowledge
        new_inference = True
        while (new_inference):
            new_inference = False
            for knowledge in self.knowledge:
                if knowledge.cells == set():
                    self.knowledge.remove(knowledge)
            #self.debug("4a", False)
            
            self.check_safes_and_mines()
            #self.debug("4b", False)
            
            knowledges_deepcopy = deepcopy(self.knowledge)
            for knowledge1 in knowledges_deepcopy:
                for knowledge2 in knowledges_deepcopy:
                    if knowledge1.cells.issubset(knowledge2.cells) and knowledge1.cells != knowledge2.cells:
                        new_sentence = Sentence(knowledge2.cells - knowledge1.cells, knowledge2.count - knowledge1.count)
                        if new_sentence not in self.knowledge and new_sentence.cells != set():
                            new_inference = True
                            self.knowledge.append(new_sentence)      
            #self.debug("4c", False)
            
        self.check_safes_and_mines()
        #self.debug("5", False)
        return

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        safe_moves = []
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.safes and (i, j) not in self.moves_made and (i, j) not in self.mines:
                    safe_moves.append((i, j))
        if len(safe_moves) == 0:
            return None
        moves_made = random.choice(safe_moves)
        print(f"________________________________________\nTiles clicked = {moves_made}")
        return moves_made

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        random_moves = []
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) not in self.mines and (i, j) not in self.moves_made:
                    random_moves.append((i, j))
        if len(random_moves) == 0:
            return None
        moves_made = random.choice(random_moves)
        print(f"________________________________________\nTiles clicked = {moves_made}")
        return moves_made
