import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view
        self._selected_language = None
        self._selected_modality = None

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleLanguageSelection(self,e):
        # prendo il valore selezionato
        self._selected_language = e.control.value.lower()
        if self._selected_language not in ["italian", "english", "spanish"]:
            self._view._lvOut.controls.append(ft.Text("Seleziona una lingua valida!", color="red"))
        else:
            self._view._lvOut.controls.append(ft.Text(f"Lingua selezionata: {self._selected_language}", color="green"))
        # aggiorno la GUI
        self._view.page.update()


    def handleModalitySelection(self,e):
        self._selected_modality = e.control.value
        if self._selected_modality not in ["Default", "Linear", "Dichotomic"]:
            self._view._lvOut.controls.append(ft.Text(f"Seleziona una modalità valida!", color = "red"))
        else:
            self._selectedModality = self._selected_modality
            self._view._lvOut.controls.append(ft.Text(f"Modalità selezionata: {self._selected_modality}",color = "green"))
        self._view.page.update()

    def handleSpellCheck(self,e):
        testo = self._view._txtInput.value
        #controllo che l'utente ha inserito tutti i campi prima di premere "Correzione"
        if self._selected_modality == None or self._selected_language == None:
            self._view._lvOut.controls.append(ft.Text("Errore: Seleziona lingua, modalità e inserisci un testo!", color="red"))
            self._view.update()
            return
        #richiamo handleSentence
        parole_errate, tempo = self.handleSentence(testo, self._selected_language,self._selected_modality)
        #stampo i risultati
        self._view._lvOut.controls.append(ft.Text(f"Frase inserita: {testo}"))
        self._view._lvOut.controls.append(ft.Text(f"Parole errate: {parole_errate}"))
        self._view._lvOut.controls.append(ft.Text(f"Tempo richiesto: {tempo} secondi"))
        #svuoto il campo testo
        self._view._txtInput.value = ""
        self._view.update()






def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text