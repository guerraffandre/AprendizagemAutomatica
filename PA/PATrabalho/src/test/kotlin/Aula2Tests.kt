import java.lang.IllegalArgumentException
import kotlin.test.*

class Aula2Tests {

    @Test
    fun TestFactorial_OK() {
        assertEquals(1, calcFactorial(0))
        assertEquals(1, calcFactorial(1))
        assertEquals(120, calcFactorial(5))
        assertFailsWith<IllegalArgumentException> { calcFactorial(-2) }
    }

    @Test
    fun TestFirstDigit() {
        assertEquals(2, firstDigit(2023))
        assertEquals(2, firstDigit(2))
    }

    @Test
    fun TestSumInt() {
        assertEquals(15, sumRange(1, 5))
    }

    @Test
    fun TestParImparDiv10() {
        assertEquals(NumType.ODD, isNumParImparDiv10(555))
        assertEquals(NumType.DIV10, isNumParImparDiv10(100))
        assertEquals(NumType.PAR, isNumParImparDiv10(12))
        (1..100).filter { i -> isEven(i) }.forEach { x -> println(x) }
        (1..100).filter { i -> isOdd(i) }.forEach { x -> println(x) }
        (1..100).filter { i -> isDiv10(i) }.forEach { x -> println(x) }
        (1..10000).filter { i -> isNumPerfect(i) }.forEach { x -> println(x) }
    }
}