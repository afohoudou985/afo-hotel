from pathlib import Path
from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *
from ..main_window.main import mainWindow

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def loginWindow():
    Login()


class Login(Toplevel):
    # Fonction de vérification de connexion
    def loginFunc(self):
        global user
        if checkUser(self.username.get().lower(), self.password.get()):
            user = self.username.get().lower()
            self.destroy()
            mainWindow()
            return
        else:
            messagebox.showerror(
                title="Identifiants invalides",
                message="Le nom d'utilisateur et le mot de passe ne correspondent pas",
            )

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("Connexion - AfoHotel")
        self.geometry("1012x506")
        self.configure(bg="#5E95FF")

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        # Fond blanc à droite
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        # Champs de saisie (images de fond)
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(736.0, 331.0, image=entry_image_1)

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(736.0, 229.0, image=entry_image_2)

        # Labels des champs
        self.canvas.create_text(
            573.0, 306.0,
            anchor="nw",
            text="Mot de passe",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.canvas.create_text(
            573.0, 204.0,
            anchor="nw",
            text="Nom d'utilisateur",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        # Titre principal
        self.canvas.create_text(
            553.0, 66.0,
            anchor="nw",
            text="Entrez vos identifiants de connexion",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        # Bouton de connexion
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginFunc,
            relief="flat",
        )
        button_1.place(x=641.0, y=412.0, width=190.0, height=48.0)

        # Logo et titre à gauche
        self.canvas.create_text(
            85.0, 77.0,
            anchor="nw",
            text="AfoHotel",
            fill="#FFFFFF",
            font=("Montserrat Bold", 50 * -1),
        )

        # Instructions
        self.canvas.create_text(
            553.0, 109.0,
            anchor="nw",
            text="Entrez les identifiants que l'administrateur vous a fournis",
            fill="#CCCCCC",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            553.0, 130.0,
            anchor="nw",
            text="lors de votre inscription au programme",
            fill="#CCCCCC",
            font=("Montserrat Bold", 16 * -1),
        )

        # Champ Nom d'utilisateur
        entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(736.0, 241.0, image=entry_image_3)

        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
        )
        self.username.place(x=573.0, y=229.0, width=326.0, height=22.0)

        # Champ Mot de passe
        entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(736.0, 342.0, image=entry_image_4)

        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
            show="•",
        )
        self.password.place(x=573.0, y=330.0, width=326.0, height=22.0)

        # Copyright
        self.canvas.create_text(
            90.0, 431.0,
            anchor="nw",
            text="© Afo & Azim, 2021",
            fill="#FFFFFF",
            font=("Montserrat Bold", 18 * -1),
        )

        # Image décorative
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(458.0, 326.0, image=image_image_1)

        # Description à gauche
        self.canvas.create_text(
            90.0, 150.0,
            anchor="nw",
            text="AfoHotel est un système",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0, 179.0,
            anchor="nw",
            text="de gestion d'hôtel qui",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0, 208.0,
            anchor="nw",
            text="vous permet de gérer les clients,",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0, 237.0,
            anchor="nw",
            text="les chambres et les réservations grâce à",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0, 266.0,
            anchor="nw",
            text="une solution bien conçue.",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0, 295.0,
            anchor="nw",
            text="Connectez-vous pour découvrir",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0, 324.0,
            anchor="nw",
            text="par vous-même...",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        # Bind de la touche Entrée pour valider le formulaire
        self.username.bind("<Return>", lambda x: self.loginFunc())
        self.password.bind("<Return>", lambda x: self.loginFunc())

        # Paramètres de la fenêtre
        self.resizable(False, False)
        self.mainloop()