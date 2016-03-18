# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoCoder_AdresseVask
                                 A QGIS plugin
 AdresseVask med Geokodning
                             -------------------
        begin                : 2016-03-18
        copyright            : (C) 2016 by Anders Vittrup
        email                : avit@orbicon.dk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeoCoder_AdresseVask class from file GeoCoder_AdresseVask.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geoadressevask import GeoCoder_AdresseVask
    return GeoCoder_AdresseVask(iface)
