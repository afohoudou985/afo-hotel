from pathlib import Path
from tkinter import (
    Frame,
    Canvas,
    Entry,
    StringVar,
    Text,
    Button,
    PhotoImage,
    messagebox,
)
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_guests():
    AddGuests()


class AddGuests(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Variables pour les champs du formulaire
        self.data = {
            "name": StringVar(),
            "address": StringVar(),
            "phone": StringVar(),
            "email": StringVar(),
        }

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

        # Image décorative
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(137.0, 153.0, image=self.image_image_1)

        # Nom complet
        self.canvas.create_text(
            52.0, 128.0,
            anchor="nw",
            text="Nom complet",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(137.5, 165.0, image=self.entry_image_1)

        entry_1 = Entry(
            self,
            textvariable=self.data.get("name"),
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_1.place(x=52.0, y=153.0, width=179.0, height=22.0)

        self.canvas.create_text(
            52.0, 155.0,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1),
        )

        # Numéro de téléphone
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(137.0, 259.0, image=self.image_image_2)

        self.canvas.create_text(
            52.0, 234.0,
            anchor="nw",
            text="Numéro de téléphone",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(137.5, 271.0, image=self.entry_image_2)

        entry_2 = Entry(
            self,
            textvariable=self.data.get("phone"),
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_2.place(x=52.0, y=259.0, width=179.0, height=22.0)

        self.canvas.create_text(
            52.0, 261.0,
            anchor="nw",
            text="7976674193",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1),
        )

        # Adresse
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(378.0, 153.0, image=self.image_image_3)

        self.canvas.create_text(
            293.0, 128.0,
            anchor="nw",
            text="Adresse",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(378.5, 165.0, image=self.entry_image_3)

        entry_3 = Entry(
            self,
            textvariable=self.data.get("address"),
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_3.place(x=293.0, y=153.0, width=179.0, height=22.0)

        self.canvas.create_text(
            293.0, 155.0,
            anchor="nw",
            text="Pochinki, Jaipur",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1),
        )

        # Email
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(378.0, 259.0, image=self.image_image_4)

        self.canvas.create_text(
            293.0, 234.0,
            anchor="nw",
            text="Email",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(378.5, 271.0, image=self.entry_image_4)

        entry_4 = Entry(
            self,
            textvariable=self.data.get("email"),
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_4.place(x=293.0, y=259.0, width=179.0, height=22.0)

        self.canvas.create_text(
            293.0, 261.0,
            anchor="nw",
            text="mail@host.in",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1),
        )

        # Bouton principal "Ajouter"
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.save,
            relief="flat",
        )
        button_1.place(x=164.0, y=322.0, width=190.0, height=48.0)

        # Titres
        self.canvas.create_text(
            143.0, 59.0,
            anchor="nw",
            text="Ajouter un nouvel invité",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            549.0, 59.0,
            anchor="nw",
            text="Opérations",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        # Séparateur vertical
        self.canvas.create_rectangle(
            515.0, 59.0, 517.0, 370.0, fill="#EFEFEF", outline=""
        )

        # Bouton Voir les invités
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("view"),
            relief="flat",
        )
        button_2.place(x=547.0, y=116.0, width=209.0, height=74.0)

        # Bouton Modifier
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("edit"),
            relief="flat",
        )
        button_3.place(x=547.0, y=210.0, width=209.0, height=74.0)

        # Sauvegarde des données dans la base
    def save(self):
        # Vérifier si tous les champs sont remplis
        for val in self.data.values():
            if val.get() == "":
                messagebox.showinfo("Erreur", "Veuillez remplir tous les champs")
                return

            # Ajouter l'invité dans la base de données
            result = db_controller.add_guest(
                *[self.data[label].get() for label in ("name", "address", "email", "phone")]
            )

            if result:
                messagebox.showinfo("Succès", "Invité ajouté avec succès")
                self.parent.navigate("view")
                self.parent.windows.get("view").handle_refresh()

                # Réinitialiser les champs
                for label in self.data.keys():
                    self.data[label].set("")
            else:
                messagebox.showerror(
                    "Erreur",
                    "Impossible d'ajouter l'invité. Veuillez vérifier les données saisies."
                )