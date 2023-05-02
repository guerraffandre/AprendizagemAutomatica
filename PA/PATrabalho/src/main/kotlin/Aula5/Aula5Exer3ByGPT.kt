import kotlin.reflect.KProperty

import kotlin.reflect.full.memberProperties

interface TypeMapping {
    fun mapType(p: KProperty<*>): String
    fun mapObject(o: Any?): String
}

class SQLGenerator(private val typeMapping: TypeMapping) {
    fun generateInsertSQL(obj: Any, tableName: String): String {
        val properties = obj::class.memberProperties
        val columnNames = properties.joinToString(", ") { it.name }
        val values = properties.joinToString(", ") { property ->
            val value = typeMapping.mapObject(property.call(obj))
            value
        }
        return "INSERT INTO $tableName ($columnNames) VALUES ($values)"
    }

    fun generateSelectSQL(tableName: String, condition: String): String {
        return "SELECT * FROM $tableName WHERE $condition"
    }
}

object OracleTypeMapping : TypeMapping {
    override fun mapType(p: KProperty<*>): String {
        return when (p.returnType.toString()) {
            "kotlin.Int" -> "NUMBER"
            "kotlin.String" -> "VARCHAR2(255)"
            else -> throw IllegalArgumentException("Unsupported property type: ${p.returnType}")
        }
    }

    override fun mapObject(o: Any?): String {
        return when (o) {
            is String -> "'$o'"
            else -> o.toString()
        }
    }
}

object MySQLTypeMapping : TypeMapping {
    override fun mapType(p: KProperty<*>): String {
        return when (p.returnType.toString()) {
            "kotlin.Int" -> "INT"
            "kotlin.String" -> "VARCHAR(255)"
            else -> throw IllegalArgumentException("Unsupported property type: ${p.returnType}")
        }
    }

    override fun mapObject(o: Any?): String {
        return when (o) {
            is String -> "'$o'"
            else -> o.toString()
        }
    }
}

fun main() {
    val student = Student(12345, "John Doe", StudentType.Bachelor)

    val oracleGenerator = SQLGenerator(OracleTypeMapping)
    val oracleInsertSQL = oracleGenerator.generateInsertSQL(student, "STUDENT")
    val oracleSelectSQL = oracleGenerator.generateSelectSQL("STUDENT", "NUMBER = 12345")

    println("Oracle INSERT SQL: $oracleInsertSQL")
    println("Oracle SELECT SQL: $oracleSelectSQL")

    val mysqlGenerator = SQLGenerator(MySQLTypeMapping)
    val mysqlInsertSQL = mysqlGenerator.generateInsertSQL(student, "STUDENT")
    val mysqlSelectSQL = mysqlGenerator.generateSelectSQL("STUDENT", "NUMBER = 12345")

    println("MySQL INSERT SQL: $mysqlInsertSQL")
    println("MySQL SELECT SQL: $mysqlSelectSQL")
}