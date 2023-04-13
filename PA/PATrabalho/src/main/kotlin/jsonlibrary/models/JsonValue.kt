
// Define the basic JSON types
sealed class JsonValue {
    abstract fun toJsonString(): String
}