package jsonlibrary


import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import java.io.File
import java.util.*
import kotlin.test.assertNotNull

class mainTests {

    @Test
    fun Test() {
        assertEquals("1", "1")
    }

    @Test
    fun testReadJsonFile() {
        val json = File("example.json").readText()
        assertNotNull(json)
    }

    @Test
    fun testRemovePropertyFromJSONObject() {
        val jsonObject = JSONObject()
        jsonObject.addProperty("uc", JSONString("PA"))
        jsonObject.addProperty("ects", JSONNumber(6.0))

        val originalSize = jsonObject.get().size

        jsonObject.remove("uc" to JSONString("PA"))

        val newSize = jsonObject.get().size

        assertEquals(originalSize - 1, newSize)
    }

    @Test
    fun testAddPropertyToJSONObject() {
        val jsonObject = JSONObject()

        val originalSize = jsonObject.get().size

        jsonObject.addProperty("uc", JSONString("PA"))

        val newSize = jsonObject.get().size

        assertEquals(originalSize + 1, newSize)

        val addedProperty = jsonObject.get().find { it.first == "uc" }

        assertNotNull(addedProperty)
        assertEquals("uc", addedProperty!!.first)
        assertEquals(JSONString("PA"), addedProperty.second)
    }
    @Test
    fun testUpdatePropertyInJSONObject() {
        val jsonObject = JSONObject()

        jsonObject.addProperty("uc", JSONString("PA"))
        jsonObject.addProperty("ects", JSONNumber(6.0))

        jsonObject.update("uc", "DB")

        val updatedProperty = jsonObject.get().find { it.first == "uc" }

        assertNotNull(updatedProperty)
        assertEquals("uc", updatedProperty!!.first)
        assertEquals(JSONString("DB"), updatedProperty.second)
    }



    @Test
    fun validaEstrutura() {
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

        objecto.addProperty("inscritos", jsonArray)

        val json = objecto.toJsonString()
        var index = 0
        val stack = Stack<Char>()

        while (index < json.length) {
            val c = json[index]

            when (c) {
                '{', '[', '(' -> stack.push(c)
                '}', ']', ')' -> {
                    if (stack.isEmpty()) {
                        //return false
                    }

                    val last = stack.pop()
                    if ((last == '{' && c != '}') ||
                        (last == '[' && c != ']') ||
                        (last == '(' && c != ')')) {
                        //return false
                    }
                }
            }

            index++
        }

        //assertEquals()
    }

    //confirmar a pesquisa está ok VISITOR

}