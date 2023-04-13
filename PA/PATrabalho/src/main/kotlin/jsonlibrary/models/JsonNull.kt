

class JsonNull : JsonValue() {
    override fun toJsonString(): String {
        return "null"
    }
}