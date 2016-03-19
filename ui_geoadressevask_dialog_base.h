/********************************************************************************
** Form generated from reading UI file 'geoadressevask_dialog_basegq9136.ui'
**
** Created by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/
pluginType = MODULE
def moduleInformation():
     return "qgis.gui", ("QgsMapLayerCombobox", "QgsMapLayerProxyModel" )

#ifndef GEOADRESSEVASK_DIALOG_BASEGQ9136_H
#define GEOADRESSEVASK_DIALOG_BASEGQ9136_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include "qgsfieldcombobox.h"
#include "qgsmaplayercombobox.h"

QT_BEGIN_NAMESPACE

class Ui_GeoCoder_AdresseVaskDialogBase
{
public:
    QDialogButtonBox *button_box;
    QLabel *layerLabel;
    QLabel *colmLabel;
    QgsFieldComboBox *mFieldComboBox;
    QgsMapLayerComboBox *mMapLayerComboBox;

    void setupUi(QDialog *GeoCoder_AdresseVaskDialogBase)
    {
        if (GeoCoder_AdresseVaskDialogBase->objectName().isEmpty())
            GeoCoder_AdresseVaskDialogBase->setObjectName(QString::fromUtf8("GeoCoder_AdresseVaskDialogBase"));
        GeoCoder_AdresseVaskDialogBase->resize(400, 189);
        button_box = new QDialogButtonBox(GeoCoder_AdresseVaskDialogBase);
        button_box->setObjectName(QString::fromUtf8("button_box"));
        button_box->setGeometry(QRect(50, 150, 341, 32));
        button_box->setOrientation(Qt::Horizontal);
        button_box->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        layerLabel = new QLabel(GeoCoder_AdresseVaskDialogBase);
        layerLabel->setObjectName(QString::fromUtf8("layerLabel"));
        layerLabel->setGeometry(QRect(10, 20, 221, 16));
        colmLabel = new QLabel(GeoCoder_AdresseVaskDialogBase);
        colmLabel->setObjectName(QString::fromUtf8("colmLabel"));
        colmLabel->setGeometry(QRect(10, 90, 221, 16));
        mFieldComboBox = new QgsFieldComboBox(GeoCoder_AdresseVaskDialogBase);
        mFieldComboBox->setObjectName(QString::fromUtf8("mFieldComboBox"));
        mFieldComboBox->setGeometry(QRect(9, 110, 381, 27));
        mMapLayerComboBox = new QgsMapLayerComboBox(GeoCoder_AdresseVaskDialogBase);
        mMapLayerComboBox->setObjectName(QString::fromUtf8("mMapLayerComboBox"));
        mMapLayerComboBox->setGeometry(QRect(10, 40, 381, 27));
        mMapLayerComboBox->setFilters(QgsMapLayerProxyModel::HasGeometry|QgsMapLayerProxyModel::LineLayer|QgsMapLayerProxyModel::NoGeometry|QgsMapLayerProxyModel::PluginLayer|QgsMapLayerProxyModel::PointLayer|QgsMapLayerProxyModel::PolygonLayer|QgsMapLayerProxyModel::VectorLayer);

        retranslateUi(GeoCoder_AdresseVaskDialogBase);
        QObject::connect(button_box, SIGNAL(accepted()), GeoCoder_AdresseVaskDialogBase, SLOT(accept()));
        QObject::connect(button_box, SIGNAL(rejected()), GeoCoder_AdresseVaskDialogBase, SLOT(reject()));

        QMetaObject::connectSlotsByName(GeoCoder_AdresseVaskDialogBase);
    } // setupUi

    void retranslateUi(QDialog *GeoCoder_AdresseVaskDialogBase)
    {
        GeoCoder_AdresseVaskDialogBase->setWindowTitle(QApplication::translate("GeoCoder_AdresseVaskDialogBase", "AdresseVask GeoCoder", 0, QApplication::UnicodeUTF8));
        layerLabel->setText(QApplication::translate("GeoCoder_AdresseVaskDialogBase", "V\303\246lg lag til geokodning:", 0, QApplication::UnicodeUTF8));
        colmLabel->setText(QApplication::translate("GeoCoder_AdresseVaskDialogBase", "V\303\246lg kolonne med adresse:", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class GeoCoder_AdresseVaskDialogBase: public Ui_GeoCoder_AdresseVaskDialogBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GEOADRESSEVASK_DIALOG_BASEGQ9136_H
