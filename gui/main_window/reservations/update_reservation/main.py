from pathlib import Path

from tkinter import (
    Frame,
    Canvas,
    Entry,
    Text,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
)
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_reservations():
    UpdateReservations()


class UpdateReservations(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_r_id = self.parent.selected_rid

        # Variables pour les champs modifiables
        self.data = {
            "id": StringVar(),
            "meal": StringVar(),
            "type": StringVar(),
            "g_id": StringVar(),
            "check_in": StringVar(),
            "room_id": StringVar(),
            "reservation_date": StringVar(),
            "check_out": StringVar(),
        }

        self.configure(bg="#FFFFFF")
        self.initialize()

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

        # Barre de séparation supérieure
        self.canvas.create_rectangle(
            40.0, 14.0, 742.0, 16.0, fill="#EFEFEF", outline=""
        )

        # Titres
        self.canvas.create_text(
            116.0, 33.0,
            anchor="nw",
            text="Modifier la réservation",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            116.0, 65.0,
            anchor="nw",
            text="Modifier les informations",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1),
        )

        # Bouton retour vers l'ajout
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("add"),
            relief="flat",
        )
        button_1.place(x=40.0, y=33.0, width=53.0, height=53.0)

        # Reservation ID (non modifiable)
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(145.0, 150.0, image=self.image_image_1)

        self.canvas.create_text(
            60.0, 125.0,
            anchor="nw",
            text="ID de la réservation",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.id_text = self.canvas.create_text(
            60.0, 152.0,
            anchor="nw",
            text="Sélectionnez d'abord un enregistrement...",
            fill="#979797",
            font=("Montserrat Bold", 18 * -1),
        )

        # Is Taking Meal
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(145.0, 246.0, image=self.image_image_2)

        self.canvas.create_text(
            60.0, 221.0,
            anchor="nw",
            text="Prend un repas ?",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(149.5, 258.0, image=self.entry_image_1)

        entry_2 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["meal"],
        )
        entry_2.place(x=60.0, y=246.0, width=179.0, height=22.0)

        # Type
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(145.0, 342.0, image=self.image_image_3)

        self.canvas.create_text(
            60.0, 317.0,
            anchor="nw",
            text="Type",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(149.5, 354.0, image=self.entry_image_2)

        entry_3 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["type"],
        )
        entry_3.place(x=60.0, y=342.0, width=179.0, height=22.0)

        # Guest ID
        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(391.0, 150.0, image=self.image_image_4)

        self.canvas.create_text(
            306.0, 125.0,
            anchor="nw",
            text="ID de l'invité",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_3 = self.canvas.create_image(395.5, 162.0, image=self.entry_image_3)

        entry_4 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["g_id"],
        )
        entry_4.place(x=306.0, y=150.0, width=179.0, height=22.0)

        # Check-in Time
        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(391.0, 246.0, image=self.image_image_5)

        self.canvas.create_text(
            306.0, 221.0,
            anchor="nw",
            text="Date d'arrivée",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_4 = self.canvas.create_image(395.5, 258.0, image=self.entry_image_4)

        entry_5 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["check_in"],
        )
        entry_5.place(x=306.0, y=246.0, width=179.0, height=22.0)

        # Reservation Date
        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(391.0, 342.0, image=self.image_image_6)

        self.canvas.create_text(
            306.0, 317.0,
            anchor="nw",
            text="Date de réservation",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_5 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_5 = self.canvas.create_image(395.5, 354.0, image=self.entry_image_5)

                # Reservation Date
        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(391.0, 342.0, image=self.image_image_6)

        self.canvas.create_text(
            306.0, 317.0,
            anchor="nw",
            text="Date de réservation",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        entry_6 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["reservation_date"],
        )
        entry_6.place(x=306.0, y=342.0, width=179.0, height=22.0)

        # Room ID
        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(637.0, 150.0, image=self.image_image_7)

        self.canvas.create_text(
            552.0, 125.0,
            anchor="nw",
            text="ID de la chambre",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_6 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_6 = self.canvas.create_image(641.5, 162.0, image=self.entry_image_6)

        entry_7 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["room_id"],
        )
        entry_7.place(x=552.0, y=150.0, width=179.0, height=22.0)

        # Check Out Time
        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(637.0, 246.0, image=self.image_image_8)

        self.canvas.create_text(
            552.0, 221.0,
            anchor="nw",
            text="Date de départ",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_7 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_7 = self.canvas.create_image(641.5, 258.0, image=self.entry_image_7)
        entry_8 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
            textvariable=self.data["check_out"],
        )
        entry_8.place(x=552.0, y=246.0, width=179.0, height=22.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_update,
            relief="flat",
        )
        button_2.place(x=570.0, y=318.0, width=144.0, height=48.0)

    def initialize(self):
        self.selected_r_id = self.parent.selected_rid
        self.reservation_data = self.parent.reservation_data

        # Filter out all reservations for selected id reservation
        self.selected_reservation_data = list(
            filter(lambda x: str(x[0]) == self.selected_r_id, self.reservation_data)
        )

        if self.selected_reservation_data:
            self.selected_reservation_data = self.selected_reservation_data[0]

            self.canvas.itemconfigure(
                self.id_text, text=self.selected_reservation_data[0]
            )
            self.data["g_id"].set(self.selected_reservation_data[1])
            self.data["room_id"].set(self.selected_reservation_data[2])
            self.data["check_in"].set(self.selected_reservation_data[3])
            self.data["check_out"].set(self.selected_reservation_data[4])
            self.data["meal"].set(self.selected_reservation_data[5])
            self.data["reservation_date"].set(self.selected_reservation_data[3])

    def initialize(self):
        """Charge les données de la réservation sélectionnée"""
        self.selected_r_id = self.parent.selected_rid
        self.reservation_data = self.parent.reservation_data  # à adapter selon votre structure

        # Filtrer les données pour l'ID sélectionné
        self.selected_reservation = list(
            filter(lambda x: str(x[0]) == self.selected_r_id, self.reservation_data)
        )

        if self.selected_reservation:
            self.selected_reservation = self.selected_reservation[0]

            # Mise à jour de l'affichage de l'ID
            self.canvas.itemconfigure(self.id_text, text=self.selected_reservation[0])

            # Remplissage des champs
            self.data["g_id"].set(self.selected_reservation[1])          # Guest ID
            self.data["check_in"].set(self.selected_reservation[2])      # Check-in
            self.data["room_id"].set(self.selected_reservation[3])       # Room ID
            self.data["check_out"].set(self.selected_reservation[4] if len(self.selected_reservation) > 4 else "")
            self.data["meal"].set(self.selected_reservation[5] if len(self.selected_reservation) > 5 else "")
            self.data["type"].set(self.selected_reservation[6] if len(self.selected_reservation) > 6 else "")
            self.data["reservation_date"].set(self.selected_reservation[7] if len(self.selected_reservation) > 7 else "")


    def handle_update(self):
        """Met à jour la réservation dans la base de données"""
        data = [
            self.data[label].get()
            for label in ("g_id", "check_in", "room_id", "check_out", "meal")
        ]

        if db_controller.update_reservation(self.selected_r_id, *data):
            messagebox.showinfo("Succès", "Réservation modifiée avec succès")
            self.parent.navigate("view")
            self.reset()
        else:
            messagebox.showerror(
                "Erreur",
                "Erreur lors de la modification de la réservation. Veuillez vérifier que tous les IDs existent."
            )

            self.parent.refresh_entries()


    def reset(self):
        """Réinitialise tous les champs du formulaire"""
        for label in self.data:
            self.data[label].set("")

            self.canvas.itemconfigure(
                self.id_text,
                text="Sélectionnez d'abord un enregistrement..."
            )