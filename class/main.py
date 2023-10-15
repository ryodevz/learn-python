"""
Web Profile : https://ryodev.my.id
Repo        : https://github.com/ryotwell/learn-python
"""

class Ryotwell():
    def __init__( self ):
        self.username   = "@ryotwell"
        self.languages  = [ "PHP", "Javascript", "Python", "Java" ]
        self.frameworks = [ "Laravel", "NextJs", "ReactJs", "VueJs" ]

    def about( self ):
        print( f"Hello, I'm {self.username}, you can contact me on Instagram at {self.username}." )

Ryotwell().about()