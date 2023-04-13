import kotlin.test.*

class Aula4Tests {

    val main = DirectoryElement("main")
    val kotlin = DirectoryElement("kotlin", main)
    val examples = FileElement("Examples.kt", kotlin)
    val week2 = FileElement("Week2.kt", kotlin)
    val week3 = FileElement("Week3.kt", kotlin)
    val resources = DirectoryElement("resources", main)


    @Test
    fun testDepth() {
        assertEquals(1, main.depth)
        assertEquals(2, kotlin.depth)
        assertEquals(3, examples.depth)
    }

    @Test
    fun testPath() {
        println(examples.getPath(""))
    }
}