
from gi.repository import Gtk


@Gtk.Template(resource_path='/org/example/App/window.ui')
class ProjetomontannatefWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ProjetomontannatefWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'projetomontannatef'
        self.props.version = "0.1.0"
        self.props.authors = ['gwitus']
        self.props.copyright = '2022 gwitus'
        self.props.logo_icon_name = 'org.example.App'
        self.props.modal = True
        self.set_transient_for(parent)
