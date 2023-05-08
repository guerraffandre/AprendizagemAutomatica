package jsonlibrary

import java.util.*
import kotlin.reflect.KClass
import kotlin.reflect.KProperty
import kotlin.reflect.full.declaredMemberProperties
import kotlin.reflect.full.findAnnotation
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

    fun update(key: String, value: String) {
        when {
            value.equals("null", ignoreCase = true) -> properties[key] = JsonNull()
            value.toDoubleOrNull() != null -> properties[key] = JsonDouble(value.toDouble())
            value.equals("true", ignoreCase = true) || value.equals("false", ignoreCase = true) -> properties[key] =
                JsonBoolean(value.toBoolean())

            value.startsWith("[") && value.endsWith("]") -> readJsonArray(key)
            else -> properties[key] = JsonString(value)
        }
    }

    fun readJsonArray(name: String) {
        var jsonArray = JsonArray()
        var objeto2 = JsonObject()
        jsonArray.addItem(objeto2)
        this.addProperty(name, jsonArray)
    }


    override fun toJsonString(depth: Int): String {
        val propertyStrings = properties.map { (name, value) ->
            "${"\t".repeat(depth + 1)}\"$name\": ${value.toJsonString(depth + 1)}"
        }.joinToString(",\n")
        return "{\n$propertyStrings\n${"\t".repeat(depth)}}"
    }

    override fun search(
        key: String,
        value: JsonValue,
        matchingObjects: MutableMap<String, JsonValue>
    ): MutableMap<String, JsonValue> {
        if (properties.containsKey(key)) {
            value.search(key, value, matchingObjects)
        }
        return matchingObjects
    }

    override fun mapObject(o: Any): JsonValue {
        val clazz: KClass<*> = o::class
        val fields: List<KProperty<*>> = clazz.dataClassFields
        val jsonObject = JsonObject()

        fields.forEach { field ->
            if (!field.annotations.any { it.annotationClass == Exclude::class }) {
                val value = field.getter.call(o)

                val fieldNameAnnotation = field.findAnnotation<ChangeName>()
                val fieldName = fieldNameAnnotation?.name ?: field.name

                val forceStringAnnotation = field.findAnnotation<ToString>()

                when (value) {
                    is String -> {
                        if (forceStringAnnotation != null) {
                            jsonObject.addProperty(fieldName, JsonString(value))
                        } else {
                            jsonObject.addProperty(fieldName, JsonString(value))
                        }
                    }

                    is Number -> {
                        if (forceStringAnnotation != null) {
                            jsonObject.addProperty(fieldName, JsonString(value.toString()))
                        } else {
                            jsonObject.addProperty(fieldName, JsonNumber(value))
                        }
                    }

                    is Boolean -> {
                        if (forceStringAnnotation != null) {
                            jsonObject.addProperty(fieldName, JsonString(value.toString()))
                        } else {
                            jsonObject.addProperty(fieldName, JsonBoolean(value))
                        }
                    }

                    is Enum<*> -> {
                        if (forceStringAnnotation != null) {
                            jsonObject.addProperty(fieldName, JsonString(value.name))
                        } else {
                            jsonObject.addProperty(fieldName, JsonString(value.name))
                        }
                    }
                }
            }
        }
        return jsonObject
    }

}

fun Any.isEnum(): Boolean {
    return this is Enum<*>
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
annotation class ToString


@Target(AnnotationTarget.PROPERTY)
annotation class Length(val length: Int)


@Retention(AnnotationRetention.RUNTIME)
@Target(AnnotationTarget.PROPERTY)
annotation class ChangeName(val name: String)

data class Student(
    //@Exclude
    @ChangeName("student_id")
    // @ToString
    val number: Int,
    @Length(50)
    val name: String,
    @DbName("degree")
    val type: StudentType


    //forçar ser string
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