import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")


"""
	- film
	- emberjs data
	- sublime docs
	- forro lessons
	- invite dea
	- spritesheetgen pull
	- pull to replace videos
	- 
"""