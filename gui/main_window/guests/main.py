from pathlib import Path
from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller

# Import des différentes vues de la section Invités
from .add_guests.gui import AddGuests
from .view_guests.main import ViewGuests
from .update_guests.main import UpdateGuests

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def guests():
    Guests()


class Guests(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Variable pour stocker l'ID de l'invité sélectionné
        self.selected_rid = None

        # Chargement initial des données des invités
        self.guest_data = db_controller.get_guests()

        self.configure(bg="#FFFFFF")

        # Dictionnaire contenant toutes les sous-fenêtres (écrans)
        self.windows = {
            "add": AddGuests(self),
            "view": ViewGuests(self),
            "edit": UpdateGuests(self),
        }

        # Affichage par défaut : écran d'ajout
        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1013.0, height=506.0)
        self.current_window.tkraise()

    def navigate(self, name):
        """Change l'écran affiché (Ajouter / Voir / Modifier)"""
        # Masquer toutes les fenêtres
        for window in self.windows.values():
            window.place_forget()

            # Afficher la fenêtre demandée
            self.windows[name].place(x=0, y=0, width=1013.0, height=506.0)
            self.current_window = self.windows[name]