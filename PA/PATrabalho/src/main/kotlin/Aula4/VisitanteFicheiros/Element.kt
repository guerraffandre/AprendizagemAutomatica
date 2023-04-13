sealed interface Element {
    val name: String
    var parent: DirectoryElement?
        get() = this.parent
        set(value) {
            if (value != null) {
                this.parent = value
            }
        }

    var depth: Int
        get() = (this.parent?.depth ?: 0) + 1
        set(value) {
            this.depth = value
        }

}