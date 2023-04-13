package jsonlibrary

import java.io.File
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
}