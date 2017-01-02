import testingobject

class Child(object):
    def __init__(self):
        self.other = testingobject.Other()

    def coolness(self):
        self.other.coolness()

    def not_coolness(self):
        print "I am not coolness"

    def help_coolness(self):
        print "Help Before"
        self.other.help_coolness()
        print "Help After"

son = Child()

son.coolness()
son.not_coolness()
son.help_coolness()