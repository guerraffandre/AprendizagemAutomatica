/*import jsonlibrary.*
import jsonlibrary.StudentType
import java.awt.Component
import java.awt.Dimension
import java.awt.GridLayout
import java.awt.event.*
import java.util.*
import javax.swing.*
import kotlin.properties.ObservableProperty
import kotlin.reflect.KProperty

fun main() {
    Editor().open()
}

class Editor {


    class JsonObjectObservableProperty(initialValue: JsonObject) : ObservableProperty<JsonObject>(initialValue) {

        override fun afterChange(property: KProperty<*>, oldValue: JsonObject, newValue: JsonObject) {
            println("########")
            val oldJson = oldValue.toJsonString()
            val newJson = newValue.toJsonString()

            if (oldJson != newJson) {
                println("$property has changed from $oldJson to $newJson")
            }
        }
    }

    val theMainObject: JsonObject by JsonObjectObservableProperty(getObject2())


    private val srcArea = JTextArea()

    val frame = JFrame("Josue - JSON Object Editor").apply {
        defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        layout = GridLayout(0, 2)
        size = Dimension(1700, 1200)

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

            fun addProperties(properties: Map<String, JsonValue>, depth: Int = 0) {
                properties.forEach {
                    val indentedKey = "                    ".repeat(depth) + it.key
                    if (it.value is JsonArray) {
                        (it.value as JsonArray).items.forEach { item ->
                            if (item is JsonObject) {
                                addProperties(
                                    item.properties,
                                    depth + 1
                                )
                            } else {
                                add(testWidget(it))
                            }
                        }
                    } else if (it.value is JsonObject) {
                        addProperties(
                            (it.value as JsonObject).properties,
                            depth + 1
                        )
                    } else {
                        add(testWidget(it))
                    }
                }
            }
            addProperties(theMainObject.properties)

        }


    fun testWidget(elVal: Map.Entry<String, JsonValue>): JPanel =
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
                            println(elVal.key)
                            val text = JOptionPane.showInputDialog("text")
                            (elVal.value as JsonObject).addProperty(text, JsonString("?"))
                            add(testWidget(elVal))
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

            add(JLabel(elVal.key))
            val text = JTextField(elVal.value.toJsonString())
            text.addKeyListener(object : KeyAdapter() {
                override fun keyReleased(e: KeyEvent?) {
                    elVal.value.update(elVal.key, text.text)
                    srcArea.text = theMainObject.toJsonString()
                }
            })
            add(text)
        }
}


fun getObject(): JsonObject {

    val student = Student(12345, "John Doe", StudentType.Bachelor)
    val oracleGenerator = JsonObject().mapObject(student)
    return oracleGenerator as JsonObject
}

fun getObject2(): JsonObject {
    var objecto = JsonObject()
    objecto.addProperty("uc", JsonString("PA"))
    objecto.addProperty("ects", JsonDouble(6.0))
    objecto.addProperty("data-exame", JsonNull())

    var jsonArray = JsonArray()
    var objeto2 = JsonObject()
    objeto2.addProperty("numero", JsonNumber(101101))
    objeto2.addProperty("nome", JsonString("Dave Farley"))
    objeto2.addProperty("internacional", JsonBoolean(true))
    jsonArray.addItem(objeto2)
    var objeto3 = JsonObject()
    objeto3.addProperty("numero", JsonNumber(101102))
    objeto3.addProperty("nome", JsonString("Martin Fowler"))
    objeto3.addProperty("internacional", JsonBoolean(true))
    jsonArray.addItem(objeto3)
    var objeto4 = JsonObject()
    objeto4.addProperty("numero", JsonNumber(26503))
    objeto4.addProperty("nome", JsonString("André Santos"))
    objeto4.addProperty("internacional", JsonBoolean(false))
    jsonArray.addItem(objeto4)

    var jsonArray2 = JsonArray()
    var objeto44 = JsonObject()
    objeto44.addProperty("numero", JsonNumber(1))
    objeto44.addProperty("nome", JsonString("Dave Farleyasd"))
    objeto44.addProperty("internacional", JsonBoolean(true))
    jsonArray2.addItem(objeto44)
    objeto4.addProperty("subInscrito", jsonArray2)

    objecto.addProperty("inscritos", jsonArray)
    return objecto
}*/
