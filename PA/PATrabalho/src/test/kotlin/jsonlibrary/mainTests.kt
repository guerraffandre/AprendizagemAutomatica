package jsonlibrary

import java.lang.IllegalArgumentException
import kotlin.test.*

class mainTests {

    @Test
    fun TestFactorial_OK() {
        assertEquals(1, calcFactorial(0))
        assertEquals(1, calcFactorial(1))
        assertEquals(120, calcFactorial(5))
        assertFailsWith<IllegalArgumentException> { calcFactorial(-2) }
    }
}