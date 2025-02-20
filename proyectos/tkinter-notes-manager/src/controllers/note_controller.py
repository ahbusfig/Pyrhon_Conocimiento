class NoteController:
    def __init__(self, note_model, ui):
        self.note_model = note_model
        self.ui = ui

    def create_note(self, title, content):
        note = self.note_model(title, content)
        self.ui.display_note(note)

    def update_note(self, note, new_title, new_content):
        note.title = new_title
        note.content = new_content
        self.ui.update_display(note)

    def delete_note(self, note):
        self.ui.remove_note_display(note)