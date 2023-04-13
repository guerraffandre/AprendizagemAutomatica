import java.io.File
import java.lang.IllegalArgumentException
import kotlin.test.*

class Aula3Tests {

    private val fileList = listOf(
        File("random"),
        File("Test.kt"),
        File("Example.kt"),
        File("Script.kts")
    )

    @Test
    fun fileExtension() {
        assertEquals("", File("random").extensionCustom)
        assertEquals("kt", File("Test.kt").extensionCustom)
        assertEquals("kts", File("build.gradle.kts").extensionCustom)
    }

    @Test
    fun distinctExtensions() {
        assertEquals(setOf("kt", "kts"), distinctExtensions(fileList))
    }

    @Test
    fun countExtensions() {
        assertEquals(2, fileList.countExtension("kt"))
        assertEquals(0, fileList.countExtension("txt"))
    }

    @Test
    fun withExtension() {
        val expected = listOf(File("Test.kt"), File("Example.kt"))
        assertEquals(expected, fileList.withExtension("kt"))
        assertEquals(emptyList<File>(), fileList.withExtension("txt"))
    }

}