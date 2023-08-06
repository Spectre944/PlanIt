# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

import json
from typing import Any, List, Dict, Union

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
#from PySide6.QtCore import QObject, pyqtProperty
from PySide6.QtWidgets import QTreeView, QApplication, QHeaderView
from PySide6.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QFileInfo

from PlanModel import JsonModel  # Assuming you named your model class tree_model.py
#My classes
from SceTreeModel import SceTreeModel
from SceTableModel import SceTableModel
from SceJsonWork import SceJsonWork


if __name__ == "__main__":

    app = QApplication(sys.argv)
    model = JsonModel()
    JsonWork = SceJsonWork()

    json_path = QFileInfo(__file__).absoluteDir().filePath("example.json")

    JsonWork.loadJson(json_path)
    JsonWork.getByKey('task');




    with open(json_path) as file:
        document = json.load(file)
        model.load(document)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("treeModel", model)

    # Load the QML file
    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


