import kotlin.reflect.KClass
import kotlin.reflect.full.findAnnotation
import kotlin.reflect.full.memberProperties


fun generateTableSQL(clazz: KClass<*>): String {
    val tableName = clazz.simpleName?.toUpperCase() ?: error("Invalid class name")
    val properties = clazz.memberProperties

    val columns = properties.joinToString(",\n") { prop ->
        val columnName = prop.findAnnotation<DbName>()?.name ?: prop.name.toUpperCase()
        val columnType = when (prop.returnType.toString()) {
            "kotlin.Int" -> "INT"
            "kotlin.String" -> "VARCHAR(${prop.findAnnotation<Length>()?.length ?: 255})"
            "StudentType" -> "ENUM('Bachelor', 'Master', 'Doctoral')"
            else -> error("Invalid data type")
        }
        val primaryKey = if (prop.findAnnotation<PrimaryKey>() != null) "PRIMARY KEY" else ""
        "$columnName $columnType $primaryKey"
    }

    return "CREATE TABLE $tableName (\n$columns\n);"
}

fun main() {
    val sql = generateTableSQL(Student::class)
    println(sql)
}
