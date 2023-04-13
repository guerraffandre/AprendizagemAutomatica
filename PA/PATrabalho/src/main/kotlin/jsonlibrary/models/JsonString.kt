
class JsonString(private val value: String) : JsonValue() {
    override fun toJsonString(): String {
        return "$value"
    }
}