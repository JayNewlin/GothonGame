from random import randint


class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		room = self.paths.get(direction, None)
		if not room:
			room = self.paths.get('death_direction', None)
		return room

	def add_paths(self, paths):
		self.paths.update(paths)


central_corridor = Room("Stage I: Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the Bridge, and blow the ship up after getting into an
escape pod.

You're running down the Central Corridor to the Weapons Armory when
a Gothon jumps out: red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate-filled body. He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")

central_corridor_shoot = Room("Stage I: Central Corridor Death",
"""
Quick on the draw, you yank out your blaster and fire it at the Gothon.
His clown costume is flowing and moving around his body, which throws
off your aim. Your laser hits his costume but misses him entirely. This
completely ruins his brand-new costume that his mother bought him. He
flies into an insane rage and blasts you repeatedly in the face until
you are dead. Then he eats you.
""")

central_corridor_dodge = Room("Stage I: Central Corridor Dodge-Death",
"""
Like a world-class boxer you dodge, weave, slip, and slide just
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips, and you
bang your head on the metal wall. You pass out.
You're only out a few moments ... then the Gothon stomps on
your head and eats you.
""")

laser_weapon_armory = Room("Stage II: Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the Academy.
You tell the one Gothon joke you know:
'Lbbe zbgure vf fb sng, jura fur fvgf nebhaq qur ubhfr, fur fvgf nebhaq gur ubhfr.'
The Gothon stops, tries not to laugh, then bursts out laughing and can't move.
While he's laughing you run up and shoot him square in the head,
putting him down, then jump through the Weapon Armory door.

You do a dive-roll into the Weapons Armory, crouch, and scan the room
for more Gothons that might be hiding. It's dead quiet...too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container. There's a keypad lock on the box,
and you need the code to get the bomb out.  The code is 3 digits.
""")

#---This is text to be added back after issue 18 is resolved---
# If you get the code
# wrong 10 times then the lock closes forever, and you can't
# get the bomb.

armory_death = Room("Stage II: Armory Death",
"""
The lock buzzes one last time and then you hear a sickening
melting sound as the mechanism is fused together.
You decide to sit there, waiting for the Gothons to blow up the
ship from their ship. You'll die in the explosion, of course...
""")


the_bridge = Room("Stage III: The Bridge",
"""
The container clicks open, and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
Bridge, where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")

bridge_throw_bomb = Room("Stage III: Bridge Death",
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door. Just as you drop it a
Gothon shoots you right in the back, killing you.
As you die you see another Gothon frantically try to disarm
the bomb. Your last thought is that they will probably blow up
when it goes off.
""")


escape_pod = Room("Stage IV: Escape Pod",
"""
You point your blaster at the bomb under your arm,
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button,
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pods to
get off this tin can.

You rush through the ship, desperately trying to make it to
the escape pods before the whole ship explodes. It seems like
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods and
now need to pick one to take. Some of them could be damaged,
but you don't have time to look. There are 5 pods. Which one
do you take?"
""")


def START():
#	global keypad_code
	keypad_code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
	print "The Armory keypad_code is", keypad_code

	good_pod = randint(1,5)
	print "The good escape pod is", good_pod

	winner_description = ("""
You jump into pod %r and hit the eject button.
The pod easily slides out into space, heading to
the planet below. As it flies to the planet, you look
back and see your ship implode, then explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
""", good_pod)
	
	the_end_winner = Room("Stage V: The End", winner_description)

	loser_description = """
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into human jelly. Squish!
"""
	the_end_loser = Room("Stage V: Death at the End", loser_description)
	
	escape_pod.add_paths({
		good_pod: the_end_winner,
		'death_direction': the_end_loser
	})

	the_bridge.add_paths({
		'throw the bomb': bridge_throw_bomb,
		'slowly place the bomb': escape_pod
	})

	laser_weapon_armory.add_paths ({
		keypad_code: the_bridge,
		'death_direction': armory_death
	})

	central_corridor.add_paths({
		'shoot!': central_corridor_shoot,
		'dodge!': central_corridor_dodge,
		'tell a joke': laser_weapon_armory
	})
	
	return central_corridor



