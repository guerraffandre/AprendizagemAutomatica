interface JsonVisitor<T> {
    fun visit(obj: JsonObject): T
    fun visit(array: JsonArray): T
    fun visit(string: JsonString): T
    fun visit(number: JsonNumber): T
    fun visit(bool: JsonBoolean): T
    fun visit(nullValue: JsonNull): T
}