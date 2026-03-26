import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self._ddLanguage= ft.Dropdown(width=200, value="Lingua",
                                      options=[ft.dropdown.Option(key ="italian",text="Italian"),
                                      ft.dropdown.Option(key ="english",text="english"),
                                      ft.dropdown.Option(key ="spanish",text="spanish")],
                                      on_change=self.__controller.handleLanguageSelection)
                                    # quando succede qualcosa chiama questa funzione
        row1 = ft.Row(controls=[self._ddLanguage], alignment=ft.MainAxisAlignment.CENTER)

        self._ddModality = ft.Dropdown(width=200, value="Modalità di ricerca",
                                       options=[ft.dropdown.Option(key = "Default", text = "Default"),
                                                ft.dropdown.Option(key = "Linear", text = "Linear"),
                                                ft.dropdown.Option(key = "Dichotomic", text = "Dichotomic")],
                                                on_change=self.__controller.handleModalitySelection)
        self._txtInput = ft.TextField(label="Inserisci il testo", width=400)
        self._ebCorrezione = ft.ElevatedButton(text="Correzione", on_click=self.__controller.handleSpellCheck)

        row2 = ft.Row(controls=[self._ddModality, self._txtInput, self._ebCorrezione], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        self._lvOut = ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=True
        )

        self.page.add(row1, row2, self._lvOut)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
