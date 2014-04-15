# import sublime
import sublime_plugin
import codecs


class Rot13Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                enc = codecs.getencoder("rot-13")
                # Transform it via rot13
                s = enc(s)[0]
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
