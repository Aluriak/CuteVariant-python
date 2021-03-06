from PySide2.QtWidgets import *
from PySide2.QtCore import *


from cutevariant.core.model import *
import peewee


class VariantModel(QAbstractListModel):
    def __init__(self):
        super(VariantModel, self).__init__()
        self.data = []

    def rowCount(self, index):
        return len(self.data)

    def data(self, index, role):

        if role == Qt.DisplayRole:
            return self.data[index.row()].pos

        return QVariant()

    def load(self, filename):
        self.beginResetModel()
        self.database = peewee.SqliteDatabase(filename)
        db.initialize(self.database)
        self.data = Variant.select()
        self.endResetModel()
