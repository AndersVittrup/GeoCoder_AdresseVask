# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geoadressevask_dialog_base.ui'
#
# Created: Sat Mar 19 17:05:08 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GeoCoder_AdresseVaskDialogBase(object):
    def setupUi(self, GeoCoder_AdresseVaskDialogBase):
        GeoCoder_AdresseVaskDialogBase.setObjectName(_fromUtf8("GeoCoder_AdresseVaskDialogBase"))
        GeoCoder_AdresseVaskDialogBase.resize(400, 189)
        self.button_box = QtGui.QDialogButtonBox(GeoCoder_AdresseVaskDialogBase)
        self.button_box.setGeometry(QtCore.QRect(50, 150, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.layerLabel = QtGui.QLabel(GeoCoder_AdresseVaskDialogBase)
        self.layerLabel.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.layerLabel.setObjectName(_fromUtf8("layerLabel"))
        self.colmLabel = QtGui.QLabel(GeoCoder_AdresseVaskDialogBase)
        self.colmLabel.setGeometry(QtCore.QRect(10, 90, 221, 16))
        self.colmLabel.setObjectName(_fromUtf8("colmLabel"))
        self.mFieldComboBox = QgsFieldComboBox(GeoCoder_AdresseVaskDialogBase)
        self.mFieldComboBox.setGeometry(QtCore.QRect(9, 110, 381, 27))
        self.mFieldComboBox.setObjectName(_fromUtf8("mFieldComboBox"))
        self.mMapLayerComboBox = QgsMapLayerComboBox(GeoCoder_AdresseVaskDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(10, 40, 381, 27))
