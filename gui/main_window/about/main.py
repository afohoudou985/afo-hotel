from pathlib import Path
from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    About()


class About(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        # Titre principal
        self.canvas.create_text(
            36.0, 43.0,
            anchor="nw",
            text="AfoHotel a été créé par",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        # Images des créateurs
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(191.0, 26.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(203.0, 205.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(565.0, 205.0, image=self.image_image_3)

        # Labels des pseudos / rôles
        self.canvas.create_text(
            56.0, 121.0,
            anchor="nw",
            text="Tinkerer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )

        self.canvas.create_text(
            418.0, 121.0,
            anchor="nw",
            text="SW-Fan",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )

        # Noms des créateurs
        self.canvas.create_text(
            56.0, 138.0,
            anchor="nw",
            text="Afo",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            418.0, 138.0,
            anchor="nw",
            text="Azim",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        # Noms de famille
        self.canvas.create_text(
            56.0, 170.0,
            anchor="nw",
            text="Houdou",
            fill="#5E95FF",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            418.0, 170.0,
            anchor="nw",
            text="Saibou",
            fill="#5E95FF",
            font=("Montserrat Bold", 18 * -1),
        )

        # Séparateur
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(308.0, 150.0, image=self.image_image_4)

        self.canvas.create_rectangle(
            56.0, 197.0, 169.0, 199.0, fill="#FFFFFF", outline=""
        )
        self.canvas.create_rectangle(
            418.0, 197.0, 531.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(669.0, 151.0, image=self.image_image_5)

        # Copyright
        self.canvas.create_text(
            197.0, 352.0,
            anchor="nw",
            text="© 2021-22 Afo et Azim, Tous droits réservés",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            246.0, 372.0,
            anchor="nw",
            text="Open source sous licence MIT",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        # Description de Mohit (à gauche)
        self.canvas.create_text(
            56.0, 207.0,
            anchor="nw",
            text="Un accro au code, un créateur enthousiaste et un",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            56.0, 223.0,
            anchor="nw",
            text="apprenant passionné, Afo aime apporter",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            56.0, 239.0,
            anchor="nw",
            text="la perfection à tout ce qu’il fait. Il est",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            56.0, 255.0,
            anchor="nw",
            text="également un designer passionné et un fan",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            56.0, 271.0,
            anchor="nw",
            text="inconditionnel des Avengers.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        # Description d’Anirudh (à droite)
        self.canvas.create_text(
            418.0, 207.0,
            anchor="nw",
            text="Un passionné de technologie et programmeur freelance,",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            418.0, 223.0,
            anchor="nw",
            text="Azim aime passer son temps dans un monde",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            418.0, 239.0,
            anchor="nw",
            text="d’ordinateur. On peut parfois le trouver dans",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            418.0, 255.0,
            anchor="nw",
            text="la réalité, en promenant son chien ou en regardant",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
        self.canvas.create_text(
            418.0, 271.0,
            anchor="nw",
            text="Star Wars.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )