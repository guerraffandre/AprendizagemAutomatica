package Aula7

import deepListFilesRec
import deepListFilesRec2
import java.io.File

abstract class Element {
    abstract fun accept(v: Visitor)
}

class Leaf : Element() {
    override fun accept(v: Visitor) {
        v.visit(this)
    }
}

class Composite : Element() {
    val children: MutableList<Element> = mutableListOf()

    override fun accept(v: Visitor) {
        if (v.visit(this))
            children.forEach {
                it.accept(v)
            }
        v.endVisit(this)
    }
}

interface Visitor {
    fun visit(c: Composite): Boolean = true
    fun endVisit(c: Composite) {}
    fun visit(l: Leaf) {}
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