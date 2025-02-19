"""Meowcoin look and feel (dark style)."""

import os
from electrum.util import pkg_dir


meowcoin_stylesheet = """

/**********************/
/* Meowcoin CSS       */
/*
0. OSX Reset
1. Navigation Bar
2. Editable Fields, Labels
3. Containers
4. File Menu, Toolbar
5. Buttons, Spinners, Dropdown
6. Table Headers
7. Scroll Bar
8. Tree View
9. Dialog Boxes
*/
/**********************/


/**********************/
/* 0. OSX Reset */

QWidget { /* Set default style for QWidget, override in following statements */
    border: 0;
    selection-color: #fff;
    selection-background-color: #818181;
    font-family:Pixeloid Sans;
}

QGroupBox {
    margin-top: 1em;
    color: #ccc;
}

QGroupBox::title {
    subcontrol-origin: margin;
}

/**********************/
/* 1. Navigation Bar */

#main_window_nav_bar {
    border:0;
}

#main_window_nav_bar > QStackedWidget {
    border-top: 2px solid #fff;
    background-color: #232629;
}

#main_window_nav_bar > QTabBar{
    color: #fff;
    border:0;
}

#main_window_nav_bar > QTabBar {
    background: url({pkg_dir}/gui/icons/navlogodark.png) no-repeat left top;
}

#main_window_nav_bar > QTabBar::tear {
    width: 126px;
    height: 48px;
    background: url({pkg_dir}/gui/icons/navlogodark.png) no-repeat left top;
}

#main_window_nav_bar > QTabBar::scroller {
    width: 64;
}

#main_window_nav_bar > QTabBar QToolButton {
    background-color: #181818;
}

#main_window_nav_bar > QTabBar QToolButton:hover {
    background-color: #BE840A;
    color: #fff;
}

QTabWidget#main_window_nav_bar::tab-bar {
    alignment: left;
}

QTabWidget#main_window_nav_bar::pane {
    position: absolute;
}

#main_window_nav_bar > QTabBar::tab {
    background-color:#181818;
    color:#F49930;
    min-height: 44px;
    padding-left:1em;
    padding-right:1em;
}

#main_window_nav_bar > QTabBar::tab:first {
    border-left: 0 solid #fff;
    margin-left:180px;
}

#main_window_nav_bar > QTabBar::tab:last {
    border-right: 0 solid #fff;
}

#main_window_nav_bar > QTabBar::tab:selected, #main_window_nav_bar > QTabBar::tab:hover {
    background-color:#BE840A;
    color:#fff;
}


/**********************/
/* 2. Editable Fields and Labels */

QCheckBox { /* Checkbox Labels */
    color:#aaa;
    background-color:transparent;
}

QCheckBox:hover {
    background-color:transparent;
}

QCheckBox {
    spacing: 5px;
}

QCheckBox::indicator,
QTreeWidget::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked,
QTreeWidget::indicator:unchecked {
    image:url({pkg_dir}/gui/icons/checkbox/unchecked-dark.png);
}

QCheckBox::indicator:unchecked:disabled,
QTreeWidget::indicator:unchecked:disabled {
    image:url({pkg_dir}/gui/icons/checkbox/unchecked_disabled-dark.png);
}

QCheckBox::indicator:unchecked:pressed,
QTreeWidget::indicator:unchecked:pressed {
    image:url({pkg_dir}/gui/icons/checkbox/checked.png);
}

QCheckBox::indicator:checked,
QTreeWidget::indicator:checked {
    image:url({pkg_dir}/gui/icons/checkbox/checked.png);
}

QCheckBox::indicator:checked:disabled,
QTreeWidget::indicator:checked:disabled {
    image:url({pkg_dir}/gui/icons/checkbox/checked_disabled.png);
}

QCheckBox::indicator:checked:pressed,
QTreeWidget::indicator:checked:pressed {
    image:url({pkg_dir}/gui/icons/checkbox/unchecked-dark.png);
}

QCheckBox::indicator:indeterminate,
QTreeWidget::indicator:indeterminate {
    image:url({pkg_dir}/gui/icons/checkbox/indeterminate.png);
}

QCheckBox::indicator:indeterminate:disabled,
QTreeWidget::indicator:indeterminate:disabled {
    image:url({pkg_dir}/gui/icons/checkbox/indeterminate_disabled.png);
}

QCheckBox::indicator:indeterminate:pressed,
QTreeWidget::indicator:indeterminate:pressed {
    image:url({pkg_dir}/gui/icons/checkbox/checked.png);
}

QRadioButton {
    padding: 2px;
    spacing: 5px;
    color: #ccc;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
}

QRadioButton::indicator::unchecked {
    image:url({pkg_dir}/gui/icons/radio/unchecked-dark.png);
}

QRadioButton::indicator:unchecked:disabled {
    image:url({pkg_dir}/gui/icons/radio/unchecked_disabled-dark.png);
}

QRadioButton::indicator:unchecked:pressed {
    image:url({pkg_dir}/gui/icons/radio/checked.png);
}

QRadioButton::indicator::checked {
    image:url({pkg_dir}/gui/icons/radio/checked.png);
}

QRadioButton::indicator:checked:disabled {
    image:url({pkg_dir}/gui/icons/radio/checked_disabled.png);
}

QRadioButton::indicator:checked:pressed {
    image:url({pkg_dir}/gui/icons/radio/checked.png);
}

ScanQRTextEdit, ShowQRTextEdit, ButtonsTextEdit {
    color:#aaa;
    background-color:#232629;
    border: 1px solid #BE840A;
}

QValidatedLineEdit, QLineEdit, PayToEdit { /* Text Entry Fields */
    border: 1px solid #BE840A;
    outline:0;
    padding: 5px 3px;
    background-color:#232629;
    color:#aaa;
}

QValidatedLineEdit:disabled, QLineEdit:disabled, PayToEdit:disabled {
    border: 1px solid #676767;
    background-color: #333639;
}

QValidatedLineEdit:read-only, QLineEdit:read-only, PayToEdit:read-only {
    border: 1px solid #676767;
}

PayToEdit {
    padding: 1px;
}

ButtonsLineEdit {
    color:#aaa;
    background: #232629;
}

QLabel {
    font-family:Pixeloid Sans;
    color: #aaa;
}


/**********************/
/* 3. Containers */


/* Wallet Container */
#main_window_container,
#central_widget {
    background: #181818;
    color: #BE840A;
}


/* History Container */
#history_container {
    margin-top: 0;
}


/* Send Container */
#send_container {
    margin-top: 0;
}

#send_container > QLabel {
    margin-left:10px;
    min-width:150px;
}


/* Receive Container */
#receive_container {
    margin-top: 0;
}

#receive_container > QLabel {
    margin-left:10px;
    min-width:150px;
}


/* Addressses Container */
#addresses_container {
    margin-top: 0;
    background-color: #232629;
}


/* Contacts Container */
#contacts_container, #utxo_container {
    margin-top: 0;
}


/* Console Container */
#console_container {
    margin-top: 0;
    color:#aaa;
    background-color: #232629;
}

#console_container > QWidget {
    background-color: #232629;
}


/* Balance Label */
#main_window_balance {
    color:#ffffff;
    font-weight:bold;
    margin-left:10px;
}


/**********************/
/* 4. File Menu, Toolbar */

#main_window_container QMenuBar,
#central_widget QMenuBar {
    color: #aaa;
}

QMenuBar {
    background-color: #232629;
}

QMenuBar::item {
    background-color: #232629;
    color:#aaa;
}

QMenuBar::item:selected {
    background-color: #53565b;
}

QMenu {
    background-color: #232629;
    border:1px solid #31363b;
}

QMenu::item {
    color:#aaa;
}

QMenu::item:selected {
    background-color: #53565b;
    color:#aaa;
}

QToolBar {
    background-color:#3398CC;
    border:0px solid #000;
    padding:0;
    margin:0;
}

QToolBar > QToolButton {
    background-color:#3398CC;
    border:0px solid #333;
    min-height:2.5em;
    padding: 0em 1em;
    font-weight:bold;
    color:#fff;
}

QToolBar > QToolButton:checked {
    background-color:#fff;
    color:#333;
    font-weight:bold;
}

QMessageBox {
    background-color: #232629;
}


QLabel { /* Base Text Size & Color */
    color: #aaa;
}


/**********************/
/* 5. Buttons, Spinners, Dropdown */

QPushButton, #blue_toolbutton { /* Global Button Style */
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #F7931D, stop: .1 #BE840A, stop: .95 #BE840A, stop: 1 #F49930);
    border:0;
    border-radius:3px;
    color:#ffffff;
    /* font-size:12px; */
    font-weight:bold;
    padding: 7px 25px;
}

#blue_toolbutton {
    padding: 5px 23px;
}

QPushButton:hover, #blue_toolbutton:hover, StatusBarButton:hover {
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: .01 #F7931D, stop: .1 #F7931D, stop: .95 #F7931D, stop: 1 #F49930);
}

StatusBarButton:hover {
    border: 0;
    border-radius:3px;
}

QPushButton:focus, #blue_toolbutton:focus {
    border:none;
    outline:none;
}

QPushButton:pressed, #blue_toolbutton:pressed {
    border:1px solid #31363b;
}

QPushButton:disabled, #blue_toolbutton:disabled
{
    color: #ccc;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A1A1A1, stop: 1 #898989);
}

QStatusBar {
    color: #fff;
}

QStatusBar QPushButton:pressed {
    border:1px solid #BE840A;
}

QStatusBar::item {
    border: none;
}

QComboBox { /* Dropdown Menus */
    border:1px solid #BE840A;
    padding: 5px;
    background:#232629;
    color:#ccc;
    combobox-popup: 0;
}

QComboBox::disabled {
    border: 1px solid #676767;
    background-color: #333639;
}

QComboBox::drop-down {
    width:25px;
    border:0px;
}

QComboBox::down-arrow {
    border-image: url({pkg_dir}/gui/icons/meowcoin_downArrow.png) 0 0 0 0 stretch stretch;
}

QComboBox QListView {
    border: 1px solid #BE840A;
    color: #ccc;
    padding: 3px;
    background-color: #232629;
    selection-color: #fff;
    selection-background-color: #818181;
}

QAbstractSpinBox {
    border:1px solid #BE840A;
    padding: 5px 3px;
    background: #232629;
    color: #ccc;
}

QAbstractSpinBox:disabled {
    border: 1px solid #676767;
}

QAbstractSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width:21px;
    background: #232629;
    border-left:0px;
    border-right:1px solid #BE840A;
    border-top:1px solid #BE840A;
    border-bottom:0px;
    padding-right:1px;
    padding-left:5px;
    padding-top:2px;
}

QAbstractSpinBox::up-button:disabled {
    border-right: 1px solid #676767;
    border-top: 1px solid #676767;
}

QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width:21px;
    background: #232629;
    border-top:0px;
    border-left:0px;
    border-right:1px solid #BE840A;
    border-bottom:1px solid #BE840A;
    padding-right:1px;
    padding-left:5px;
    padding-bottom:2px;
}

QAbstractSpinBox::down-button:disabled {
    border-right: 1px solid #676767;
    border-bottom: 1px solid #676767;
}

QAbstractSpinBox::up-arrow {
    image: url({pkg_dir}/gui/icons/meowcoin_upArrow_small.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {
    image: url({pkg_dir}/gui/icons/meowcoin_upArrow_small_disabled.png);
}

QAbstractSpinBox::down-arrow {
    image: url({pkg_dir}/gui/icons/meowcoin_downArrow_small.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {
    image: url({pkg_dir}/gui/icons/meowcoin_downArrow_small_disabled.png);
}

QSlider::groove:horizontal {
    border: 1px solid #BE840A;
    background: 232629;
    height: 10px;
}

QSlider::sub-page:horizontal {
    background-color: #53565b;
    border: 1px solid #BE840A;
    height: 10px;
}

QSlider::add-page:horizontal {
    background: #232629;
    border: 1px solid #BE840A;
    height: 10px;
}

QSlider::handle:horizontal {
    background-color: #BE840A;
    border: 1px solid #BE840A;
    width: 13px;
    margin-top: -2px;
    margin-bottom: -2px;
    border-radius: 2px;
}


QProgressBar {
    color: #ccc;
}

QProgressBar:horizontal {
    border: 1px solid #BE840A;
    background-color: #232629;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #53565b;
}


/**********************/
/* 6. Table Headers */

QHeaderView { /* Table Header */
    background-color:transparent;
    border:0px;

}

QHeaderView::section { /* Table Header Sections */
    qproperty-alignment:center;
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.25, stop: 0 #BE840A, stop: 1 #C18632);
    color:#fff;
    font-weight:bold;
    font-size:11px;
    outline:0;
    border:0;
    border-right:1px solid #BE840A;
    padding-left:2px;
    padding-right:10px;
    padding-top:1px;
    padding-bottom:1px;
}

#contacts_container QHeaderView::section {
}

#contacts_container QHeaderView::section:first {
    padding-left:50px;
    padding-right:40px;
}

QHeaderView::section:last {
    border-right: 0px solid #d7d7d7;
}


/**********************/
/* 7. Scroll Bar */

QAbstractScrollArea::corner {
    background: none;
    border: none;
}

QScrollBar { /* Scroll Bar */
}

QScrollBar:vertical { /* Vertical Scroll Bar Attributes */
    border:0;
    background: #31363b;
    width:18px;
    margin: 18px 0px 18px 0px;
}

QScrollBar:horizontal { /* Horizontal Scroll Bar Attributes */
    border:0;
    background: #31363b;
    height:18px;
    margin: 0px 18px 0px 18px;
}


QScrollBar::handle:vertical { /* Scroll Bar Slider - vertical */
    background: #31363b;
    min-height:10px;
}

QScrollBar::handle:horizontal { /* Scroll Bar Slider - horizontal */
    background: #31363b;
    min-width:10px;
}

QScrollBar::add-page, QScrollBar::sub-page { /* Scroll Bar Background */
    background: #53565b;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { /* Define Arrow Button Dimensions */
    background-color: #232629;
    border: 1px solid #31363b;
    width:16px;
    height:16px;
}

QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed {
    background-color:#53565b;
}

QScrollBar::sub-line:vertical { /* Vertical - top button position */
    subcontrol-position:top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical { /* Vertical - bottom button position */
    subcontrol-position:bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal { /* Vertical - left button position */
    subcontrol-position:left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal { /* Vertical - right button position */
    subcontrol-position:right;
    subcontrol-origin: margin;
}

QScrollBar:up-arrow, QScrollBar:down-arrow, QScrollBar:left-arrow, QScrollBar:right-arrow { /* Arrows Icon */
    width:10px;
    height:10px;
}

QScrollBar:up-arrow {
    background-image: url({pkg_dir}/gui/icons/meowcoin_upArrow_small.png);
}

QScrollBar:down-arrow {
    background-image: url({pkg_dir}/gui/icons/meowcoin_downArrow_small.png);
}

QScrollBar:left-arrow {
    background-image: url({pkg_dir}/gui/icons/meowcoin_leftArrow_small.png);
}

QScrollBar:right-arrow {
    background-image: url({pkg_dir}/gui/icons/meowcoin_rightArrow_small.png);
}


/**********************/
/* 8. Tree Widget */

QTreeView, QTreeWidget, QListWidget, QTableView, QTextEdit, QPlainTextEdit  {
    border: 0px;
    color: #ccc;
    background-color: #232629;
}

QTreeView:disabled, QTreeWidget:disabled, QListWidget:disabled,
QTableView:disabled, QTextEdit:disabled, QPlainTextEdit:disabled  {
    border: 1px solid #676767;
    background-color: #333639;
}

QTreeView QLineEdit, QTreeWidget QLineEdit {
    min-height: 0;
    padding: 0;
}

QListWidget, QTableView, QTextEdit, QPlainTextEdit,
QDialog QTreeWidget, QDialog QTreeView {
    border: 1px solid #BE840A;
}

#send_container QTreeWidget, #receive_container QTreeWidget,
#send_container QTreeView, #receive_container QTreeView {
    border: 1px solid #BE840A;
    background-color: #232629;
}

QTableView {
    background-color: #232629;
}

QTreeView::branch {
    color: #ccc;
    background-color: transparent;
}

QTreeView::branch:selected {
    background-color:#808080;
}

QTreeView::item:selected, QTreeView::item:selected:active {
    color: #fff;
    background-color:#808080;
}

MyTreeView::branch:has-siblings:adjoins-item {
    border-image: url({pkg_dir}/gui/icons/tx_group_mid.png) 0;
}

MyTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url({pkg_dir}/gui/icons/tx_group_tail.png) 0;
}

/**********************/
/* 9. Dialog Boxes */

QDialog {
    background-color: #232629;
}

QDialog QScrollArea {
    background: transparent;
}

QDialog QTabWidget,
QTabWidget QTabWidget {
    border-bottom:1px solid #333;
}

QDialog QTabWidget::pane,
QTabWidget QTabWidget::pane {
    border: 1px solid #53565b;
    color: #ccc;
    background-color: #232629;
}

QDialog QTabWidget QTabBar::tab,
QTabWidget QTabWidget QTabBar::tab {
    background-color: #232629;
    color: #ccc;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #53565b;
}

QDialog QTabWidget QTabBar::tab:first,
QTabWidget QTabWidget QTabBar::tab:first {
    border-left: 1px solid #53565b;
}

QDialog QTabWidget QTabBar::tab:last,
QTabWidget QTabWidget QTabBar::tab:last {
    border-right: 1px solid #53565b;
}

QDialog QTabWidget QTabBar::tab:selected,
QDialog QTabWidget QTabBar::tab:hover,
QTabWidget QTabWidget QTabBar::tab:selected,
QTabWidget QTabWidget QTabBar::tab:hover {
    background-color: #53565b;
    color: #ccc;
}

QDialog QTabWidget QTabBar::tear,
QTabWidget QTabWidget QTabBar::tear {
    width: 0px;
    border: none;
    border-right: 1px solid #53565b;
}

QDialog QTabWidget QTabBar::scroller,
QTabWidget QTabWidget QTabBar::scroller {
    width: 36;
}

QDialog QTabWidget QTabBar QToolButton,
QTabWidget QTabWidget QTabBar QToolButton {
    background-color: #232629;
    border: 1px solid #53565b;
    border-bottom: none;
}

QDialog QTabWidget QTabBar QToolButton:hover,
QTabWidget QTabWidget QTabBar QToolButton:hover {
    background-color: #53565b;
}

QDialog QTabWidget QTabBar QToolButton::left-arrow,
QTabWidget QTabWidget QTabBar QToolButton::left-arrow {
    image: url({pkg_dir}/gui/icons/meowcoin_leftArrow_small.png);
}

QDialog QTabWidget QTabBar QToolButton::left-arrow:disabled,
QTabWidget QTabWidget QTabBar QToolButton::left-arrow:disabled {
    image: url({pkg_dir}/gui/icons/meowcoin_leftArrow_small_disabled.png);
}

QDialog QTabWidget QTabBar QToolButton::right-arrow,
QTabWidget QTabWidget QTabBar QToolButton::right-arrow {
    image: url({pkg_dir}/gui/icons/meowcoin_rightArrow_small.png);
}

QDialog QTabWidget QTabBar QToolButton::right-arrow:disabled,
QTabWidget QTabWidget QTabBar QToolButton::right-arrow:disabled {
    image: url({pkg_dir}/gui/icons/meowcoin_rightArrow_small_disabled.png);
}

QDialog HelpButton {
    background-color: transparent;
    color: #ccc;
}

QDialog QWidget { /* Remove Annoying Focus Rectangle */
    outline: 0;
}

QDialog #settings_tab {
    min-width: 600px;
}

MasternodeDialog {
    min-height: 650px;
}

MasternodeDialog #dip3_warn {
    color: #FF0000;
}

Dip3TabWidget {
    border-bottom:1px solid #333;
}

Dip3TabWidget::pane {
    border: 1px solid #53565b;
    color: #ccc;
    background-color: #232629;
}

QTabWidget VTabBar::tab {
    background-color: #232629;
    color: #ccc;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #53565b;
}

QTabWidget VTabBar::tab:first {
    border-left: 1px solid #53565b;
}

QTabWidget VTabBar::tab:last {
    border-right: 1px solid #53565b;
}

QTabWidget VTabBar::tab:selected, QTabWidget VTabBar::tab:hover {
    background-color: #53565b;
    color: #ccc;
}

QWizard {
    background-color: #232629;
}

#err-label {
    color: #ff0000;
}
#info-label {
    color: #00cc00;
}
"""


pkg_dir_for_css = pkg_dir.replace(os.sep, '/')
meowcoin_stylesheet = meowcoin_stylesheet.replace('{pkg_dir}', '%s' % pkg_dir_for_css)
