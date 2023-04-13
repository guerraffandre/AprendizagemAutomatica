class JsonObject : JsonValue() {
    private val properties = mutableMapOf<String, JsonValue>()

    fun addProperty(name: String, value: JsonValue) {
        properties[name] = value
    }

    override fun toJsonString(): String {
        val propertyStrings = properties.map { (name, value) ->
            "\"$name\": ${value.toJsonString()}"
        }.joinToString(", ")
        return "{ $propertyStrings }"
    }
}