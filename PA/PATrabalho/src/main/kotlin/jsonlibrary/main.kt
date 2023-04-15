package jsonlibrary

/*
{
  "uc": "PA",
  "ects" : 6.0,
  "data-exame" : null,
  "inscritos": [
    {
      "numero" : 101101,
      "nome" : "Dave Farley",
      "internacional" : true
    },
    {
      "numero" : 101102,
      "nome" : "Martin Fowler",
      "internacional" : true
    },
    {
      "numero" : 26503,
      "nome" : "André Santos",
      "internacional" : false
    }
  ]
}
 */
interface JsonVisitor {
    fun visit(obj: JsonObject)
    fun visit(array: JsonArray)
    fun visit(string: JsonString)
    fun visit(number: JsonNumber)
    fun visit(bool: JsonBoolean)
    fun visit(nullValue: JsonNull)
}

sealed class JsonValue {
    abstract fun toJsonString(depth: Int): String
}

class JsonArray : JsonValue() {
    private val items = mutableListOf<JsonValue>()

    fun addItem(item: JsonValue) {
        items.add(item)
    }

    override fun toJsonString(depth: Int): String {
        val itemStrings = items.joinToString(",\n${"\t".repeat(depth + 1)}") { it.toJsonString(depth + 1) }

        return "[\n${"\t".repeat(depth + 1)}$itemStrings\n${"\t".repeat(depth)}]"
    }
}

class JsonBoolean(private val value: Boolean) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }
}

class JsonDouble(private val value: Double) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }
}

object JsonNull : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "null"
    }
}

class JsonNumber(private val value: Number) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }
}

class JsonString(private val value: String) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "\"$value\""
    }
}

class JsonObject : JsonValue() {
    private val properties = mutableMapOf<String, JsonValue>()

    fun addProperty(name: String, value: JsonValue) {
        properties[name] = value
    }

    override fun toJsonString(depth: Int): String {
        val propertyStrings = properties.map { (name, value) ->
            "${"\t".repeat(depth + 1)}\"$name\": ${value.toJsonString(depth + 1)}"
        }.joinToString(",\n")
        return "{\n$propertyStrings\n${"\t".repeat(depth)}}"
    }
}


fun main(args: Array<String>) {

    var objecto = JsonObject()
    objecto.addProperty("uc", JsonString("PA"))
    objecto.addProperty("ects", JsonDouble(6.0))
    objecto.addProperty("data-exame", JsonNull)

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

    println(objecto.toJsonString(0))

}
