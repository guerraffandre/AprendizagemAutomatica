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

abstract class JsonValue {
    abstract fun toJsonString(depth: Int = 0): String

    abstract fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue>
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

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        items.forEach { it.search(propertyName, propertyValue, matchingObjects) }
        return matchingObjects
    }
}

class JsonBoolean(private val value: Boolean) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        //no-impl
        return matchingObjects
    }
}

class JsonDouble(private val value: Double) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        //no-impl
        return matchingObjects
    }
}

object JsonNull : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "null"
    }

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        //no-impl
        return matchingObjects
    }
}

class JsonNumber(private val value: Number) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        if (this == propertyValue) {
            matchingObjects[this.hashCode().toString()] = this
        }
        return matchingObjects
    }
}

class JsonString(private val value: String) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "\"$value\""
    }

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        if (this == propertyValue) {
            matchingObjects[this.hashCode().toString()] = this
        }
        return matchingObjects
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

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        if (properties.containsKey(propertyName) && properties[propertyName]?.toJsonString() == propertyValue.toJsonString()) {
            matchingObjects[propertyName] = propertyValue
        }
        properties.values.forEach { it.search(propertyName, propertyValue, matchingObjects) }
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
    //println(objecto.toJsonString())

    /*SEARCH*/
    val propertyName = "uc"
    val propertyValue = JsonString("PA")
    val listRes = mutableMapOf<String, JsonValue>()
    objecto.search(propertyName, propertyValue, listRes)

    println("Matching objects:")
    for (matchingObject in objecto.search(propertyName, propertyValue, listRes)) {
        println(matchingObject.key + ": " + matchingObject.value.toJsonString(0))
    }

    //2 fase => objetoXPTO para os nossos objetos, ver Aula5
    /*val jo = Student::class::toJO
    print(jo.get().properties)*/
}

/*
@Target(AnnotationTarget.CLASS, AnnotationTarget.PROPERTY)
annotation class DbName(val name: String)

@Target(AnnotationTarget.PROPERTY)
annotation class PrimaryKey

@Target(AnnotationTarget.PROPERTY)
annotation class Exclude

@Target(AnnotationTarget.PROPERTY)
annotation class ForceString

@DbName("STUDENT")
data class Student(
    @PrimaryKey
    val number: Int,
    @Exclude
    val xpto: Int,
    @ForceString
    val propToForceString: Int,
    val name: String,
    @DbName("degree")
    val type: StudentType
)

enum class StudentType {
    Bachelor, Master, Doctoral
}

val KClass<*>.dataClassFields: List<KProperty<*>>
    get() {
        require(isData) { "instance must be data class" }
        return primaryConstructor!!.parameters.map { p ->
            declaredMemberProperties.find { it.name == p.name }!!
        }
    }

val KClass<*>.toJO: JsonObject
    get() {
        print(declaredMemberProperties)
        return JsonObject()
    }*/