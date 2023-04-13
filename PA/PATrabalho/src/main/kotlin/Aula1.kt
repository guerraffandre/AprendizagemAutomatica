fun main(args: Array<String>) {
    println("Hello World!")

    println("Program arguments: ${args.joinToString()}")
}

fun isOrdered(list: List<Int>, cresc: Boolean): Boolean {
    for (i in 0 until list.lastIndex) {
        if ((cresc && list[i] > list[i + 1]) || (!cresc && list[i] < list[i + 1])) {
            return false
        }
    }
    return true
}

fun List<Int>.isSorted(cresc: Boolean = true) = isOrdered(this, cresc)

enum class Tipo {
    A, B, C, D
}

fun map(t: Tipo) =
    when (t) {
        Tipo.A -> 5
        Tipo.B -> 0
        else -> 100
    }
//if (t == Tipo.A) 5 else 0