import kotlin.reflect.KClass
import kotlin.reflect.KClassifier
import kotlin.reflect.KProperty
import kotlin.reflect.KType
/*import kotlin.reflect.full.declaredMemberProperties
import kotlin.reflect.full.isSubclassOf
import kotlin.reflect.full.primaryConstructor

@Target(AnnotationTarget.CLASS, AnnotationTarget.PROPERTY)
annotation class DbName(val name: String)

@Target(AnnotationTarget.PROPERTY)
annotation class Length(val length: Int)

@Target(AnnotationTarget.PROPERTY)
annotation class PrimaryKey


@DbName("STUDENT")
data class Student(
    @PrimaryKey
    val number: Int,
    @Length(50)
    val name: String,
    @DbName("degree")
    val type: StudentType
)

enum class StudentType {
    Bachelor, Master, Doctoral
}

// obtem lista de atributos pela ordem do construtor primario
val KClass<*>.dataClassFields: List<KProperty<*>>
    get() {
        require(isData) { "instance must be data class" }
        return primaryConstructor!!.parameters.map { p ->
            declaredMemberProperties.find { it.name == p.name }!!
        }
    }

// saber se um KClassifier é um enumerado
val KClassifier?.isEnum: Boolean
    get() = this is KClass<*> && this.isSubclassOf(Enum::class)

// obter uma lista de constantes de um tipo enumerado
val <T : Any> KClass<T>.enumConstants: List<T>
    get() {
        require(isEnum) { "instance must be enum" }
        return java.enumConstants.toList()
    }


fun KType.getSqlType(): String {
    if (this.classifier!!.isEnum) return "ENUM" + StudentType::class.enumConstants.toString()
        .replace("[", "('")
        .replace(", ", "', '")
        .replace("]", "')") //(‘Bachelor’, ‘Master’, ‘Doctoral’)
    else
        when (this.classifier) {
            Int::class -> "INT"
            String::class -> "CHAR"
        }
    return ""
}

fun Any?.getSqlType(): Any {
    if (this == null) return ""
    if (this::class.isInstance(Int)) return this
    else if (this::class.isInstance(String)) return "\"" + this + "\""
    return ""
}

fun createTable(c: KClass<*>): String {
    var str = "CREATE TABLE ${c.simpleName} ("
    c.dataClassFields.forEach {
        str += it.name + " "
        str += it.returnType.getSqlType() + " "
        if (!it.returnType.isMarkedNullable) str += " NOT NULL, " else str += " , "
    }
    /*c.declaredMemberProperties.forEach { //println(it.name)
    }
    c.declaredMemberFunctions.forEach {
        //println(it.name)
        //println(it.returnType)
        //println(it.returnType.isMarkedNullable)
    }*/
    return str + ");"
}

fun insertInto(c: Any): String {
    var str = "INSERT INTO ${c::class.simpleName} ("
    str += c::class.dataClassFields.joinToString { it.name } + ") VALUES ("
    str += c::class.dataClassFields.joinToString { it.call(c).getSqlType().toString() }
    return str
}

fun main() {
    val fields: List<KProperty<*>> = Student::class.dataClassFields
    //println(fields)
    val isEnum = StudentType::class.isEnum
    //println(isEnum)
    val enumConstants: List<StudentType> = StudentType::class.enumConstants
    //println(enumConstants)

    val clazz: KClass<*> = Student::class
    val sql: String = createTable(clazz)
    //println(sql)
    //CREATE TABLE Student (number INT NOT NULL, name CHAR NOT NULL, type ENUM(‘Bachelor’, ‘Master’, ‘Doctoral’));

    val s = Student(7, "Cristiano", StudentType.Doctoral)
    val sql2: String = insertInto(s)
    println(sql2)
    //INSERT INTO Student (number, name, type) VALUES (7, ‘Cristiano’, ‘Doctoral’);
}*/