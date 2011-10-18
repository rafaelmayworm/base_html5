import sublime, sublime_plugin, os, sys, re
sys.path.append('lib')
import source_tools

class Actionscript3Import(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit = edit
		# Project reference
		st = source_tools.SourceTools(self.view.file_name(), os.path.join(sublime.packages_path(), 'ActionScript3'))

		# Get the word we'll search for
		self.current_word_region = self.view.word(self.view.sel()[0])
		self.current_word = self.view.substr(self.current_word_region)

		self.matches = st.find_package(self.current_word.strip())

		if len(self.matches) == 0:
			sublime.status_message("No package found");
			return
		elif len(self.matches) == 1:
			# Found only one, let's insert it
			imp = self.matches[0]
		else:
			# Lots of choices
			self.view.window().show_quick_panel(self.matches, self.on_import_selected)
			return	
		self.finilize_import(imp)

	def finilize_import(self, imp):
		# Class name
		cla = imp.split('.').pop()
		# Replace Class name
		self.view.replace(self.edit, self.current_word_region, cla)

		# Exit if already imported
		if self.view.find("^\\s*import\\s+%s(\\s|;)" % imp.replace('.', '\\.'), 0):
			return
		# Searching where to add
		pkg = self.view.find("^\\s*package\\b\\s*([\\w+\\.]*)[\\s\\n]*\\{", 0)
		# cls = self.view.find("^\\s*(public|final)\\s+(final|public)?\\s*\\b(class|interface|function)\\b", 0)
		# mta = self.view.find_all("^\\s*\\[(Style|Bindable|Event|Embed|SWF)")
		# Calculate
		# insert_before = (mta+[cls])[0] # Before class or meta
		insert_after = sublime.Region(0, 0) if pkg is None else pkg # after the package, if it exists

		l = self.view.line(insert_after.end())
		self.view.replace(self.edit, l, "%s\n\timport %s;" % (self.view.substr(l), imp));
		self.view.show(self.view.sel()[0])


	def on_import_selected(self, index):
		if index == -1 :
			return
		self.finilize_import(self.matches[index])