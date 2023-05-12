package jsonlibrary

import java.util.*
import kotlin.reflect.KClass
import kotlin.reflect.KProperty
import kotlin.reflect.full.declaredMemberProperties
import kotlin.reflect.full.findAnnotation
import kotlin.reflect.full.memberProperties
import kotlin.reflect.full.primaryConstructor

val identSpaces: Int = 6

fun getObject(): JSONObject {
    val student = Student(12345, "John Doe", StudentType.Bachelor)
    val json = JSONObject().mapObject(student)
    return json as JSONObject
}

fun getObject2(): JSONObject {
    val json = JSONObject().apply {
        addProperty("uc", JSONString("PA"))
        addProperty("ects", JSONNumber(6.0))
        addProperty("data-exame", JSONNull())
        val inscritos = JSONArray().apply {
            addItem(JSONObject().apply {
                addProperty("numero", JSONNumber(101101))
                addProperty("nome", JSONString("Dave Farley"))
                addProperty("internacional", JSONBoolean(true))
            })
            addItem(JSONObject().apply {
                addProperty("numero", JSONNumber(101102))
                addProperty("nome", JSONString("Martin Fowler"))
                addProperty("internacional", JSONBoolean(true))
            })
            addItem(JSONObject().apply {
                addProperty("numero", JSONNumber(26503))
                addProperty("nome", JSONString("André Santos"))
                addProperty("internacional", JSONBoolean(false))
            })
        }
        addProperty("inscritos", inscritos)
    }
    return json
}

fun main() {
    //println(json.getObject2())

    val propertyName = "numero"
    val propertyValue = JSONNumber(101102)
    val matchingObjects = getObject2().search(propertyName, propertyValue)
    for (matchingObject in matchingObjects) {
        //println(matchingObject.toJsonString())
    }

    //2 fase
    val student = Student(12345, "John Doe", StudentType.Bachelor)
    val json2 = JSONObject().mapObject(student)
    println(json2.toJsonString())
}

abstract class JSONValue {
    abstract fun toJsonString(indent: Int = 0): String
    open fun search(
        propertyName: String,
        propertyValue: JSONValue,
        results: MutableList<JSONValue> = mutableListOf()
    ): List<JSONValue> {
        if (this == propertyValue) {
            results.add(this)
        }
        return results
    }

    abstract fun mapObject(o: Any): JSONValue
}

class JSONObject : JSONValue() {
    private val properties = mutableListOf<Pair<String, JSONValue>>()

    fun get(): List<Pair<String, JSONValue>> {
        return properties
    }

    fun addProperty(name: String, value: JSONValue) {
        properties.add(name to value)
    }

    fun remove(el: Pair<String, JSONValue>) {
        properties.remove(el)
    }

    fun update(name: String, value: String) {
        var aux = when {
            value.equals("null", ignoreCase = true) -> JSONNull()
            value.toDoubleOrNull() != null -> JSONNumber(value.toDouble())
            value.equals("true", ignoreCase = true) || value.equals(
                "false",
                ignoreCase = true
            ) -> JSONBoolean(value.toBoolean())

            value.startsWith("[") && value.endsWith("]") -> JSONArray().apply {
                addItem(JSONObject().apply {
                    addProperty(name, JSONString("?"))
                })
            }

            else -> JSONString(value)
        }
        properties.forEachIndexed { index, pair ->
            if (pair.first == name) {
                properties[index] = name to aux
                return
            }
        }
        addProperty(name, aux)
    }

    override fun toJsonString(indent: Int): String {
        val sb = StringBuilder()
        sb.append("${addIndentation(indent)}{\n")
        for ((name, value) in properties) {
            sb.append("${addIndentation(indent + 2)}\"$name\": ${value.toJsonString()}")
            sb.append(",\n")
        }
        if (properties.isNotEmpty()) {
            sb.setLength(sb.length - 2) // remove last comma and newline
            sb.append('\n')
        }
        sb.append("${addIndentation(indent)}}")
        return sb.toString()
    }

    override fun search(
        propertyName: String,
        propertyValue: JSONValue,
        results: MutableList<JSONValue>
    ): List<JSONValue> {
        for ((name, value) in properties) {
            if (name.equals(propertyName, ignoreCase = true)) {
                if (value.toJsonString() == propertyValue.toJsonString()) {
                    results.add(value)
                }
            }
            value.search(propertyName, propertyValue, results)
        }
        return results
    }

    override fun mapObject(o: Any): JSONValue {
        val jsonObject = JSONObject()

        o::class.memberProperties
            .filterNot { it.annotations.any { annotation -> annotation is Exclude } }
            .forEach { field ->
                val fieldName = field.findAnnotation<ChangeName>()?.name ?: field.name
                val forceString = field.findAnnotation<ToString>() != null

                val jsonValue = when (val value = field.getter.call(o)) {
                    is String -> JSONString(value)
                    is Number -> if (forceString) JSONString(value.toString()) else JSONNumber(value)
                    is Boolean -> if (forceString) JSONString(value.toString()) else JSONBoolean(value)
                    is Enum<*> -> JSONString(value.name)
                    else -> throw IllegalArgumentException("Cannot serialize to JSON")
                }

                jsonObject.addProperty(fieldName, jsonValue)
            }

        return jsonObject
    }
}

class JSONArray : JSONValue() {
    private val items = mutableListOf<JSONValue>()

    fun getItems(): List<JSONValue> {
        return items.toList()
    }

    fun addItem(value: JSONValue) {
        items.add(value)
    }

    override fun toJsonString(indent: Int): String {
        val sb = StringBuilder()
        sb.append("${addIndentation(indent)}[")
        if (items.isNotEmpty()) {
            sb.append("\n")
            sb.append(items.joinToString(",\n") { it.toJsonString(indent + identSpaces) })
            sb.append("\n${addIndentation(indent)}")
        }
        sb.append("${addIndentation(indent + identSpaces / 2)}]")
        return sb.toString()
    }

    override fun search(
        propertyName: String,
        propertyValue: JSONValue,
        results: MutableList<JSONValue>
    ): List<JSONValue> {
        for (item in items) {
            item.search(propertyName, propertyValue, results)
        }
        return results
    }

    override fun mapObject(o: Any): JSONValue {
        return JSONArray()
    }
}


class JSONNull : JSONValue() {
    override fun toJsonString(indent: Int): String {
        return "${addIndentation(indent)}null"
    }

    override fun mapObject(o: Any): JSONValue {
        TODO("Not yet implemented")
    }
}

class JSONBoolean(val value: Boolean) : JSONValue() {
    override fun toJsonString(indent: Int): String {
        return "${addIndentation(indent)}$value"
    }

    override fun mapObject(o: Any): JSONValue {
        TODO("Not yet implemented")
    }
}


class JSONString(val value: String) : JSONValue() {
    override fun toJsonString(indent: Int): String {
        return "${addIndentation(indent)}\"$value\""
    }

    override fun mapObject(o: Any): JSONValue {
        TODO("Not yet implemented")
    }
}

class JSONNumber(val value: Number) : JSONValue() {
    override fun toJsonString(indent: Int): String {
        return "${addIndentation(indent)}$value"
    }

    override fun mapObject(o: Any): JSONValue {
        TODO("Not yet implemented")
    }
}

class JSONDouble(private val value: Double) : JSONValue() {
    override fun toJsonString(depth: Int): String {
        return value.toString()
    }

    override fun mapObject(o: Any): JSONValue {
        TODO("Not yet implemented")
    }
}

private fun addIndentation(indent: Int): String {
    return " ".repeat(indent)
}

//########################################################
//########################################################
//########################################################
//########################################################
//########################################################
//########################################################

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
    @ToString
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
