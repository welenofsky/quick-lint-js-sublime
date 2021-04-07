import sublime
import sublime_plugin

class QuickLintJsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		quicklintjs_bin = self.view.settings().get('quicklintjs_bin', 'quick-lint-js')
		filepath = self.view.file_name()
		args = {
			"cmd": [
				quicklintjs_bin,
				filepath
			],
			"file_regex": r"^(.+):(\d+):(\d+): (.*)$",
			"line_regex": r"^.+:(\d+):(\d+): (.*)$"
		}

		self.view.window().run_command('exec', args)