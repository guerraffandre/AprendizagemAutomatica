
class JsonArray : JsonValue() {
    private val items = mutableListOf<JsonValue>()

    fun addItem(item: JsonValue) {
        items.add(item)
    }

    override fun toJsonString(): String {
        val itemStrings = items.map { it.toJsonString() }.joinToString(", ")
        return "[ $itemStrings ]"
    }
}