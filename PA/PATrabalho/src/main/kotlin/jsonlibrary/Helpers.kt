import jsonlibrary.*
import jsonlibrary.StudentType
import java.awt.Component
import java.awt.Dimension
import java.awt.GridLayout
import java.awt.event.*
import javax.swing.*

fun main() {
    Editor().open()
}

class Editor {
    val frame = JFrame("Josue - JSON Object Editor").apply {
        defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        layout = GridLayout(0, 2)
        size = Dimension(600, 600)

        val left = JPanel()
        left.layout = GridLayout()
        val scrollPane = JScrollPane(testPanel()).apply {
            horizontalScrollBarPolicy = JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS
            verticalScrollBarPolicy = JScrollPane.VERTICAL_SCROLLBAR_ALWAYS
        }
        left.add(scrollPane)
        add(left)

        val right = JPanel()
        right.layout = GridLayout()
        val srcArea = JTextArea()
        srcArea.tabSize = 2
        srcArea.text = getObjectString()
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

            getObject().properties.forEach {
                if (it.value is JsonArray) {
                    (it.value as JsonArray).items.forEach { it2 ->
                        val it22 = it2 as JsonObject
                        it22.properties.forEach { it222 ->
                            add(testWidget(it222.key, it222.value.toJsonString()))
                        }
                    }
                } else {
                    add(testWidget(it.key, it.value.toJsonString()))
                }
            }

            // menu
            addMouseListener(object : MouseAdapter() {
                override fun mouseClicked(e: MouseEvent) {
                    if (SwingUtilities.isRightMouseButton(e)) {
                        val menu = JPopupMenu("Message")
                        val add = JButton("add")
                        add.addActionListener {
                            val text = JOptionPane.showInputDialog("text")
                            add(testWidget(text, "?"))
                            menu.isVisible = false
                            revalidate()
                            frame.repaint()
                        }
                        val del = JButton("delete all")
                        del.addActionListener {
                            components.forEach {
                                remove(it)
                            }
                            menu.isVisible = false
                            revalidate()
                            frame.repaint()
                        }
                        menu.add(add);
                        menu.add(del)
                        menu.show(this@apply, 100, 100);
                    }
                }
            })
        }


    fun testWidget(key: String, value: String): JPanel =
        JPanel().apply {
            layout = BoxLayout(this, BoxLayout.X_AXIS)
            alignmentX = Component.LEFT_ALIGNMENT
            alignmentY = Component.TOP_ALIGNMENT

            add(JLabel(key))
            val text = JTextField(value)
            text.addKeyListener(object : KeyAdapter() {
                override fun keyReleased(e: KeyEvent?) {
                    println("keyReleased: ${text.text}")
                }
            })
            add(text)
        }
}




fun getObjectString(): String {

    val student = Student(12345, "John Doe", StudentType.Bachelor)
    val oracleGenerator = JsonObject().mapObject(student)
    return oracleGenerator.toJsonString()
}

fun getObject(): JsonObject {

    val student = Student(12345, "John Doe", StudentType.Bachelor)
    val oracleGenerator = JsonObject().mapObject(student)
    return oracleGenerator as JsonObject
}

