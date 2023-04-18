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

/*Projeção textual*/
sealed class JsonValue {
    abstract fun toJsonString(depth: Int = 0): String
    abstract fun search(visitor: JsonVisitor)
}

class JsonArray : JsonValue() {
    val items = mutableListOf<JsonValue>()

    fun addItem(item: JsonValue) {
        items.add(item)
    }

    override fun toJsonString(depth: Int): String {
        val itemStrings = items.joinToString(",\n${"\t".repeat(depth + 1)}") { it.toJsonString(depth + 1) }

        return "[\n${"\t".repeat(depth + 1)}$itemStrings\n${"\t".repeat(depth)}]"
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}

class JsonBoolean(private val value: Boolean) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}

class JsonDouble(private val value: Double) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}

object JsonNull : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "null"
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}

class JsonNumber(private val value: Number) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}

class JsonString(private val value: String) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "\"$value\""
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}

class JsonObject : JsonValue() {
    val properties = mutableMapOf<String, JsonValue>()

    fun addProperty(name: String, value: JsonValue) {
        properties[name] = value
    }

    override fun toJsonString(depth: Int): String {
        val propertyStrings = properties.map { (name, value) ->
            "${"\t".repeat(depth + 1)}\"$name\": ${value.toJsonString(depth + 1)}"
        }.joinToString(",\n")
        return "{\n$propertyStrings\n${"\t".repeat(depth)}}"
    }

    override fun search(visitor: JsonVisitor) {
        visitor.visit(this)
    }
}


/*VISITOR*/
interface JsonVisitor {
    fun visit(jsonArray: JsonArray)
    fun visit(jsonBoolean: JsonBoolean)
    fun visit(jsonDouble: JsonDouble)
    fun visit(jsonNull: JsonNull)
    fun visit(jsonNumber: JsonNumber)
    fun visit(jsonString: JsonString)
    fun visit(jsonObject: JsonObject)
}

class JsonVisitorImpl(private val propertyName: String, private val propertyValue: JsonValue) : JsonVisitor {
    private val matchingObjects = mutableMapOf<String, JsonValue>()

    override fun visit(jsonArray: JsonArray) {
        jsonArray.items.forEach { it.search(this) }
    }

    override fun visit(jsonBoolean: JsonBoolean) {
    }

    override fun visit(jsonDouble: JsonDouble) {
    }

    override fun visit(jsonNull: JsonNull) {
    }

    override fun visit(jsonNumber: JsonNumber) {
    }

    override fun visit(jsonString: JsonString) {
    }

    override fun visit(jsonObject: JsonObject) {
        if (jsonObject.properties.containsKey(propertyName) && jsonObject.properties[propertyName]?.toJsonString() == propertyValue.toJsonString()) {
            matchingObjects[propertyName] = propertyValue
        }
        jsonObject.properties.values.forEach { it.search(this) }
    }

    fun getMatchingObjects(): MutableMap<String, JsonValue> {
        return matchingObjects
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
    //println(objecto.toJsonString(0))

    /*SEARCH*/
    val propertyName = "numero"
    val propertyValue = JsonNumber(26503)
    val search = JsonVisitorImpl(propertyName, propertyValue)

    objecto.search(search)
    val matchingObjects = search.getMatchingObjects()
    println("Matching objects:")
    for (matchingObject in matchingObjects) {
        println(matchingObject.key + ": " + matchingObject.value.toJsonString(0))
    }

}