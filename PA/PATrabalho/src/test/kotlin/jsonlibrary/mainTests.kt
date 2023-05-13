package jsonlibrary

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import kotlin.test.assertNotNull

class MainTests {

    @Test
    fun Test() {
        assertEquals("1", "1")
    }

    @Test
    fun testRemovePropertyFromJSONObject() {
        var jsonObject = JSONObject()
        jsonObject.addProperty("uc", JSONString("PA"))
        jsonObject.addProperty("ects", JSONNumber(6.0))

        val originalSize = jsonObject.get().size

        val el: Pair<String, JSONValue> = jsonObject.get()[0]
        jsonObject.remove(el)

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
        assertEquals(JSONString("PA").toJsonString(), addedProperty.second.toJsonString())
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
        assertEquals(JSONString("DB").toJsonString(), updatedProperty.second.toJsonString())
    }


    @Test
    fun testValidateJSONStructure() {
        val jsonObject = JSONObject()
        jsonObject.addProperty("uc", JSONString("PA"))
        jsonObject.addProperty("ects", JSONNumber(6.0))

        val jsonArray = JSONArray()
        val jsonObject2 = JSONObject()
        jsonObject2.addProperty("numero", JSONNumber(101101))
        jsonObject2.addProperty("nome", JSONString("Dave Farley"))
        jsonArray.addItem(jsonObject2)
        val jsonObject3 = JSONObject()
        jsonObject3.addProperty("numero", JSONNumber(101102))
        jsonObject3.addProperty("nome", JSONString("Martin Fowler"))
        jsonArray.addItem(jsonObject3)
        val jsonObject4 = JSONObject()
        jsonObject4.addProperty("numero", JSONNumber(26503))
        jsonObject4.addProperty("nome", JSONString("André Santos"))
        jsonArray.addItem(jsonObject4)

        jsonObject.addProperty("inscritos", jsonArray)

        val jsonString = jsonObject.toJsonString()

        val expectedJsonString =
            """
{
  "uc": "PA",
  "ects": 6.0,
  "inscritos": [
      {
        "numero": 101101,
        "nome": "Dave Farley"
      },
      {
        "numero": 101102,
        "nome": "Martin Fowler"
      },
      {
        "numero": 26503,
        "nome": "André Santos"
      }
   ]
}
             """.trimIndent()
        assertEquals(expectedJsonString, jsonString)
    }

    @Test
    fun testSearchInJSONObject() {
        val jsonObject = JSONObject()
        jsonObject.addProperty("uc", JSONString("PA"))
        jsonObject.addProperty("ects", JSONNumber(6.0))

        val propertyName = "uc"
        val propertyValue = JSONString("PA")
        val matchingObjects = jsonObject.search(propertyName, propertyValue)

        assertEquals(1, matchingObjects.size)
        assertEquals(JSONString("PA").toJsonString(), matchingObjects[0].toJsonString())
    }

}