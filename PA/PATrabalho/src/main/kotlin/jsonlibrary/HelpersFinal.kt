package jsonlibrary

import java.awt.Component
import java.awt.Dimension
import java.awt.GridLayout
import java.awt.Toolkit
import java.awt.event.*
import javax.swing.*

fun main() {
    val x = Editor().open()
}

class Editor {

    private var theMainObject: JSONObject = getObject2()
    private var srcArea = JTextArea()
    private var leftPanel = JPanel()
    private var scrollPane = JScrollPane()

    val frame = JFrame("Josue - JSON Object Editor").apply {
        defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        layout = GridLayout(0, 2)
        extendedState = JFrame.MAXIMIZED_BOTH

        leftPanel.layout = GridLayout()
        scrollPane = JScrollPane(testPanel()).apply {
            horizontalScrollBarPolicy = JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS
            verticalScrollBarPolicy = JScrollPane.VERTICAL_SCROLLBAR_ALWAYS
        }
        leftPanel.add(scrollPane)
        add(leftPanel)

        val right = JPanel()
        right.layout = GridLayout()
        srcArea.tabSize = 2
        srcArea.text = theMainObject.toJsonString()
        right.add(srcArea)
        add(right)
    }

    fun open() {
        frame.isVisible = true
    }

    fun testPanel(): JPanel =
        JPanel().apply {
            layout = BoxLayout(this, BoxLayout.Y_AXIS)
            alignmentX = Component.LEFT_ALIGNMENT
            alignmentY = Component.TOP_ALIGNMENT

            fun addProperties(parentObj: JSONObject?, jsonArray: JSONArray?, depth: Int = 0) {
                jsonArray?.getItems()?.forEach { item ->
                    when (item) {
                        is JSONArray -> {
                            item.getItems().forEach { nestedItem ->
                                when (nestedItem) {
                                    is JSONObject -> {
                                        addProperties(nestedItem, null, depth + 1)
                                    }

                                    else -> {
                                        add(testWidget(Pair("", nestedItem), parentObj, depth))
                                    }
                                }
                            }
                        }

                        is JSONObject -> {
                            addProperties(parentObj = item, jsonArray = null, depth = depth + 1)
                        }

                        else -> {
                            add(testWidget(Pair("", item), parentObj, depth))
                        }
                    }
                }
                parentObj?.get()?.forEach { (key, value) ->
                    when (value) {
                        is JSONArray -> {
                            value.getItems().forEach { item ->
                                when (item) {
                                    is JSONObject -> {
                                        addProperties(item, null, depth = depth + 1)
                                    }

                                    else -> {
                                        add(testWidget(Pair(key, item), parentObj, depth))
                                    }
                                }
                            }
                        }

                        is JSONObject -> {
                            addProperties(parentObj = value, jsonArray = null, depth = depth + 1)
                        }

                        else -> {
                            add(testWidget(Pair(key, value), parentObj, depth))
                        }
                    }
                }
            }
            addProperties(theMainObject, null)
        }


    fun testWidget(prop: Pair<String, JSONValue>, jo: JSONObject?, depth: Int): JPanel =
        JPanel().apply {
            layout = BoxLayout(this, BoxLayout.X_AXIS)
            alignmentX = Component.LEFT_ALIGNMENT
            alignmentY = Component.TOP_ALIGNMENT

            // menu
            addMouseListener(object : MouseAdapter() {
                override fun mouseClicked(e: MouseEvent) {
                    if (SwingUtilities.isRightMouseButton(e)) {
                        val menu = JPopupMenu("Message")
                        val add = JButton("add")
                        add.addActionListener {
                            val text = JOptionPane.showInputDialog("text")

                            jo?.addProperty(text, JSONString("?"))
                            add(testWidget(prop, jo, depth))
                            srcArea.text = theMainObject.toJsonString()

                            leftPanel.layout = GridLayout()
                            scrollPane = JScrollPane(testPanel()).apply {
                                horizontalScrollBarPolicy = JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS
                                verticalScrollBarPolicy = JScrollPane.VERTICAL_SCROLLBAR_ALWAYS
                            }
                            leftPanel.add(scrollPane)
                            add(leftPanel)
                            leftPanel.revalidate()
                            leftPanel.repaint()

                            menu.isVisible = false
                            revalidate()
                            frame.repaint()
                        }
                        val del = JButton("delete")
                        del.addActionListener {
                            jo?.remove(prop)
                            srcArea.text = theMainObject.toJsonString()
                            components.forEach {
                                remove(it)
                            }
                            menu.isVisible = false
                            revalidate()
                            frame.repaint()
                        }
                        menu.add(add);
                        menu.add(del)
                        menu.show(this@apply, 40, 40);
                    }
                }
            })

            add(JLabel("                    ".repeat(depth) + prop.first))
            val text = JTextField(prop.second.toJsonString().replace("\"", ""))
            text.addKeyListener(object : KeyAdapter() {
                override fun keyReleased(e: KeyEvent?) {
                    jo?.update(prop.first, text.text)
                    srcArea.text = theMainObject.toJsonString()
                }
            })
            add(text)
        }
}