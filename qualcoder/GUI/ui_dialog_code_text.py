# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_code_text.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_code_text(object):
    def setupUi(self, Dialog_code_text):
        Dialog_code_text.setObjectName("Dialog_code_text")
        Dialog_code_text.resize(1024, 695)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_code_text)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_code_text)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_auto_code = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_auto_code.setGeometry(QtCore.QRect(570, 0, 32, 32))
        self.pushButton_auto_code.setText("")
        self.pushButton_auto_code.setObjectName("pushButton_auto_code")
        self.label_coder = QtWidgets.QLabel(self.groupBox)
        self.label_coder.setGeometry(QtCore.QRect(10, 0, 281, 28))
        self.label_coder.setObjectName("label_coder")
        self.label_code = QtWidgets.QLabel(self.groupBox)
        self.label_code.setGeometry(QtCore.QRect(10, 87, 411, 31))
        self.label_code.setWordWrap(True)
        self.label_code.setObjectName("label_code")
        self.lineEdit_search = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_search.setGeometry(QtCore.QRect(40, 38, 171, 30))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.checkBox_search_case = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_search_case.setGeometry(QtCore.QRect(230, 38, 21, 36))
        self.checkBox_search_case.setText("")
        self.checkBox_search_case.setObjectName("checkBox_search_case")
        self.checkBox_search_all_files = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_search_all_files.setGeometry(QtCore.QRect(290, 38, 21, 36))
        self.checkBox_search_all_files.setText("")
        self.checkBox_search_all_files.setObjectName("checkBox_search_all_files")
        self.label_search_totals = QtWidgets.QLabel(self.groupBox)
        self.label_search_totals.setGeometry(QtCore.QRect(443, 44, 81, 22))
        self.label_search_totals.setAlignment(QtCore.Qt.AlignCenter)
        self.label_search_totals.setObjectName("label_search_totals")
        self.label_codes_clicked_in_text = QtWidgets.QLabel(self.groupBox)
        self.label_codes_clicked_in_text.setGeometry(QtCore.QRect(620, 46, 431, 22))
        self.label_codes_clicked_in_text.setObjectName("label_codes_clicked_in_text")
        self.label_codes_count = QtWidgets.QLabel(self.groupBox)
        self.label_codes_count.setGeometry(QtCore.QRect(570, 46, 41, 22))
        self.label_codes_count.setText("")
        self.label_codes_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_codes_count.setObjectName("label_codes_count")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(540, 30, 531, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(530, 40, 16, 91))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox_codes_in_text = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_codes_in_text.setGeometry(QtCore.QRect(550, 80, 431, 31))
        self.comboBox_codes_in_text.setObjectName("comboBox_codes_in_text")
        self.pushButton_previous = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_previous.setGeometry(QtCore.QRect(360, 38, 32, 32))
        self.pushButton_previous.setText("")
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setGeometry(QtCore.QRect(400, 38, 32, 32))
        self.pushButton_next.setText("")
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_search_all_files = QtWidgets.QLabel(self.groupBox)
        self.label_search_all_files.setGeometry(QtCore.QRect(316, 41, 24, 24))
        self.label_search_all_files.setAutoFillBackground(False)
        self.label_search_all_files.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_all_files.setText("")
        self.label_search_all_files.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_all_files.setWordWrap(True)
        self.label_search_all_files.setObjectName("label_search_all_files")
        self.label_search_case_sensitive = QtWidgets.QLabel(self.groupBox)
        self.label_search_case_sensitive.setGeometry(QtCore.QRect(250, 41, 24, 24))
        self.label_search_case_sensitive.setAutoFillBackground(False)
        self.label_search_case_sensitive.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_case_sensitive.setText("")
        self.label_search_case_sensitive.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_case_sensitive.setWordWrap(True)
        self.label_search_case_sensitive.setObjectName("label_search_case_sensitive")
        self.pushButton_auto_code_frag_this_file = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_auto_code_frag_this_file.setGeometry(QtCore.QRect(610, 0, 32, 32))
        self.pushButton_auto_code_frag_this_file.setText("")
        self.pushButton_auto_code_frag_this_file.setObjectName("pushButton_auto_code_frag_this_file")
        self.pushButton_auto_code_frag_all_files = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_auto_code_frag_all_files.setGeometry(QtCore.QRect(650, 0, 32, 32))
        self.pushButton_auto_code_frag_all_files.setText("")
        self.pushButton_auto_code_frag_all_files.setObjectName("pushButton_auto_code_frag_all_files")
        self.pushButton_auto_code_undo = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_auto_code_undo.setGeometry(QtCore.QRect(730, 0, 32, 32))
        self.pushButton_auto_code_undo.setText("")
        self.pushButton_auto_code_undo.setObjectName("pushButton_auto_code_undo")
        self.pushButton_delete_all_codes = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete_all_codes.setGeometry(QtCore.QRect(780, 0, 32, 32))
        self.pushButton_delete_all_codes.setText("")
        self.pushButton_delete_all_codes.setObjectName("pushButton_delete_all_codes")
        self.pushButton_annotate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_annotate.setGeometry(QtCore.QRect(380, 0, 32, 32))
        self.pushButton_annotate.setText("")
        self.pushButton_annotate.setObjectName("pushButton_annotate")
        self.pushButton_coding_memo = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_coding_memo.setGeometry(QtCore.QRect(420, 0, 32, 32))
        self.pushButton_coding_memo.setText("")
        self.pushButton_coding_memo.setObjectName("pushButton_coding_memo")
        self.label_font_size = QtWidgets.QLabel(self.groupBox)
        self.label_font_size.setGeometry(QtCore.QRect(470, 2, 24, 24))
        self.label_font_size.setAutoFillBackground(False)
        self.label_font_size.setFrameShape(QtWidgets.QFrame.Box)
        self.label_font_size.setText("")
        self.label_font_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_font_size.setWordWrap(True)
        self.label_font_size.setObjectName("label_font_size")
        self.spinBox_font_size = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_font_size.setGeometry(QtCore.QRect(500, 0, 53, 30))
        self.spinBox_font_size.setMinimum(6)
        self.spinBox_font_size.setMaximum(32)
        self.spinBox_font_size.setProperty("value", 12)
        self.spinBox_font_size.setObjectName("spinBox_font_size")
        self.label_search_regex = QtWidgets.QLabel(self.groupBox)
        self.label_search_regex.setGeometry(QtCore.QRect(10, 41, 24, 24))
        self.label_search_regex.setAutoFillBackground(False)
        self.label_search_regex.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_regex.setText("")
        self.label_search_regex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_regex.setWordWrap(True)
        self.label_search_regex.setObjectName("label_search_regex")
        self.pushButton_auto_code_surround = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_auto_code_surround.setGeometry(QtCore.QRect(690, 0, 32, 32))
        self.pushButton_auto_code_surround.setText("")
        self.pushButton_auto_code_surround.setObjectName("pushButton_auto_code_surround")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Dialog_code_text)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftsplitter = QtWidgets.QSplitter(self.splitter)
        self.leftsplitter.setOrientation(QtCore.Qt.Vertical)
        self.leftsplitter.setObjectName("leftsplitter")
        self.listWidget = QtWidgets.QListWidget(self.leftsplitter)
        self.listWidget.setObjectName("listWidget")
        self.groupBox_file_buttons = QtWidgets.QGroupBox(self.leftsplitter)
        self.groupBox_file_buttons.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_file_buttons.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_file_buttons.setTitle("")
        self.groupBox_file_buttons.setObjectName("groupBox_file_buttons")
        self.pushButton_latest = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_latest.setGeometry(QtCore.QRect(40, 0, 28, 28))
        self.pushButton_latest.setText("")
        self.pushButton_latest.setObjectName("pushButton_latest")
        self.pushButton_bookmark_go = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_bookmark_go.setGeometry(QtCore.QRect(80, 0, 28, 28))
        self.pushButton_bookmark_go.setText("")
        self.pushButton_bookmark_go.setObjectName("pushButton_bookmark_go")
        self.pushButton_next_file = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_next_file.setGeometry(QtCore.QRect(0, 0, 28, 28))
        self.pushButton_next_file.setText("")
        self.pushButton_next_file.setObjectName("pushButton_next_file")
        self.pushButton_document_memo = QtWidgets.QPushButton(self.groupBox_file_buttons)
        self.pushButton_document_memo.setGeometry(QtCore.QRect(120, 0, 28, 28))
        self.pushButton_document_memo.setText("")
        self.pushButton_document_memo.setObjectName("pushButton_document_memo")
        self.treeWidget = QtWidgets.QTreeWidget(self.leftsplitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.groupBox_coding_buttons = QtWidgets.QGroupBox(self.leftsplitter)
        self.groupBox_coding_buttons.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_coding_buttons.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_coding_buttons.setTitle("")
        self.groupBox_coding_buttons.setObjectName("groupBox_coding_buttons")
        self.pushButton_show_all_codings = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_show_all_codings.setGeometry(QtCore.QRect(90, 0, 28, 28))
        self.pushButton_show_all_codings.setText("")
        self.pushButton_show_all_codings.setObjectName("pushButton_show_all_codings")
        self.pushButton_show_codings_prev = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_show_codings_prev.setGeometry(QtCore.QRect(10, 0, 28, 28))
        self.pushButton_show_codings_prev.setText("")
        self.pushButton_show_codings_prev.setObjectName("pushButton_show_codings_prev")
        self.pushButton_show_codings_next = QtWidgets.QPushButton(self.groupBox_coding_buttons)
        self.pushButton_show_codings_next.setGeometry(QtCore.QRect(50, 0, 28, 28))
        self.pushButton_show_codings_next.setText("")
        self.pushButton_show_codings_next.setObjectName("pushButton_show_codings_next")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(Dialog_code_text)
        QtCore.QMetaObject.connectSlotsByName(Dialog_code_text)
        Dialog_code_text.setTabOrder(self.lineEdit_search, self.pushButton_previous)
        Dialog_code_text.setTabOrder(self.pushButton_previous, self.pushButton_next)
        Dialog_code_text.setTabOrder(self.pushButton_next, self.checkBox_search_case)
        Dialog_code_text.setTabOrder(self.checkBox_search_case, self.checkBox_search_all_files)
        Dialog_code_text.setTabOrder(self.checkBox_search_all_files, self.pushButton_auto_code)
        Dialog_code_text.setTabOrder(self.pushButton_auto_code, self.comboBox_codes_in_text)
        Dialog_code_text.setTabOrder(self.comboBox_codes_in_text, self.textEdit)

    def retranslateUi(self, Dialog_code_text):
        _translate = QtCore.QCoreApplication.translate
        Dialog_code_text.setWindowTitle(_translate("Dialog_code_text", "Code Text"))
        self.pushButton_auto_code.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Auto code with exact text</p></body></html>"))
        self.label_coder.setText(_translate("Dialog_code_text", "Coder:"))
        self.label_code.setText(_translate("Dialog_code_text", "Right click below to create new codes and categories"))
        self.lineEdit_search.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Search for text.</p><p>check <span style=\" font-weight:600;\">Case sensitive</span> for case sensitive search</p><p>check <span style=\" font-weight:600;\">All files</span> for searching all files search</p></body></html>"))
        self.checkBox_search_case.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>search case sensitive</p></body></html>"))
        self.checkBox_search_all_files.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>search all files</p></body></html>"))
        self.label_search_totals.setText(_translate("Dialog_code_text", "0 / 0"))
        self.label_codes_clicked_in_text.setText(_translate("Dialog_code_text", "No overlapping codes"))
        self.pushButton_previous.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Previous</p></body></html>"))
        self.pushButton_next.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Next</p></body></html>"))
        self.label_search_all_files.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Search text. All text files.</p></body></html>"))
        self.label_search_case_sensitive.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Search text. Case sensitive</p></body></html>"))
        self.pushButton_auto_code_frag_this_file.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Text fragment to auto code sentences. This file.</p></body></html>"))
        self.pushButton_auto_code_frag_all_files.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Text fragment to auto code sentences. All files.</p></body></html>"))
        self.pushButton_auto_code_undo.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Undo auto coding</p></body></html>"))
        self.pushButton_delete_all_codes.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Delete all codes by this coder from this file</p></body></html>"))
        self.pushButton_annotate.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Annotate selection</p></body></html>"))
        self.pushButton_coding_memo.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Memo for this coded section</p></body></html>"))
        self.label_font_size.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Text font size</p></body></html>"))
        self.spinBox_font_size.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Text font size</p></body></html>"))
        self.label_search_regex.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Search uses Regex functions. </p><p>A dot ‘.’ is used as a wild card, e.g. ‘.ears’ will match ‘bears’ and ‘years’. </p><p>A ‘?’ after a character will match one or none times that character, e.g. ‘bears?’ will match ‘bear’ and ‘bears’ </p><p><span style=\" background-color:transparent;\">A ‘*’ after a character will match zero or more times. </span></p><p><span style=\" background-color:transparent;\">‘</span>\\. will match the dot symbol, ‘\\?’ will match the question mark. ‘\\n’ will match the line ending symbol. </p><p>Regex cheatsheet: <a href=\"http://www.rexegg.com/regex-quickstart.html\"><span style=\" text-decoration: underline; color:#000080;\">www.rexegg.com/regex-quickstart.html</span></a></p></body></html>"))
        self.pushButton_auto_code_surround.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Auto code using start and end marks.</p></body></html>"))
        self.pushButton_latest.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>File with latest coding</p></body></html>"))
        self.pushButton_bookmark_go.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Go to bookmark</p></body></html>"))
        self.pushButton_next_file.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Next file</p></body></html>"))
        self.pushButton_document_memo.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>File memo</p></body></html>"))
        self.pushButton_show_all_codings.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Show all codings</p></body></html>"))
        self.pushButton_show_codings_prev.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Show previous coding of selected code</p></body></html>"))
        self.pushButton_show_codings_next.setToolTip(_translate("Dialog_code_text", "<html><head/><body><p>Show next coding of selected code.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_code_text = QtWidgets.QDialog()
    ui = Ui_Dialog_code_text()
    ui.setupUi(Dialog_code_text)
    Dialog_code_text.show()
    sys.exit(app.exec_())
