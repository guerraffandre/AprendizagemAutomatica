package jsonlibrary

import getSqlType
import kotlin.jvm.internal.Intrinsics.Kotlin
import kotlin.reflect.KClass
import kotlin.reflect.KProperty
import kotlin.reflect.KType
import kotlin.reflect.full.declaredMemberProperties
import kotlin.reflect.full.memberProperties
import kotlin.reflect.full.primaryConstructor

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

    open fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue> = mutableMapOf()
    ): MutableMap<String, JsonValue> {
        if (this == propertyValue) {
            matchingObjects[propertyName] = this
        }
        return matchingObjects
    }

    abstract fun mapObject(o: Any): JsonValue
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

    override fun mapObject(o: Any): JsonValue {
        return JsonArray()
    }
}

class JsonBoolean(private val value: Boolean) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun mapObject(o: Any): JsonValue {
        TODO("Not yet implemented")
    }
}

class JsonDouble(private val value: Double) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun mapObject(o: Any): JsonValue {
        TODO("Not yet implemented")
    }
}

class JsonNull() : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "null"
    }

    override fun search(
        propertyName: String,
        propertyValue: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        return matchingObjects
    }

    override fun mapObject(o: Any): JsonValue {
        TODO("Not yet implemented")
    }
}

class JsonNumber(private val value: Number) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun mapObject(o: Any): JsonValue {
        TODO("Not yet implemented")
    }
}

class JsonString(private val value: String) : JsonValue() {
    override fun toJsonString(depth: Int): String {
        return "\"$value\""
    }

    override fun mapObject(o: Any): JsonValue {
        TODO("Not yet implemented")
    }
}

class JsonObject : JsonValue() {
    val properties = mutableMapOf<String, JsonValue>()

    fun addProperty(name: String, value: JsonValue) {
        properties[name] = value
    }

    fun updateValue(name: String, value: JsonValue) {
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
        if (properties.containsKey(propertyName)) {
            propertyValue.search(propertyName, propertyValue, matchingObjects)
        }
        return matchingObjects
    }

    override fun mapObject(o: Any): JsonValue {
        val clazz: KClass<*> = o::class
        val fields: List<KProperty<*>> = clazz.dataClassFields
        val jsonObject = JsonObject()

        fields.forEach {
            if (!it.annotations.any { it.annotationClass == Exclude::class }) {
                val value = it.getter.call(o)
                when (value) {
                    is String -> jsonObject.addProperty(it.name, JsonString(value))
                    is Number -> jsonObject.addProperty(it.name, JsonNumber(value))
                    is Boolean -> jsonObject.addProperty(it.name, JsonBoolean(value))
                    //is ArrayList<*> -> jsonObject.addProperty(field.name, JsonArray(value))
                    //else -> jsonObject[field.name] = mapObject(value)
                }
            }
        }
        return jsonObject
    }

}

fun main(args: Array<String>) {

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
    //println(objecto.toJsonString())

    /*SEARCH*/
    val propertyName = "uc"
    val propertyValue = JsonString("PA")

    val listRes = objecto.search(propertyName, propertyValue)
    for (matchingObject in objecto.search(propertyName, propertyValue, listRes)) {
        //println(matchingObject.key + ": " + matchingObject.value.toJsonString(0))
    }

    //2 fase
    val student = Student(12345, "John Doe", StudentType.Bachelor)
    val oracleGenerator = JsonObject().mapObject(student)
    println(oracleGenerator.toJsonString())
}


@Target(AnnotationTarget.CLASS, AnnotationTarget.PROPERTY)
annotation class DbName(val name: String)

@Target(AnnotationTarget.PROPERTY)
annotation class PrimaryKey

@Target(AnnotationTarget.PROPERTY)
annotation class Exclude

@Target(AnnotationTarget.PROPERTY)
annotation class ForceString

@Target(AnnotationTarget.PROPERTY)
annotation class Length(val length: Int)
data class Student(
    //@Exclude
    val number: Int,
    @Length(50)
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