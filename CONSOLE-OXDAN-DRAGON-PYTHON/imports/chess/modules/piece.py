""" piece.py
File containing all the piece classes used in drawing_tools.py
"""

import pygame


class Piece:
    def __init__(self, color):
        self.color = color
        self._is_active = True

    @property
    def get_color(self):
        return self.color

    @property
    def is_active(self):
        return self.is_active

    @is_active.setter
    def is_active(self, value):
        self.is_active = value


class Pawn(Piece):
    def __init__(self, color):
        self.piece_type = "PAWN"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./resources/chess/chess_images_ai/BP.png").convert_alpha()
        else:
            return pygame.image.load("./resources/chess/chess_images_ai/WP.png").convert_alpha()

class Knight(Piece):
    def __init__(self, color):
        self.piece_type = "KNIGHT"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./resources/chess/chess_images_ai/BN.png").convert_alpha()
        else:
            return pygame.image.load("./resources/chess/chess_images_ai/WN.png").convert_alpha()


class Bishop(Piece):
    def __init__(self, color):
        self.piece_type = "BISHOP"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./resources/chess/chess_images_ai/BB.png").convert_alpha()
        else:
            return pygame.image.load("./resources/chess/chess_images_ai/WB.png").convert_alpha()


class Rook(Piece):
    def __init__(self, color):
        self.piece_type = "ROOK"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./resources/chess/chess_images_ai/BR.png").convert_alpha()
        else:
            return pygame.image.load("./resources/chess/chess_images_ai/WR.png").convert_alpha()


class Queen(Piece):
    def __init__(self, color):
        self.piece_type = "QUEEN"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./resources/chess/chess_images_ai/BQ.png").convert_alpha()
        else:
            return pygame.image.load("./resources/chess/chess_images_ai/WQ.png").convert_alpha()


class King(Piece):
    def __init__(self, color):
        self.piece_type = "KING"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./resources/chess/chess_images_ai/BK.png").convert_alpha()
        else:
            return pygame.image.load("./resources/chess/chess_images_ai/WK.png").convert_alpha()
