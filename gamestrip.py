from deckstrip import Deck


class Monotone:
    ASCENDING = 1
    DESCENDING = -1
    STATIONARY = None

    def __init__(self):
        """Object of class stores cards in monotone sequences and
        remembers his state"""
        self._stack = []
        self._state = Monotone.STATIONARY

    def push(self, card):
        if self.__checker_push(card):
            self._stack.append(card)
            return True
        return False

    def __checker_push(self, card):
        if len(self._stack) < 1:
            return True
        if len(self._stack) >= 1:
            if self._state is Monotone.STATIONARY:
                if card > self._stack[-1]:
                    self._state = Monotone.ASCENDING
                    return True
                if card < self._stack[-1]:
                    self._state = Monotone.DESCENDING
                    return True
            else:
                if self._state == Monotone.ASCENDING and card > self._stack[-1]:
                    return True
                if self._state == Monotone.DESCENDING and card < self._stack[-1]:
                    return True
            return False

    @property
    def check_strict_monotone(self):
        """Checks if sequence is strictly ascending monotone"""
        if len(self._stack) < 2:
            return True
        else:
            for index in range(len(self._stack) - 1):
                if self._stack[index + 1] - self._stack[index] != 1:
                    return False
            return True

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)

    def __iter__(self):
        return iter(self._stack)


class Game:
    GAME_NUM = 4
    BASE_NUM = 6
    STACK_CARDS = 13

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._game_stacks = [[] for _ in range(Game.GAME_NUM)]
        self._base_stacks = [Monotone() for _ in range(Game.BASE_NUM)]
        for i in range(Game.GAME_NUM):
            for j in range(Game.STACK_CARDS):
                card = self._deck.deal()
                self._game_stacks[i].append(card)

    @classmethod
    def _check_put_stack(cls, put_stack):
        """Checks pertinency of chosen basestack"""
        return 0 <= put_stack <= Game.BASE_NUM - 1

    @classmethod
    def _check_take_stack(cls, take_stack):
        """Checks pertinency of chosen gamestack"""
        return 0 <= take_stack <= Game.GAME_NUM - 1

    def is_win(self):
        res = 0
        if self._empty_gamestacks():
            for stack in self._base_stacks:
                if stack.check_strict_monotone:
                    res += 1
            return res == Game.BASE_NUM
        return False

    def _empty_gamestacks(self):
        """Checks if all gamestacks are empty"""
        res = 0
        for stack in self._game_stacks:
            if len(stack) == 0:
                res += 1
        return res == Game.GAME_NUM

    def move_card(self, take_stack, put_stack):
        """Fulfills the move if it is allowed"""
        if self.valid_move(take_stack, put_stack):
            card = self._game_stacks[take_stack][-1]
            if self._base_stacks[put_stack].push(card):
                self._game_stacks[take_stack].pop()
                return True
        return False

    def valid_move(self, take_stack, put_stack):
        """Checks whether move is valid or not"""
        if Game._check_put_stack(put_stack) and Game._check_take_stack(take_stack):
            if self._game_stacks[take_stack]:
                return True
        return False

    def show_info(self):
        """Show current game state"""
        print("Game Stacks:")
        for stack in self._game_stacks:
            print([str(card) for card in stack])
        print("Base Stacks:")
        for stack in self._base_stacks:
            print([str(card) for card in stack])
        print("")
