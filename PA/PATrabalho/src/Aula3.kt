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

fun File.deepListFilesRec2(filter: (File) -> Boolean = { true }): List<File> {
    return deepListFilesRec(this, filter)
}

fun main(args: Array<String>) {
    val path = File(System.getProperty("user.dir") + "/files")

    val kotlinFiles = deepListFilesRec(path) {
        it.name.endsWith(".kt")
    }
    kotlinFiles.forEach { println(it.name) }

    val kotlinFiles2 = path.deepListFilesRec2() {
        it.name.endsWith(".txt")
    }
    kotlinFiles2.forEach { println(it.name) }
}
