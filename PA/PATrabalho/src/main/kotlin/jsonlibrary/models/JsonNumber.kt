

class JsonNumber(private val value: Number) : JsonValue() {
    override fun toJsonString(): String {
        return value.toString()
    }
}

