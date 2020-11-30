import sqlite3
import sys
from Проект.Setup import NewItemUI, Main_ui, CritUi
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QInputDialog, QTableWidgetItem, QDialog, \
    QAbstractItemView, QLabel, QPushButton


class Crit(QWidget, CritUi):
    def __init__(self, form):
        super().__init__()
        self.setupUi(self)
        self.form = form
        self.init()

    def init(self):
        self.criteti.currentTextChanged.connect(self.c)
        self.show_it.clicked.connect(self.click)

    def c(self):
        self.text_crit.setText('')

    def click(self):
        try:
            a = self.criteti.currentText()
            self.table.setRowCount(0)
            if a == 'id':
                """
                crit =  id
                """
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(['Название', 'Цена', 'Количество', 'Номер партии', 'Состояние'])
                b = self.form.cur_db.execute(
                    f'select title,price,count,id_party,condition from {self.form.table_name} where id = {self.text_crit.text()}').fetchall()
                for i, items in enumerate(b):
                    self.table.setRowCount(self.table.rowCount() + 1)
                    for j, item in enumerate(items):
                        self.table.setItem(i, j, QTableWidgetItem(str(item)))
            elif a == 'Название':
                """
                crit = title
                """
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(['id', 'Цена', 'Количество', 'Номер партии', 'Состояние'])
                b = self.form.cur_db.execute(
                    f'select id,price,count,id_party,condition from {self.form.table_name} where title = "{self.text_crit.text()}"').fetchall()
                for i, items in enumerate(b):
                    self.table.setRowCount(self.table.rowCount() + 1)
                    for j, item in enumerate(items):
                        self.table.setItem(i, j, QTableWidgetItem(str(item)))
            elif a == 'Цена':
                """
                crit = price
                """
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(['id', 'Наименовние', 'Количество', 'Номер партии', 'Состояние'])
                b = self.form.cur_db.execute(
                    f'select id,title,count,id_party,condition from {self.form.table_name} where price = {self.text_crit.text()}').fetchall()
                for i, items in enumerate(b):
                    self.table.setRowCount(self.table.rowCount() + 1)
                    for j, item in enumerate(items):
                        self.table.setItem(i, j, QTableWidgetItem(str(item)))
            elif a == 'Кол-во':
                """
                crit = count
                """
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(['id', 'Наименовние', 'Цена', 'Партия', 'Состояние'])
                b = self.form.cur_db.execute(
                    f'select id,title,price,id_party,condition from {self.form.table_name} where count = {self.text_crit.text()}').fetchall()
                for i, items in enumerate(b):
                    self.table.setRowCount(self.table.rowCount() + 1)
                    for j, item in enumerate(items):
                        self.table.setItem(i, j, QTableWidgetItem(str(item)))
            elif a == 'Партия':
                """
                crit = id_party
                """
                self.table.setColumnCount(4)
                self.table.setHorizontalHeaderLabels(['id', 'Наименование', 'Цена', 'Количество', 'Состояние'])
                b = self.form.cur_db.execute(
                    f'select id,title,price,count,condition from {self.form.table_name} where id_party = {self.text_crit.text()}').fetchall()
                for i, items in enumerate(b):
                    self.table.setRowCount(self.table.rowCount() + 1)
                    for j, item in enumerate(items):
                        self.table.setItem(i, j, QTableWidgetItem(str(item)))
            elif a == 'Состояние':
                """
                crit = condition
                """
                self.table.setColumnCount(5)
                self.table.setHorizontalHeaderLabels(['id', 'Наименование', 'Цена', 'Количество', 'Номер партии'])
                b = self.form.cur_db.execute(
                    f'select id,title,price,count,id_party from {self.form.table_name} where condition = "{self.text_crit.text()}"').fetchall()
                for i, items in enumerate(b):
                    self.table.setRowCount(self.table.rowCount() + 1)
                    for j, item in enumerate(items):
                        self.table.setItem(i, j, QTableWidgetItem(str(item)))
        except Exception as e:
            print(e)

    def closeEvent(self, event):
        try:
            self.form.is_append = True
            self.form.show()
        except Exception as e:
            print(e)


class DialogOk(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.paren = parent
        self.initialization()

    def initialization(self):
        try:
            self.resize(300, 150)
            self.setWindowTitle('Подтверждение')
            self.text = QLabel('Вы уверены что хотите удалить элемент?', self)
            self.text.setGeometry(25, 10, 250, 30)
            self.ok = QPushButton(self)
            self.ok.setText('Да')
            self.ok.setGeometry(60, 50, 75, 30)
            self.no = QPushButton(self)
            self.no.setText('Нет')
            self.no.setGeometry(160, 50, 75, 30)
            self.setWindowModality(True)
            self.show()
            self.ok.clicked.connect(self.yes)
            self.no.clicked.connect(self.nop)
        except Exception as e:
            print(e)

    def yes(self):
        """
        Если выбрал да
        """
        self.paren.is_delete = True
        self.paren.delete()
        self.close()

    def nop(self):
        """
        Если выбрал нет
        """
        self.paren.is_delete = False
        self.paren.delete()
        self.close()


class Error(QDialog):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.form = parent
        self.text = text
        self.init_ui()
        self.setWindowModality(True)
        self.show()

    def init_ui(self):
        self.resize(300, 150)
        self.setWindowTitle('Ошибка!')
        self.label = QLabel(self.text, self)

    def closeEvent(self, event):
        self.form.retern_last()


class NewItem(QWidget, NewItemUI):
    def __init__(self, form):
        super().__init__()
        self.setupUi(self)
        self.form = form
        self.error = False
        self.new_item.clicked.connect(self.give)

    def give(self):
        try:
            """
            trying to commit data base with changes
            """
            id, title, count, price, id_party, cond = self.id.text(), self.name.text(), self.count.text(), self.price.text(), \
                                                      self.id_party.text(), self.box.currentText()
            self.form.cur_db.execute(
                f'insert into magazine(id, title, price, count, id_party, condition) values({id}, "{title}",'
                f' {count}, {price}, {id_party}, "{cond}")')
            self.form.data_base.commit()
            self.closeEvent(self)
        # изменить Exception чтобы при ошибке вылетало окно и оставаться здесь же
        except Exception as e:
            print(e)
            self.error = True
            self.closeEvent(self)

    def closeEvent(self, event):
        """
        starting closing with execute modality windows
        """
        try:
            if self.error:
                self.form.is_append = False
                self.form.show()
                self.form.error.show()
            else:
                self.form.is_append = True
                self.form.show()
        except Exception as e:
            print(e)


class Main(QWidget, Main_ui):
    def __init__(self):
        super().__init__()
        self.is_change = False
        self.me_change = False
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        try:
            self.is_append = True
            """
            получаем имя файла бд и открываем его
            у нас возможно только одно имя таблицы, при желании изменить
            """
            file = QFileDialog.getOpenFileName(self, 'Открываемая БД')[0]
            self.data_base = sqlite3.connect(file)
            self.cur_db = self.data_base.cursor()
            self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.main_table.setSelectionMode(QAbstractItemView.SingleSelection)
            self.main_table.setColumnCount(6)
            self.table_name = 'magazine'
            """
            заполняем нашу таблицу главного окна значениями из базы данных
            здесь нужно быть осторожным тк при изменении таблицы в базе данных также нужно изменить настройки
            нашей базы данных например количество столбцов
            """
            res = self.cur_db.execute(f'select * from {self.table_name}').fetchall()
            for i, elements in enumerate(res):
                self.main_table.setRowCount(self.main_table.rowCount() + 1)
                for j, element in enumerate(elements):
                    self.main_table.setItem(i, j, QTableWidgetItem(str(element)))
        except Exception as e:
            self.error.show()
            print(e)
        self.is_change = True
        """
        подключенние слотов, убедителная просьба не менять их имена
        тк возможно их использование в других классах или функциях
        """
        self.new_elem.clicked.connect(self.new_item)
        self.showforkrit.clicked.connect(self.show_krit)
        self.main_table.itemChanged.connect(self.change_data)
        self.main_table.currentItemChanged.connect(self.whaaat)

    def retern_last(self):
        """
        здесь мы задаем текст если при изменении произошла ошибка
        """
        try:
            self.me_change = True
            self.ch.setText(self.prev)
            self.me_change = False
        except Exception as e:
            print(e)

    def whaaat(self, prev, now):
        if not self.me_change:
            """
            здесь мы получаем текст на последнем выбранном элементе тк возможна ошибка
            значения параметров: prev - текущий, now - предыдущий (да, немного напутал в полключении слота к сигналу)
            """
            self.prev = prev.text()

    def change_data(self):
        try:
            """
            Проверка если я изменяю специально
            """
            if not self.me_change:
                self.ch = self.main_table.item(self.main_table.currentRow(), self.main_table.currentColumn())
                if self.ch != None:
                    if self.ch.column() == 0:
                        self.p = Error(self, 'Ошибка, невозможно изменить id')
                    else:
                        if self.ch.text() != '':
                            if self.ch.column() == 1:
                                """
                                Change to title
                                """
                                self.cur_db.execute(
                                    f'update magazine set title = "{self.ch.text()}" where id = {self.main_table.item(self.ch.row(), 0).text()}')
                                self.data_base.commit()
                            elif self.ch.column() == 2:
                                """
                                Change to price
                                """
                                self.cur_db.execute(
                                    f'update magazine set price = {self.ch.text()} where id = {self.main_table.item(self.ch.row(), 0).text()}')
                                self.data_base.commit()
                            elif self.ch.column() == 3:
                                """
                                Change to count
                                """
                                self.cur_db.execute(
                                    f'update magazine set count = {self.ch.text()} where id = {self.main_table.item(self.ch.row(), 0).text()}')
                                self.data_base.commit()
                            elif self.ch.column() == 4:
                                """
                                Change to id_party
                                """
                                self.cur_db.execute(
                                    f'update magazine set id_party = {self.ch.text()} where id = {self.main_table.item(self.ch.row(), 0).text()}')
                                self.data_base.commit()
                            elif self.ch.column() == 5:
                                """
                                Change to conditions
                                """
                                self.cur_db.execute(
                                    f'update magazine set condition = "{self.ch.text()}" where id = {self.main_table.item(self.ch.row(), 0).text()}')
                                self.data_base.commit()
                        else:
                            self.p = Error(self, 'Ошибка значение изменено на нулевое')
        except Exception as e:
            print(e)

    def new_item(self):
        self.a = NewItem(self)
        self.a.show()
        self.hide()

    def deleting(self):
        self.is_delete = False
        self.yes = DialogOk(self)

    def delete(self):
        if self.is_delete:
            item = self.main_table.selectedItems()
            row = item[0].row()
            id = item[0].text()
            self.cur_db.execute(f'delete from magazine where id = {id}')
            self.main_table.removeRow(row)
            self.data_base.commit()

    def show_krit(self):
        try:
            self.a = Crit(self)
            self.a.show()
            self.hide()
        except Exception as e:
            print(e)

    def showEvent(self, event):
        try:
            if self.is_append:
                self.me_change = True
                res = self.cur_db.execute(f'select * from magazine').fetchall()
                try:
                    self.main_table.setRowCount(0)
                except Exception as e:
                    print(e)
                for i, elements in enumerate(res):
                    self.main_table.setRowCount(self.main_table.rowCount() + 1)
                    for j, element in enumerate(elements):
                        self.main_table.setItem(i, j, QTableWidgetItem(str(element)))
                self.me_change = False
            else:
                raise Exception
        except Exception as e:
            print(e)
            self.error.setText('Ошибка! Пожалуйста, проверте правильность ввода информации')
            self.error.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = Main()
    b.show()
    sys.exit(app.exec())
else:
    print('wow')
