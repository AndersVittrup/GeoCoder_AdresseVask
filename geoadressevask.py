# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoCoder_AdresseVask
                                 A QGIS plugin
 AdresseVask med Geokodning
                              -------------------
        begin                : 2016-03-18
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Anders Vittrup
        email                : avit@orbicon.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QApplication
import processing
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from geoadressevask_dialog import GeoCoder_AdresseVaskDialog
import os.path


class GeoCoder_AdresseVask:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeoCoder_AdresseVask_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = GeoCoder_AdresseVaskDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&AdresseVask GeoCoder')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'GeoCoder_AdresseVask')
        self.toolbar.setObjectName(u'GeoCoder_AdresseVask')
        
        self.dlg.lineEdit.clear()
        self.dlg.pushButton_2.clicked.connect(self.select_output_file)
        
        self.dlg.pushButton.clicked.connect(self.geocode)
        

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('GeoCoder_AdresseVask', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action
        

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/GeoCoder_AdresseVask/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Adressevask og Geocodning'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&AdresseVask GeoCoder'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar      

    def layerCol(self, layer):
        self.dlg.mFieldComboBox.setLayer(layer)
        
    def select_output_file(self):
        filename = QFileDialog.getSaveFileName(self.dlg, "Gem fil","", '*.shp')
        self.dlg.lineEdit.setText(filename)
        
    def geocode(self):
        
        self.dlg.pushButton.setDisabled( True )
        print "Geocode"
        
        layer = self.dlg.mMapLayerComboBox.currentLayer()
        layer_field_index = layer.fieldNameIndex(self.dlg.mFieldComboBox.currentField())

        # prepare
        features = processing.features(layer)
        
        count = 0
        total = 0
        for f in features:
            total +=1
            
        features = processing.features(layer)
        

        for f in features:
            count += 1
            self.dlg.progressBar.setValue(int(100 * total / count))
            print int(100 * count / total)
            #print f.attributes()[layer_field_index]
        
    def run(self):
        """Run method that performs all the real work"""
        
        #connecting layerCombo with fieldCombo and setting first layer
        vlayer = self.dlg.mMapLayerComboBox.currentLayer()
        self.dlg.mFieldComboBox.setLayer(vlayer)
        self.dlg.mMapLayerComboBox.layerChanged.connect(self.layerCol)
        
        self.dlg.lineEdit.clear()
        
        self.dlg.pushButton.setDisabled( False )
        self.dlg.progressBar.setValue(0)

        # show the dialog
        self.dlg.show()
            

