class DirectoryElement : Element {
    override var name: String
    override var parent: DirectoryElement? = null

    fun getPath(name: String): String {
        if (parent == null) return name
        return this.parent!!.getPath(name)
    }

    var children: MutableList<FileElement> = mutableListOf()

    constructor(name: String) {
        this.name = name
    }

    constructor(name: String, parent: DirectoryElement) {
        this.name = name
        this.parent = parent
    }

    /*fun deepElementCount(parent: DirectoryElement): Int {
        tailrec fun aux(parent: DirectoryElement?, count: Int): Int {
            if (parent != null) {
                count + 1
                return aux(parent.parent, count)
            }
            return count
        }

        return aux(parent, 0)
    }*/
}