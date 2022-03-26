# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CsvtoMAp
                                 A QGIS plugin
 This plugin imports .csv files and creates .shp files based on the treshold values and prefed colour coding and legends for the forecast of IMD data.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-10-01
        copyright            : (C) 2021 by Ashish
        email                : ashishjain202027@gmail.com
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
    """Load CsvtoMAp class from file CsvtoMAp.
    
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    from .csv_to_map import CsvtoMAp
    return CsvtoMAp(iface)