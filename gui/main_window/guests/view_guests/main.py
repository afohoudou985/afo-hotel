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
from tkinter.ttk import Treeview
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def view_guests():
    ViewGuests()


class ViewGuests(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.search_query = StringVar()

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

        # Barres de séparation
        self.canvas.create_rectangle(
            40.0, 14.0, 742.0, 16.0, fill="#EFEFEF", outline=""
        )
        self.canvas.create_rectangle(
            40.0, 342.0, 742.0, 344.0, fill="#EFEFEF", outline=""
        )

        # Titres principaux
        self.canvas.create_text(
            116.0, 33.0,
            anchor="nw",
            text="Voir les invités",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            116.0, 65.0,
            anchor="nw",
            text="Et effectuer des opérations",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1),
        )

        self.canvas.create_text(
            40.0, 367.0,
            anchor="nw",
            text="Actions disponibles :",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        # Image décorative
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(666.0, 59.0, image=self.image_image_1)

        # Champ de recherche
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(680.5, 60.0, image=self.entry_image_1)

        entry_1 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            foreground="#777777",
            font=("Montserrat Bold", 18 * -1),
            textvariable=self.search_query,
        )
        # Recherche en temps réel
        entry_1.bind(
            "<KeyRelease>",
            lambda event: self.filter_treeview_records(self.search_query.get()),
        )
        entry_1.place(x=637.0, y=48.0, width=87.0, height=22.0)

        # Bouton Rafraîchir
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.refresh_btn = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_refresh,
            relief="flat",
        )
        self.refresh_btn.place(x=525.0, y=33.0, width=53.0, height=53.0)

        # Bouton Retour
        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(617.0, 60.0, image=self.image_image_2)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.navigate_back_btn = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_navigate_back,
            relief="flat",
        )
        self.navigate_back_btn.place(x=40.0, y=33.0, width=53.0, height=53.0)

        # Bouton Supprimer
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.delete_btn = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_delete,
            relief="flat",
            state="disabled",
        )
        self.delete_btn.place(x=596.0, y=359.0, width=146.0, height=48.0)

        # Bouton Modifier
        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.edit_btn = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_edit,
            relief="flat",
            state="disabled",
        )
        self.edit_btn.place(x=463.0, y=359.0, width=116.0, height=48.0)

        # Configuration du Treeview
        self.columns = {
            "Guest ID": ["ID Invité", 80],
            "Name": ["Nom", 120],
            "Address": ["Adresse", 150],
            "Email": ["Email", 180],
            "Phone Number": ["Téléphone", 130],
            "Created At": ["Date de création", 150],
        }

        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
        )

        # Configuration des en-têtes et largeurs des colonnes
        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            self.treeview.column(idx, width=txt[1])

            self.treeview.place(x=40.0, y=101.0, width=700.0, height=229.0)

            # Chargement initial des données
            self.handle_refresh()

            # Événement de sélection
            self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

    def filter_treeview_records(self, query):
        """Filtre les enregistrements en fonction de la recherche"""
        self.treeview.delete(*self.treeview.get_children())

        for row in self.guest_data:
            # Recherche dans toutes les colonnes
            if query.lower() in str(row).lower():
                self.treeview.insert("", "end", values=row)

                self.on_treeview_select()

    def on_treeview_select(self, event=None):
        """Gère la sélection d'une ligne dans le tableau"""
        try:
            self.treeview.selection()[0]
        except:
            self.parent.selected_rid = None
            return

        # Récupérer l'élément sélectionné
        item = self.treeview.selection()[0]
        self.parent.selected_rid = self.treeview.item(item, "values")[0]

        # Activer les boutons Modifier et Supprimer
        self.delete_btn.config(state="normal")
        self.edit_btn.config(state="normal")

    def handle_refresh(self):
        """Rafraîchit la liste des invités"""
        self.treeview.delete(*self.treeview.get_children())
        self.guest_data = db_controller.get_guests()

        for row in self.guest_data:
            self.treeview.insert("", "end", values=row)

    def handle_navigate_back(self):
        """Retour vers l'écran d'ajout"""
        self.parent.navigate("add")

    def handle_delete(self):
        """Supprime l'invité sélectionné"""
        if db_controller.delete_guest(self.parent.selected_rid):
            messagebox.showinfo("Succès", "Invité supprimé avec succès")
        else:
            messagebox.showerror("Erreur", "Impossible de supprimer l'invité")

            self.handle_refresh()

    def handle_edit(self):
        """Passe en mode modification"""
        self.parent.navigate("edit")
        self.parent.windows["edit"].initialize()