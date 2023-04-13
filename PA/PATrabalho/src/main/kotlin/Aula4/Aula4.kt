package Aula4

interface IntValue {
    val integer: Int
    fun increment()
    val isNegative: Boolean
        get() = integer < 0
}

open class Counter(value: Int = 0) : IntValue { // this is a constructor
    override var integer: Int = value
        //private set
        set(value) {//alternative to the set method
            require(value >= 0)
            field = value
        }

    /*override val integer: Int
        get() = this.value*/
    init {
        require(value >= 0)
    }

    override fun increment() {
        this.integer++
    }

    val isZero: Boolean
        //is like a method 'isZero()'
        get() = integer == 0
}

class SpecialCounter : Counter() {
    override fun increment() {
        this.integer + 2
    }
}

fun main() {
    val c = Counter(5)
    println(c.integer)
    c.integer = 4
    println(c.integer)
    println(c.isZero)

    val x = SpecialCounter()
    println(x)
    x.increment()
    println(x)
}

