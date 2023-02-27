import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from RIRP import RIRP



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 620, 1071, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(380, 30, 711, 581))
        self.widget.setObjectName("widget")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 80, 671, 491))
        self.graphicsView.setObjectName("graphicsView")
        self.gb_graph_settings = QtWidgets.QGroupBox(self.widget)
        self.gb_graph_settings.setGeometry(QtCore.QRect(20, 10, 661, 61))
        self.gb_graph_settings.setObjectName("gb_graph_settings")
        self.combo_graph_band = QtWidgets.QComboBox(self.gb_graph_settings)
        self.combo_graph_band.setGeometry(QtCore.QRect(260, 30, 101, 21))
        self.combo_graph_band.setObjectName("combo_graph_band")
        self.label_band = QtWidgets.QLabel(self.gb_graph_settings)
        self.label_band.setGeometry(QtCore.QRect(220, 30, 68, 19))
        self.label_band.setObjectName("label_band")
        self.combo_graph_parameter = QtWidgets.QComboBox(self.gb_graph_settings)
        self.combo_graph_parameter.setGeometry(QtCore.QRect(90, 30, 101, 21))
        self.combo_graph_parameter.setObjectName("combo_graph_parameter")
        self.label_parameter = QtWidgets.QLabel(self.gb_graph_settings)
        self.label_parameter.setGeometry(QtCore.QRect(10, 30, 81, 19))
        self.label_parameter.setObjectName("label_parameter")
        self.pb_download_graph = QtWidgets.QPushButton(self.gb_graph_settings)
        self.pb_download_graph.setGeometry(QtCore.QRect(520, 30, 131, 21))
        self.pb_download_graph.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 160, 341, 231))
        self.groupBox.setObjectName("groupBox")
        
        ### File selection
        self.gb_file_selection = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_file_selection.setGeometry(QtCore.QRect(30, 30, 341, 121))
        self.gb_file_selection.setObjectName("gb_file_selection")
        self.pb_load_signal = QtWidgets.QPushButton(self.gb_file_selection)
        self.pb_load_signal.setGeometry(QtCore.QRect(210, 60, 91, 34))
        self.pb_load_signal.setObjectName("pb_load_signal")
        self.groupBox_7 = QtWidgets.QGroupBox(self.gb_file_selection)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 30, 161, 81))
        self.groupBox_7.setObjectName("groupBox_7")
        self.rb_impulse_response = QtWidgets.QRadioButton(self.groupBox_7)
        self.rb_impulse_response.setGeometry(QtCore.QRect(10, 20, 141, 23))
        self.rb_impulse_response.setObjectName("rb_impulse_response")
        self.rb_sine_sweep = QtWidgets.QRadioButton(self.groupBox_7)
        self.rb_sine_sweep.setGeometry(QtCore.QRect(10, 50, 119, 23))
        self.rb_sine_sweep.setObjectName("rb_sine_sweep")
        # Initial state
        self.rb_impulse_response.setChecked(True)
        
        ### Filtering settings
        # Bands
        self.gb_bands = QtWidgets.QGroupBox(self.groupBox)
        self.gb_bands.setGeometry(QtCore.QRect(20, 30, 301, 61))
        self.gb_bands.setObjectName("gb_bands")
        self.rb_octave_bands = QtWidgets.QRadioButton(self.gb_bands)
        self.rb_octave_bands.setGeometry(QtCore.QRect(10, 30, 121, 23))
        self.rb_octave_bands.setObjectName("rb_octave_bands")
        self.rb_third_octave_bands = QtWidgets.QRadioButton(self.gb_bands)
        self.rb_third_octave_bands.setGeometry(QtCore.QRect(130, 30, 151, 23))
        self.rb_third_octave_bands.setObjectName("rb_third_octave_bands")
        # Frequencies
        self.gb_frequencies = QtWidgets.QGroupBox(self.groupBox)
        self.gb_frequencies.setGeometry(QtCore.QRect(20, 100, 301, 91))
        self.gb_frequencies.setObjectName("gb_frequencies")
        self.label_minimum_band = QtWidgets.QLabel(self.gb_frequencies)
        self.label_minimum_band.setGeometry(QtCore.QRect(40, 30, 68, 19))
        self.label_minimum_band.setObjectName("label_minimum_band")
        self.label_maximum_band = QtWidgets.QLabel(self.gb_frequencies)
        self.label_maximum_band.setGeometry(QtCore.QRect(40, 60, 71, 19))
        self.label_maximum_band.setObjectName("label_maximum_band")
        self.comboBox = QtWidgets.QComboBox(self.gb_frequencies)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 121, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.gb_frequencies)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 60, 121, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        # Initial state
        self.rb_octave_bands.setChecked(True)
        # Frequencies lists boxes
        if self.rb_octave_bands.isChecked():
            bands_freqs = ['31.5 Hz', '63 Hz', '125 Hz', '250 Hz', '500 Hz', '1 kHz', '2 kHz', '4 kHz', '8 kHz', '16 kHz']
            
        if self.rb_third_octave_bands.isChecked():
            bands_freqs = ['31.5 Hz', '40 Hz', '50 Hz', '63 Hz', '80 Hz', '100 Hz', '125 Hz', '160 Hz', '200 Hz', '250 Hz',
            '315 Hz', '400 Hz','500 Hz', '630 Hz', '800 Hz', '1 kHz', '1.25 kHz', '1.6 kHz', '2 kHz', '2.5 kHz',
            '3.15 kHz', '4 kHz', '5 kHz', '6.3 kHz', '8 kHz', '10 kHz', '12.5 kHz', '16 kHz']   
        self.comboBox.addItems(bands_freqs)
        self.comboBox_2.addItems(bands_freqs)
        # Reversed filtering
        self.cb_reversed_filtering = QtWidgets.QCheckBox(self.groupBox)
        self.cb_reversed_filtering.setGeometry(QtCore.QRect(110, 200, 121, 23))
        self.cb_reversed_filtering.setObjectName("cb_reversed_filtering")
        # Initial state
        self.comboBox.setCurrentText('63 Hz')
        self.comboBox_2.setCurrentText('8 kHz')

        
        ### Smoothing settings
        self.gb_smoothing_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_smoothing_settings.setGeometry(QtCore.QRect(30, 410, 341, 61))
        self.gb_smoothing_settings.setObjectName("gb_smoothing_settings")
        self.rb_shroeder = QtWidgets.QRadioButton(self.gb_smoothing_settings)
        self.rb_shroeder.setGeometry(QtCore.QRect(30, 30, 119, 23))
        self.rb_shroeder.setObjectName("rb_shroeder")
        self.rb_moving_median = QtWidgets.QRadioButton(self.gb_smoothing_settings)
        self.rb_moving_median.setGeometry(QtCore.QRect(150, 30, 151, 23))
        self.rb_moving_median.setObjectName("rb_moving_median")
        # Initial state
        self.rb_shroeder.setChecked(True)
        
        ### Noise compensation
        self.gb_noise_compensation = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_noise_compensation.setGeometry(QtCore.QRect(30, 490, 341, 61))
        self.gb_noise_compensation.setObjectName("gb_noise_compensation")
        self.rb_lundeby = QtWidgets.QRadioButton(self.gb_noise_compensation)
        self.rb_lundeby.setGeometry(QtCore.QRect(30, 30, 119, 23))
        self.rb_lundeby.setObjectName("rb_lundeby")
        self.rb_chu = QtWidgets.QRadioButton(self.gb_noise_compensation)
        self.rb_chu.setGeometry(QtCore.QRect(120, 30, 151, 23))
        self.rb_chu.setObjectName("rb_chu")
        self.rb_no_compensation = QtWidgets.QRadioButton(self.gb_noise_compensation)
        self.rb_no_compensation.setGeometry(QtCore.QRect(180, 30, 141, 23))
        self.rb_no_compensation.setObjectName("rb_no_compensation")
        # Initial state
        self.rb_lundeby.setChecked(True)
        
        self.pb_calculate_parameters = QtWidgets.QPushButton(self.centralwidget)
        self.pb_calculate_parameters.setGeometry(QtCore.QRect(210, 570, 161, 34))
        self.pb_calculate_parameters.setObjectName("pb_calculate_parameters")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Room Impulse Response "))
        self.gb_graph_settings.setTitle(_translate("MainWindow", "Graph settings"))
        self.label_band.setText(_translate("MainWindow", "Band"))
        self.label_parameter.setText(_translate("MainWindow", "Parameter"))
        self.pb_download_graph.setText(_translate("MainWindow", "Download graph"))
        self.groupBox.setTitle(_translate("MainWindow", "Filtering settings"))
        self.gb_bands.setTitle(_translate("MainWindow", "Bands"))
        self.rb_octave_bands.setText(_translate("MainWindow", "Octave bands"))
        self.rb_third_octave_bands.setText(_translate("MainWindow", "Third octave bands"))
        self.gb_frequencies.setTitle(_translate("MainWindow", "Frequencies"))
        self.label_minimum_band.setText(_translate("MainWindow", "Minimum band"))
        self.label_maximum_band.setText(_translate("MainWindow", "Maximum band"))
        self.cb_reversed_filtering.setText(_translate("MainWindow", "Reversed filtering"))
        self.gb_smoothing_settings.setTitle(_translate("MainWindow", "Smoothing settings"))
        self.rb_shroeder.setText(_translate("MainWindow", "Schroeder"))
        self.rb_moving_median.setText(_translate("MainWindow", "Moving Median"))
        self.gb_file_selection.setTitle(_translate("MainWindow", "File selection"))
        self.pb_load_signal.setText(_translate("MainWindow", "Load signal"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Type"))
        self.rb_impulse_response.setText(_translate("MainWindow", "Impulse response"))
        self.rb_sine_sweep.setText(_translate("MainWindow", "Sine sweep"))
        self.pb_calculate_parameters.setText(_translate("MainWindow", "Calculate parameters"))
        self.gb_noise_compensation.setTitle(_translate("MainWindow", "Noise compensation"))
        self.rb_lundeby.setText(_translate("MainWindow", "Lundeby"))
        self.rb_chu.setText(_translate("MainWindow", "Chu"))
        self.rb_no_compensation.setText(_translate("MainWindow", "No compensation"))

        # Connections
        self.backend = RIRP()
        self.pb_load_signal.clicked.connect(self.load_signal_dialog)
        self.rb_third_octave_bands.toggled.connect(self.refresh_frequencies)
        self.pb_calculate_parameters.clicked.connect(self.calculate_parameters)

    ### Methods
    
    def load_signal_dialog(self):
        dialog_response = QtWidgets.QFileDialog.getOpenFileName(
            caption = 'Select a signal to process',
            directory = os.getcwd()
        )
        self.signal_path = dialog_response[0]
        ### Copy file into folder audio_tests/
        # file_name = signal_path.split('/')[-1]
        # audio_test_path = os.path.join(os.getcwd(),'audio_tests')
        # new_signal_path = os.path.join(audio_test_path,file_name)
        # shutil.copyfile(signal_path, new_signal_path)
        # self.signal_path = new_signal_path
        
    
    def refresh_frequencies(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        
        if self.rb_octave_bands.isChecked():
            bands_freqs = ['31.5 Hz', '63 Hz', '125 Hz', '250 Hz', '500 Hz', '1 kHz', '2 kHz', '4 kHz', '8 kHz', '16 kHz']
            
        if self.rb_third_octave_bands.isChecked():
            bands_freqs = ['31.5 Hz', '40 Hz', '50 Hz', '63 Hz', '80 Hz', '100 Hz', '125 Hz', '160 Hz', '200 Hz', '250 Hz',
            '315 Hz', '400 Hz','500 Hz', '630 Hz', '800 Hz', '1 kHz', '1.25 kHz', '1.6 kHz', '2 kHz', '2.5 kHz',
            '3.15 kHz', '4 kHz', '5 kHz', '6.3 kHz', '8 kHz', '10 kHz', '12.5 kHz', '16 kHz']   
        
        self.comboBox.addItems(bands_freqs)
        self.comboBox_2.addItems(bands_freqs)
        
        self.comboBox.setCurrentText('63 Hz')
        self.comboBox_2.setCurrentText('8 kHz')
    
    def configure_table(self,parameters_labels, bands_labels):
        
        self.tableWidget.setRowCount(len(parameters_labels))
        self.tableWidget.setColumnCount(len(bands_labels))
        self.tableWidget.setHorizontalHeaderLabels(bands_labels)
        self.tableWidget.setVerticalHeaderLabels(parameters_labels)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
    
    def write_table(self, data_i, band_i):
            
        for i, item in enumerate(data_i.values()):
            item_i = QtWidgets.QTableWidgetItem(str(item))
            self.tableWidget.setItem(i,band_i,item_i)
        
    
    def calculate_parameters(self):
        # data
        # self.write_table(data)
        ### Frequency boundaries
        minimum_band_text = self.comboBox.currentText()
        maximum_band_text = self.comboBox_2.currentText()
        
        minimum_band_value = float(minimum_band_text.split(' ')[0])
        if 'k' in minimum_band_text.split(' ')[1]:
            minimum_band_value *= 1000
            
        maximum_band_value = float(maximum_band_text.split(' ')[0])
        if 'k' in maximum_band_text.split(' ')[1]:
            maximum_band_value *= 1000
        
        ### Signal type
        IR, fs = self.backend.load_signal(self.signal_path)
        if self.rb_sine_sweep.isChecked():
            IR, fs = self.backend.get_ir_from_sinesweep(minimum_band_value*(1/np.sqrt(2)),
                                                       maximum_band_value*np.sqrt(2))
        
        ### Filter settings
        # Bands per octave
        if self.rb_octave_bands.isChecked():
            bands_per_oct = 1
        else:
            bands_per_oct = 3
        
        if self.cb_reversed_filtering.isChecked():
            IR = self.backend.get_reversed_IR(IR)
        
        filtered_IR, center_freqs = self.backend.get_ir_filtered(IR, bands_per_oct)
        
        if self.cb_reversed_filtering.isChecked():
            filtered_IR = self.backend.get_reversed_IR(filtered_IR)
        
        parameters = ['Tt','EDTt','EDT','T20','T30','C50','C80']
        center_freqs_str = [str(int(np.round(band_i)))+' Hz' for band_i in center_freqs]
        center_freqs_str = center_freqs_str[
            np.argwhere(center_freqs==minimum_band_value)[0,0]:np.argwhere(center_freqs==maximum_band_value)[0,0]+1
            ]
        self.configure_table(parameters, center_freqs_str)
        self.combo_graph_band.clear()
        self.combo_graph_parameter.addItem('Energy')
        self.combo_graph_parameter.addItems(parameters)
        self.combo_graph_band.addItems(center_freqs_str)
        
        parameters_list = []
        
        for band_i , ir_i in enumerate(filtered_IR):
            ### Noise compensation
            if self.rb_lundeby.isChecked():
                crosspoint, _ = self.backend.get_lundeby_limit(ir_i)
                
            
            elif self.rb_chu.isChecked():
                crosspoint = self.backend.get_chu_compensation(ir_i)
            
            else:
                crosspoint = 0
            
            ### Smoothing settings
            if self.rb_shroeder.isChecked():
                smoothed_IR = self.backend.get_smooth_by_schroeder(ir_i, crosspoint)
            
            else:
                smoothed_IR = self.backend.get_smooth_by_median_filter(ir_i, 500)    # a definir
            
            parameters = self.backend.get_acoustical_parameters(smoothed_IR)
            parameters_list.append(parameters)
            self.write_table(parameters, band_i)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())