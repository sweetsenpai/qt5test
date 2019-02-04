import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.GraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "My Window"
    Item {
        id: page
        visible: true
        width: parent.width

        Rectangle:{
            height: {
                console.log("I\'m a comment")
                return 160
            }

            color = "#ff0000"

            Text {
                text: "I am some regular text"
                height: 50
                width: parent.width
                font.pointSize: 12
            }
        }
    }
}