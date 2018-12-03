from random import randint
from sys import exit
from textwrap import dedent

class Scene(object):
    def enter(self):
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Fail(Scene):
    quips = [
        "You failed. Try again!",
        "Meh nobody is perfect",
        "Try again!",
        "Oops, you messed up!",
        "Better luck next time!"
    ]

    def enter(self):
        print(Fail.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class FashionShow(Scene):
    def enter(self):
        print(dedent("""
            Today is the big day for the annual fashion show event!
            You're the director of the fashion brand, Prada and you're
            stuck on what theme you want to present for investors. You have 3
            themes to choose from: Jungle, Floral and Noir. Keep in mind that
            you want to impress all the judges with your new designs, so make
            sure you choose the best one! Which theme are you going to display?
			"""))

        action = input("> ")

        if action == "Jungle":
            print(dedent("""
                You decide to showcase your Jungle theme to the audience and
                the judge panel. The models are dressed in leopard and zebra
                prints. Unfortunately, the theme was a disaster because one of
                the judges was a lobbyist for PETA and wrote a hit-piece on your
                fashion line and how inhumane it was.
			    """))
            return 'Fail'

        elif action == "Floral":
            print(dedent("""
                 You decide to showcase your Floral theme to the audience and
                 the judge panel. The models are wearing elegant fabrics flourished
                 with rose, lily, and hydrangea patterns scattered all over. The
                 audience loves the designs presented on stage but one of the
                 judges got reminded of her ex-boyfriend as he always gave her
                 lilies on their anniversary. Heartbroken, the judge angrily
                 rejects the theme and hates it.
				"""))
            return 'Fail'

        elif action == "Noir":
            print(dedent("""
	        You decide to showcase your Noir theme to the audience and the
            judge panel. The models are wearing fedoras with long coats and
            wearing fringe dresses as if it were the roaring 20's. The judges
            are impressed to be immersed to a different era of time and they
            absolutely loved the outfits shown. Now it's time for the next theme!
			   """))
            return 'NextTheme'

        else:
            print("Um, it's only 3 themes can you try again? Time is ticking!")
            return 'FashionShow'


class NextTheme(Scene):
    def enter(self):
        print(dedent("""
		      With the success of the first theme, now you need something else to
              really show off the lavish lifestyle. You have three more themes to
              choose from. Remember the theme counts and you must impress all the
              judges and the audience! The themes are: Birthday Party or Steam Punk.
              Which theme do you want to go with?
			"""))

        action2 = input("> ")

        if action2 == "Birthday Party":
            print(dedent("""
			You decided on the Birthday Party theme to the audience and the
            judge panel. The models are wearing balloon animals and confetti
            all over their outfits. The judges thought the design was childish
            and one of the judges got scared because it reminded her of her
            intense phobia of clowns.
			    """))
            return 'Fail'

        elif action2 == "Steam Punk":
            print(dedent("""
			    You decided on the Steam Punk theme to the audience and the judge
                panel. The models are dressed in Victoran Era outfits with metallic
                accessories and clockwork designs. The judges are impressed by the
                unique features and designs. Awesome!
			    """))
            return 'LastTheme'

        else:
            print("It's only 2 choices, the fashion show depends on you!")
            return 'NextTheme'


class LastTheme(Scene):
    def enter(self):
        print(dedent("""

			It is now the final act of the fashion show and you want to end it
            with a bang. You have three celebrity performances you can choose to
            close off the event and impress the investors and the judges. You can
            choose from Bruno Mars, Britney Spears, or Kayne West. Who do you want
            to perform the final act?
			"""))

        action = input("> ")

        if action == "Bruno Mars":
            print(dedent("""
			You choose Bruno Mars to perform for the final act. He gets in
            his groove and flairs his funkiness to the crowd. However, the
            audience is bored of his constant stage presence and thinks his
            performance wasn't anything special. It was lame to put it at best.
			    """))
            return 'Fail'

        elif action == "Britney Spears":
            print(dedent("""

			    You thought Britney Spears was here? Honey, she's in Vegas where
                all the washed up celebrites linger. The show had no final act
                and the judges and audience were bored and infuriated.
			    """))
            return 'Fail'

        elif action == "Kayne West":
            print(dedent("""
            You choose Kayne to end the fashion show to impress the judges. He
            gets on stage and before performing, he makes a speech about how
            great he is and how he's going to create a death ray because he is
            so innovative. He then goes on a tangent that his brand should've
            been on display instead of yours and leaves the stage. Not surprisingly,
            the audience and judges felt symphathy from Kayne insulting your brand
            and you gain positive reputation for the entire year.
            """))
            return 'finished'
        else:
            print("You really need to finish this event, c'mon!")
            return 'LastTheme'


class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):
    scenes = {
        'FashionShow': FashionShow(),
        'NextTheme': NextTheme(),
        'LastTheme': LastTheme(),
        'Fail': Fail(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('FashionShow')
a_game = Engine(a_map)
a_game.play()
