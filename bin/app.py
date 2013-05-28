import web
from gothonweb import map

urls = (
	'/game', 'GameEngine',
	'/', 'Index'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store,
								  initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
	def GET(self):
		# this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")


class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is this here? do we need it?
			return render.you_died()					# Code as on LPTHW pg. 171
#			return render.show_room(room=map.START)		# Code as adjusted by JRN wk of 5/21/13

	def POST(self):
		form = web.input(action=None)

		# there is a bug here. can you fix it?
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")

if __name__ == "__main__":
	app.run()
