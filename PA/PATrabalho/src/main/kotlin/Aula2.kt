import java.lang.IllegalArgumentException

fun calcFactorial(i: Int): Int {
    tailrec fun auxCalcFactorial(i: Int, f: Int): Int =
        if (i <= 1) f else auxCalcFactorial(i - 1, i * f)

    if (i < 0) throw IllegalArgumentException("negative")
    /*return if (i <= 1) 1 else i * calcFactorial(i - 1)*/
    return auxCalcFactorial(i, 1)
}

//tailrec only work if it doesn't need to go throw all the reverse call's => check before method => auxCalcFactorial solves the issue
tailrec fun firstDigit(i: Int): Int =
    if (i < 10) i else firstDigit(i / 10)


fun sumRange(min: Int, max: Int): Int {
    //regularRecursion
    /*var soma = min + 1
    return if (soma <= max) return soma + sumRange(min + 1, max) else 1*/
    //tailRecursion
    tailrec fun aux(min: Int, max: Int, soma: Int): Int =
        if (min > max) soma else aux(min + 1, max, soma + min)

    return aux(min, max, 0)
}

enum class NumType {
    PAR, ODD, DIV10
}

fun isNumParImparDiv10(i: Int): NumType =
    if (i % 10 == 0) NumType.DIV10
    else if ((i % 10) % 2 > 0) NumType.ODD
    else NumType.PAR

fun isEven(i: Int): Boolean =
    isNumParImparDiv10(i) == NumType.PAR

fun isOdd(i: Int): Boolean =
    isNumParImparDiv10(i) == NumType.ODD

fun isDiv10(i: Int): Boolean =
    isNumParImparDiv10(i) == NumType.DIV10

fun isNumPerfect(num: Int): Boolean {
    tailrec fun aux(div: Int, sum: Int): Int =
        if (div <= num / 2) {
            aux(div + 1, if (num % div == 0) sum + div else sum)
        } else {
            sum
        }
    return aux(1, 0) == num
}

//############ PREDICATE
fun count(list: List<Int>, predicate: (Int) -> Boolean): Int {
    tailrec fun aux(i: Int, c: Int): Int =
        if (i == list.size) c
        else aux(
            i + 1, if (predicate(list[i])) c + 1
            else c
        )
    return aux(0, 0)
}

fun main() {
    val list = listOf(1, 2, -3, 0, -1, 5)
    val criterio: (Int) -> Boolean = { it < 0 } //set the rule <=
    val c = count((list), criterio)
    val c2 = count(list, ::isEven)
    //println(c)
    //println(c2)

    val c3 = sumRangeEx4(1, 5, ::isEven)
    println(c3)
}

fun sumRangeEx4(min: Int, max: Int, predicate: (Int) -> Boolean): Int {
    tailrec fun aux(min: Int, max: Int, soma: Int): Int =
        if (min > max) soma else aux(min + 1, max, (if (predicate(min)) soma + min else soma))

    return aux(min, max, 0)
}