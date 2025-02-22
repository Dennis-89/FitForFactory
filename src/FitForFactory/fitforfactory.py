import sys
from csv import QUOTE_MINIMAL, DictReader, writer
from datetime import datetime
from json import dumps, loads
from pathlib import Path
from random import randrange
from time import monotonic, sleep

# from bcs2.Scale import Scale
from PySide6.QtCharts import (QChart, QChartView, QDateTimeAxis, QLineSeries,
                              QValueAxis)
from PySide6.QtCore import (QDateTime, QObject, QRegularExpression, Qt,
                            QThread, QTimer, Signal)
from PySide6.QtGui import QPainter, QRegularExpressionValidator
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMessageBox,
                               QSizePolicy, QTableWidgetItem, QWidget)
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside6-rcc pictures.qrc -o pictures_rc.py
from ui_form import Ui_FitForFactory

ROOT = Path(__file__).parent
MEMBERS_FILE = ROOT / "members.json"
WEIGHT_FILE = ROOT / "members_to_weight.csv"
TIME_FORMAT = "%d.%m.%Y - %H:%M"
TEST_NAME = "X"
TEST_ID = "abc123"

LOGIN_TEXT = "Zur Anmeldung Chip vorhalten\nVerbleibende Zeit:"
MEASUREMENT_TEXT = "Gewichtsmessung läuft noch:\n"

DURATION_MEASUREMENT = 5
SCALE_ADDRESS = "5C:CA:D3:5E:65:8E"


class Reader(QObject):
    finished = Signal()

    def __init__(self):
        super(Reader, self).__init__(parent=None)
        self.id = None

    def run(self):
        sleep(3)
        self.id = TEST_ID
        self.finished.emit()


class WeightMeasurement(QObject):
    finished = Signal()

    def __init__(self):
        super(WeightMeasurement, self).__init__(parent=None)
        self.weight = None

    def run(self):
        sleep(DURATION_MEASUREMENT)
        self.weight = randrange(40, 120)
        self.finished.emit()
        # scale = Scale(SCALE_ADDRESS)
        # timestamp = monotonic()
        # while True:
        #     scale.measure(0.01)
        #     if monotonic() - timestamp >= DURATION_MEASUREMENT:
        #         self.weight = scale.weight
        #         self.finished.emit()
        #         break


class UserMessage(QMessageBox):
    def __init__(self, event_, title, text, timeout=10):
        super(UserMessage, self).__init__(parent=None)
        self.timer = QTimer()
        self.event_ = event_
        self.title = title
        self.text = text
        self.timeout = timeout
        self.timer.timeout.connect(self.tick)
        self.timer.setInterval(1000)
        self.setWindowTitle(title)
        self.setDefaultButton(self.addButton(QMessageBox.Cancel))
        self.defaultButton().clicked.connect(self.stop_event)
        if title == "Gewichtsmessung":
            self.defaultButton().hide()

    def stop_event(self):
        self.event_.quit()
        self.event_.wait()

    def showEvent(self, event):
        self.tick()
        self.timer.start()

    def tick(self):
        self.timeout -= 1
        if self.timeout > 0:
            self.setText(f"{self.text} {self.timeout} s")
        if not self.event_.isRunning() or self.timeout <= 0:
            self.timer.stop()
            self.defaultButton().animateClick()

    @staticmethod
    def create_new(event_, title, text, timeout):
        window = UserMessage(event_, title, text, timeout)
        window.setIcon(QMessageBox.Information)
        return window.exec()


class FitForFactory(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FitForFactory()
        self.ui.setupUi(self)
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size.setHorizontalStretch(4)
        self.chart_view.setSizePolicy(size)
        self.main_layout.addWidget(self.chart_view)
        self.ui.tabWidget.widget(2).setLayout(self.main_layout)

        validator = QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z\s]*$/"))
        self.ui.user_name.setValidator(validator)
        self.reader_thread = QThread()
        self.reader = Reader()
        self.reader.moveToThread(self.reader_thread)
        self.reader_thread.started.connect(self.reader.run)
        self.reader.finished.connect(self.reader_thread.quit)
        self.scale_thread = QThread()
        self.scale = WeightMeasurement()
        self.scale.moveToThread(self.scale_thread)
        self.scale_thread.started.connect(self.scale.run)
        self.ui.weight_button.setEnabled(False)
        self.user_id = None
        self._init_weight_table()
        self.ui.tabWidget.currentChanged.connect(self.clear_user_information)
        self.ui.register_button.clicked.connect(self.register_process)
        self.ui.login_button.clicked.connect(self.login_process)
        self.ui.logout_button.clicked.connect(self._log_out)
        self.ui.weight_button.clicked.connect(self.weight_process)
        self.update_chart()

    def register_process(self):
        user_name = self.ui.user_name.text()
        members = load_members(MEMBERS_FILE)
        self.get_chip_id()
        if self.user_id is None:
            return
        if is_member(members["members"], self.user_id):
            show_user_register_error(members["members"][self.user_id])
            self.ui.user_info.setText("In der User-Lounge kannst du dich anmelden")
        else:
            register_member(MEMBERS_FILE, members, user_name, self.user_id)
            show_user_info("Registierung abgeschlossen!", f"Willkomen {user_name}!")
            self.ui.user_info.setText(f"{user_name} weiter geht es in der User-Lounge.")

    def login_process(self):
        self.get_chip_id()
        if self.user_id is None:
            return
        members = load_members(MEMBERS_FILE)
        if is_member(members["members"], self.user_id):
            self.ui.hello_user.setText(
                f"Wilkommen {list(map(lambda x: x.get(self.user_id, ""), members["members"]))[0]}, viel Spass!"
            )
            self.ui.login_button.setEnabled(False)
            self.ui.logout_button.setEnabled(True)
            user_weights = get_user_weights(WEIGHT_FILE, self.user_id)
            self.update_weight_table(user_weights)
            timestamp, _ = user_weights[-1]
            if (
                datetime.strptime(timestamp, TIME_FORMAT).date()
                == datetime.now().date()
            ):
                show_user_info("Achtung", f"Du hast dich heute schon gewogen")
            else:
                self.ui.weight_button.setEnabled(True)

    def update_chart(self):
        members = load_members(MEMBERS_FILE)
        for member in members["members"]:
            id_, name = [(id_, name) for id_, name in member.items()][0]
            series = QLineSeries()
            series.setName(name)
            for timestamp, weight in get_user_weights(WEIGHT_FILE, id_):
                timestamp = (
                    QDateTime()
                    .fromString(timestamp, "dd.MM.yyyy - hh:mm")
                    .toMSecsSinceEpoch()
                )
                series.append(timestamp, float(weight))
            self.chart.addSeries(series)
        axis_x = QDateTimeAxis()
        axis_x.setTickCount(10)
        axis_x.setFormat("dd.MM (hh:mm)")
        axis_x.setTitleText("Datum (Uhrzeit)")
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)
        axis_y = QValueAxis()
        axis_y.setTickCount(20)
        axis_y.setLabelFormat("%.2f")
        axis_y.setTitleText("Gewicht [kg]")
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

    def weight_process(self):
        self.scale_thread.start()
        UserMessage.create_new(
            self.scale_thread,
            "Gewichtsmessung",
            MEASUREMENT_TEXT,
            timeout=DURATION_MEASUREMENT,
        )
        if self.scale.weight is None:
            show_user_info(
                "Oh no", "Die Messung war nicht erfolgreich,\n bitte nochmal."
            )
            return
        show_user_info(
            "Ergebniss", f"Folgendes wird gespeichert:\nGewicht: {self.scale.weight} kg"
        )
        save_weight(WEIGHT_FILE, self.user_id, self.scale.weight)
        self.ui.weight_button.setEnabled(False)
        self.update_weight_table(get_user_weights(WEIGHT_FILE, self.user_id))
        self.update_chart()

    def get_chip_id(self):
        self.reader_thread.start()
        UserMessage.create_new(self.reader_thread, "Anmeldung", LOGIN_TEXT, timeout=10)
        self.user_id = self.reader.id

    def _init_weight_table(self):
        self.ui.weight_table.setHorizontalHeaderLabels(["Zeitpunkt Messung", "Gewicht"])
        self.ui.weight_table.setRowCount(0)

    def update_weight_table(self, weights):
        self.ui.weight_table.setRowCount(len(weights))
        for row, (time, weight) in enumerate(weights):
            self.ui.weight_table.setItem(row, 0, QTableWidgetItem(time))
            self.ui.weight_table.setItem(row, 1, QTableWidgetItem(weight))

    def _init_register_tab(self):
        self.ui.user_info.setText(
            "Willkomen! Bitte registieren oder in der Benutzer-Lounge anmelden."
        )
        self.ui.user_name.setText("")

    def _log_out(self):
        self._init_weight_table()
        self.user_id = None
        self.ui.hello_user.setText("Willkommen, bitte anmelden!")
        self.ui.weight_button.setEnabled(False)
        self.ui.login_button.setEnabled(True)
        self.ui.logout_button.setEnabled(False)

    def clear_user_information(self):
        index = self.ui.tabWidget.currentIndex()
        if index == 0:
            self._log_out()
        elif index == 1:
            self._init_register_tab()


def show_user_register_error(name):
    pop_up = QMessageBox()
    pop_up.setIcon(QMessageBox.Warning)
    pop_up.setText(f"Dieser Chip ist bereits auf den Name {name} registriert.")
    pop_up.setWindowTitle("Neue Registierung nicht möglich!")
    pop_up.setStandardButtons(QMessageBox.Ok)
    pop_up.exec()


def show_user_info(title, message):
    pop_up = QMessageBox()
    pop_up.setIcon(QMessageBox.Information)
    pop_up.setText(message)
    pop_up.setWindowTitle(title)
    pop_up.setStandardButtons(QMessageBox.Ok)
    pop_up.exec()


def is_member(members, id_):
    return id_ in [id_ for member in members for id_ in member]


def load_members(file):
    return loads(file.read_text(encoding="UTF-8"))


def register_member(file, members, name, id_):
    members["members"].append({id_: name})
    file.write_text(dumps(members), encoding="UTF-8")


def save_weight(file, id_, weight):
    with open(file, "a", newline="") as csv_file:
        csv_writer = writer(
            csv_file, delimiter=",", quotechar="|", quoting=QUOTE_MINIMAL
        )
        csv_writer.writerow((id_, weight, datetime.now().strftime(TIME_FORMAT)))


def get_user_weights(file, id_):
    with open(file, newline="") as csvfile:
        reader = DictReader(csvfile)
        return [(row["timestamp"], row["weight"]) for row in reader if row["id"] == id_]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FitForFactory()
    widget.show()
    sys.exit(app.exec())
