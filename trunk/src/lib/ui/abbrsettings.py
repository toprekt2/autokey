#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from uic/abbrsettings.ui on Tue Jul 28 15:29:17 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.abbrLabel = QtGui.QLabel(Form)
        self.abbrLabel.setObjectName("abbrLabel")
        self.horizontalLayout.addWidget(self.abbrLabel)
        self.abbrLineEdit = KLineEdit(Form)
        self.abbrLineEdit.setObjectName("abbrLineEdit")
        self.horizontalLayout.addWidget(self.abbrLineEdit)
        self.triggerOnLabel = QtGui.QLabel(Form)
        self.triggerOnLabel.setObjectName("triggerOnLabel")
        self.horizontalLayout.addWidget(self.triggerOnLabel)
        self.wordCharCombo = KComboBox(Form)
        self.wordCharCombo.setObjectName("wordCharCombo")
        self.horizontalLayout.addWidget(self.wordCharCombo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.removeTypedCheckbox = QtGui.QCheckBox(Form)
        self.removeTypedCheckbox.setObjectName("removeTypedCheckbox")
        self.verticalLayout.addWidget(self.removeTypedCheckbox)
        self.omitTriggerCheckbox = QtGui.QCheckBox(Form)
        self.omitTriggerCheckbox.setObjectName("omitTriggerCheckbox")
        self.verticalLayout.addWidget(self.omitTriggerCheckbox)
        self.matchCaseCheckbox = QtGui.QCheckBox(Form)
        self.matchCaseCheckbox.setObjectName("matchCaseCheckbox")
        self.verticalLayout.addWidget(self.matchCaseCheckbox)
        self.ignoreCaseCheckbox = QtGui.QCheckBox(Form)
        self.ignoreCaseCheckbox.setObjectName("ignoreCaseCheckbox")
        self.verticalLayout.addWidget(self.ignoreCaseCheckbox)
        self.triggerInsideCheckbox = QtGui.QCheckBox(Form)
        self.triggerInsideCheckbox.setObjectName("triggerInsideCheckbox")
        self.verticalLayout.addWidget(self.triggerInsideCheckbox)
        self.immediateCheckbox = QtGui.QCheckBox(Form)
        self.immediateCheckbox.setObjectName("immediateCheckbox")
        self.verticalLayout.addWidget(self.immediateCheckbox)
        self.kseparator = KSeparator(Form)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n("Form"))
        self.abbrLabel.setText(kdecore.i18n("Abbreviation:"))
        self.triggerOnLabel.setText(kdecore.i18n("Trigger on:"))
        self.removeTypedCheckbox.setText(kdecore.i18n("Remove typed abbreviation"))
        self.omitTriggerCheckbox.setText(kdecore.i18n("Omit trigger character"))
        self.matchCaseCheckbox.setText(kdecore.i18n("Match phrase case to typed abbreviation"))
        self.ignoreCaseCheckbox.setText(kdecore.i18n("Ignore case of typed abbreviation"))
        self.triggerInsideCheckbox.setText(kdecore.i18n("Trigger when typed as part of a word"))
        self.immediateCheckbox.setText(kdecore.i18n("Trigger immediately (don\'t require a trigger character)"))

from PyKDE4.kdeui import KSeparator, KLineEdit, KComboBox
