class FileElement(
    override val name: String,
    override var parent: DirectoryElement? = null
) : Element {
    init {
        parent?.children?.add(this)
    }

    fun getPath(name: String): String {
        return this.parent?.getPath(name) ?: ""
    }
}