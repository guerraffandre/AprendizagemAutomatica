import Aula7.Composite
import Aula7.Element
import Aula7.Leaf
import Aula7.Visitor
import java.io.File
import java.lang.Exception

fun String.addBrackets() = "($this)"

val String.onlyVowela: Boolean
    get() = this.matches(Regex("[aeiou]*"))

val File.extensionCustom: String
    get() {
        if (!this.name.contains(".")) return ""
        try {
            return this.name.substring(this.name.lastIndexOf(".") + 1)
        } catch (_: Exception) {
        }
        return ""
    }

fun distinctExtensions(files: List<File>): Set<String> {
    return files.map { it.extensionCustom }.filter { it.isNotEmpty() }
        .toSet()  //toSet set doesn't add duplicated => if already exists will not add
}

fun List<File>.countExtension(extension: String): Int {
    return this.map { it.extensionCustom }.filter { x -> x == extension }.size
}

fun List<File>.withExtension(extension: String): List<File> {
    return this.filter { x -> x.extensionCustom == extension }
}


fun deepListFilesRec(file: File, filter: (File) -> Boolean = { true }): List<File> {
    fun aux(file: File, files: MutableList<File>): List<File> {
        file.listFiles()?.forEach {
            if (it.isFile && filter(it)) {
                files.add(it)
            } else if (it.isDirectory) {
                aux(it, files)
            }
        }
        return files
    }
    return aux(file, ArrayList())
}


abstract class Element2 {
    abstract fun accept(v: Visitor2)
}

interface Visitor2 {
    fun visit(c: Ddirectory): Boolean = true
    fun endVisit(c: Ddirectory) {}
    fun visit(l: Ffile) {}
}

class Ffile : Element2() {
    override fun accept(v: Visitor2) {
        v.visit(this)
    }
}

val countLeafs = object : Visitor {
    var count = 0
    override fun visit(l: Leaf) {
        count++
    }
}
val depth = object : Visitor {
    var depth = 0
    var max = 0
    override fun visit(c: Composite): Boolean {
        depth++
        if (depth > max)
            max = depth
        return true
    }

    override fun endVisit(c: Composite) {
        depth--
    }
}


class Ddirectory : Element2() {
    val children: MutableList<Ffile> = mutableListOf()

    override fun accept(v: Visitor2) {
        if (v.visit(this))
            children.forEach {
                it.accept(v)
            }
        v.endVisit(this)
    }
}

fun File.deepListFilesRec2(filter: (File) -> Boolean = { true }): List<File> {
    return deepListFilesRec(this, filter)
}

fun main(args: Array<String>) {
    val path = File(System.getProperty("user.dir") + "/files")

    /*val kotlinFiles = deepListFilesRec(path) {
        it.name.endsWith(".kt")
    }
    kotlinFiles.forEach { println(it.name) }

    val kotlinFiles2 = path.deepListFilesRec2() {
        it.name.endsWith(".txt")
    }
    kotlinFiles2.forEach { println(it.name) }*/

    val kotlinFiles = deepListFilesRec(path)
    kotlinFiles.forEach { println(it.name) }

}
