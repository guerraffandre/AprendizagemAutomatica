package jsonlibrary


import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import java.io.File
import java.util.*
import kotlin.test.*

class mainTests {

    @Test
    fun Test() {
        assertEquals("1", "1")
    }

    @Test
    fun testReadJsonFile() {
        val json = File("example.json").readText()
        assertNotNull(json)
    }
    @Test
    fun validaEstrutura(): Boolean {
        val json = File("example.json").readText()
        var index = 0
        val stack = Stack<Char>()

        while (index < json.length) {
            val c = json[index]

            when (c) {
                '{', '[', '(' -> stack.push(c)
                '}', ']', ')' -> {
                    if (stack.isEmpty()) {
                        return false
                    }

                    val last = stack.pop()
                    if ((last == '{' && c != '}') ||
                        (last == '[' && c != ']') ||
                        (last == '(' && c != ')')) {
                        return false
                    }
                }
            }

            index++
        }

        return stack.isEmpty()
    }











}