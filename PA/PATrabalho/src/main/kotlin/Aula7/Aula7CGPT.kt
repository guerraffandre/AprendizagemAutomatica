interface Visitor {
    fun visitFile(file: File)
    fun visitDirectory(directory: Directory)
}

abstract class File(val name: String) {
    abstract fun accept(visitor: Visitor)
}

class Directory(name: String) : File(name) {
    val elements = mutableListOf<File>()

    override fun accept(visitor: Visitor) {
        visitor.visitDirectory(this)
    }

    fun addElement(element: File) {
        elements.add(element)
    }
}

class TextFile(name: String, val content: String) : File(name) {
    override fun accept(visitor: Visitor) {
        visitor.visitFile(this)
    }
}

class ImageFile(name: String, val size: Int) : File(name) {
    override fun accept(visitor: Visitor) {
        visitor.visitFile(this)
    }
}

class FindByNameVisitor(private val name: String) : Visitor {
    private var foundFile: File? = null

    override fun visitFile(file: File) {
        if (file.name == name) {
            foundFile = file
        }
    }

    override fun visitDirectory(directory: Directory) {
        for (element in directory.elements) {
            element.accept(this)
            if (foundFile != null) {
                break
            }
        }
    }

    fun getFoundFile(): File? {
        return foundFile
    }
}

class CountByExtensionVisitor(private val extension: String) : Visitor {
    private var count: Int = 0

    override fun visitFile(file: File) {
        if (file.name.endsWith(".$extension")) {
            count++
        }
    }

    override fun visitDirectory(directory: Directory) {
        for (element in directory.elements) {
            element.accept(this)
        }
    }

    fun getCount(): Int {
        return count
    }
}

class DepthVisitor : Visitor {
    private var maxDepth: Int = 0
    private var currentDepth: Int = 0

    override fun visitFile(file: File) {
        // do nothing
    }

    override fun visitDirectory(directory: Directory) {
        currentDepth++
        if (currentDepth > maxDepth) {
            maxDepth = currentDepth
        }
        for (element in directory.elements) {
            element.accept(this)
        }
        currentDepth--
    }

    fun getMaxDepth(): Int {
        return maxDepth
    }
}

fun printFileTree(root: File, indent: String = "") {
    println("$indent${root.name}")
    if (root is Directory) {
        for (element in root.elements) {
            printFileTree(element, "$indent  ")
        }
    }
}

fun main(args: Array<String>) {
    // create a file hierarchy
    val root = Directory("root")
    val subDir1 = Directory("subDir1")
    val subDir2 = Directory("subDir2")
    val textFile1 = TextFile("textFile1.txt", "Hello, world!")
    val textFile2 = TextFile("textFile2.txt", "Lorem ipsum dolor sit amet.")
    val imageFile1 = ImageFile("imageFile1.png", 1024)
    val imageFile2 = ImageFile("imageFile2.jpg", 2048)

    root.addElement(subDir1)
    root.addElement(subDir2)
    root.addElement(textFile1)
    subDir1.addElement(textFile2)
    subDir1.addElement(imageFile1)
    subDir2.addElement(imageFile2)

    // perform visitor operations on the file hierarchy
    val findVisitor = FindByNameVisitor("textFile2.txt")
    root.accept(findVisitor)
    println("Found file: ${findVisitor.getFoundFile()?.name}")

    val countVisitor = CountByExtensionVisitor("png")
    root.accept(countVisitor)
    println("Number of png files: ${countVisitor.getCount()}")

    val depthVisitor = DepthVisitor()
    root.accept(depthVisitor)
    println("Max depth: ${depthVisitor.getMaxDepth()}")

    // print the file tree
    printFileTree(root)
}
