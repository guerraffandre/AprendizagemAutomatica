package jsonlibrary

import JsonArray
import JsonBoolean
import JsonNull
import JsonNumber
import JsonObject
import JsonString
import java.io.File

fun main(args: Array<String>) {

    val path = File(System.getProperty("user.dir") + "/files")
    //path.listFiles().forEach { println(it.readText()) }
    val json = path.listFiles()?.get(0)?.readText();
    println(json)
    json?.toCharArray()?.forEach {
        println(it)
        if(it.equals("{")){

        }
    }

}

fun testJson(file: File) {
    //TODO test the fileJson { [ ( => same number
    // " tem que ser PAR
}


function parseJson(jsonStr) {
    let index = 0;
    let currentState = 'start';
    let currentObject = {};
    let currentKey = '';
    let currentValue = '';

    while (index < jsonStr.length) {
        const currentChar = jsonStr[index];
        switch (currentState) {
            case 'start':
            if (currentChar === '{') {
                currentState = 'object';
            } else if (currentChar === '[') {
                currentState = 'array';
                currentObject = [];
            }
            break;

            case 'object':
            if (currentChar === '}') {
                return currentObject;
            } else if (currentChar === '"') {
                currentState = 'key';
            }
            break;

            case 'key':
            if (currentChar === '"') {
                currentState = 'colon';
            } else {
                currentKey += currentChar;
            }
            break;

            case 'colon':
            if (currentChar === ':') {
                currentState = 'value';
            }
            break;

            case 'value':
            if (currentChar === ',') {
                currentObject[currentKey] = parseValue(currentValue.trim());
                currentKey = '';
                currentValue = '';
                currentState = 'object';
            } else if (currentChar === '}') {
                currentObject[currentKey] = parseValue(currentValue.trim());
                return currentObject;
            } else {
                currentValue += currentChar;
            }
            break;

            case 'array':
            if (currentChar === ']') {
                return currentObject;
            } else {
                currentObject.push(parseValue(currentChar));
            }
            break;
        }

        index++;
    }

    return currentObject;
}

function parseValue(value) {
    if (value === 'true') {
        return true;
    } else if (value === 'false') {
        return false;
    } else if (value === 'null') {
        return null;
    } else if (!isNaN(parseFloat(value))) {
        return parseFloat(value);
    } else {
        return value;
    }
}