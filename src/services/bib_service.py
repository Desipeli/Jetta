class BibService:

    def generate_bib(self, notes):
        """bibtex parser function

        Args:
            notes (list): A list of note objects to be parsed to bibtex

        Returns:
            String: a string file, which follows bibtex-format
        """
        if len(notes) > 0:
            print(notes)
            bibtex_string = ""
            for note in notes:
                print(note)
                self.validate_note(note)
                bibtex_string += "@" + note.bib_category + \
                "{" + note.bib_citekey + "," + "\n\ttitle = {" + note.title + "}," +\
                "\n\tauthor = {" + note.author + "}," + "\n\tyear = {" + note.year + "}," + \
                "\n\tdoi_address = {" + note.doi_address + "}\n}" + "\n"
            return bibtex_string
            

    def validate_note(self,note):
        valid_categories = ["book","article","phdthesis","misc"]
        if note.bib_category in valid_categories and \
            note.bib_citekey != "":
            return True
        raise ValueError("The note object is not valid for bib_tex")

the_bib_service = BibService()
