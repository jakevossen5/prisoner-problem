class Box:
    identifier = -1
    val_in_box = -1

    def __init__(self, identifier, val_in_box):
        self.identifier = identifier
        self.val_in_box = val_in_box

    def set_val_in_box(self, new_val_in_box):
        self.val_in_box = new_val_in_box
