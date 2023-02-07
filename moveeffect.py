class Move:
    def __init__(self, sender, receiver, statsaffected, affectopponent):
        self._sender = sender #pokemon who send the attack
        self._receiver = receiver #pokemon who received the attack
        self._statsaffected = statsaffected #lowing spe attak, [[stats1, multiplicateur],[stats2, multiplicateur]]
        self._affectopponent = affectopponent #burn the target [[effect1, accuracy], [effect2, accuracy]] flinch included !