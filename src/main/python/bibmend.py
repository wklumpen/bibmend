import time

from PyQt5 import QtWidgets, uic

import bibtexparser

class BibmendMainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        uic.loadUi(ui, self)
        self.btnRun.clicked.connect(self.convert)

    
    def message(self, text):
        self.statusbar.showMessage(text)

    def convert(self):
        txt = self.txtInput.toPlainText().strip()
        if len(txt) <= 0:
            self.message("COULD NOT RUN: The input text is empty.")
        else:
            tic = time.perf_counter()
            bib = bibtexparser.loads(txt)
            for entry in bib.entries:
                if self.chkISSN.isChecked():
                    entry.pop('issn', False)
                if self.chkISBN.isChecked():
                    entry.pop('isbn', None)
                if self.chkAbstract.isChecked():
                    entry.pop('abstract', None)
                if self.chkDOI.isChecked():
                    entry.pop('doi', None)
                if self.chkFilepath.isChecked():
                    entry.pop('file', None)
                if self.chkBracket.isChecked():
                    if 'title' in entry:
                        entry['title'] = entry['title'].replace("{", "").replace("}", "")
                if self.chkURL.isChecked():
                    entry.pop('url', None)

            self.txtOutput.setEnabled(True)
            self.txtOutput.setPlainText(bibtexparser.dumps(bib))
            toc = time.perf_counter()
            self.message(f"Checked {len(bib.entries)} entries in {round(toc-tic, 2)} seconds.")
        
