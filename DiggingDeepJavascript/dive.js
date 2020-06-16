import { data } from './data.mjs'; 
import { mockData } from './mockGameData.mjs';
//This isnt a promise anymore! O:

function CheckIfObjectType(value){
    return (typeof(value) === 'object' ? true : false); 
}

function CheckIfArrayType(value){
    return Array.isArray(value);
}

//NOT IN USE UNTILL TESTED!
function RECURSIVE_GetItemsFromObject(object){
    console.log("using Recursive Function...")
    for(let item in object){
        //console.log(newFavThingsObject[item])
        console.log(`object[item].stringify = ${JSON.stringify(item)} : [${typeof(object[item])}] ${object[item]}`)

        //Check if object again
        if(CheckIfObjectType(object[item])){
            console.log(`\nFound Complex Object... Converting to Iterable structure...\n`)
            var computerObject = new Object(object[item]);
            //return RECURSIVE_GetItemsFromObject(nextObject)
            for(let item in computerObject){
                console.log(`Line:31 ${JSON.stringify(item)} : [${typeof(computerObject[item])}] ${computerObject[item]}`)
                if(CheckIfObjectType(computerObject[item])){
                    console.log(`\nFound Complex Object... Converting to Iterable structure...\n`)
                    var leftOverObjects = new Object(computerObject[item]);
                    for(let item in leftOverObjects){
                        console.log(`Line:35 ${JSON.stringify(item)} : [${typeof(leftOverObjects[item])}] ${leftOverObjects[item]}`)
                    }
                }
                else{
                    console.log(`l:38 - ${computerObject[item]}`)
                }
            }
        }
        else{
            console.log(`l:43 - ${object[item]}`)
            //mappableItems.set(JSON.stringify(item), object[item])
            // return mappableItems;
        }
    }
}

function GenerateMappableItems(convertObject){
    let map = new Map();
    for(let item in convertObject){
        map.set(item, convertObject[item])
    }
    return map;
}

//NOT IN USE UNTILL TESTED!
function ConvertArrayTypes(arr){
    for(let i in arr){
        console.log(typeof(i))
        if(CheckIfObjectType(i)){
            console.log(arr[i])
            ConvertObjectTypes(arr[i])
            //return GenerateMappableItems(arr[i])
        }else{
            console.log(arr[i])
            //return arr[i]
        }
    }
}

function ConvertObjectTypes(data){
    for(let i in data){ //loops through items in object
        console.log(`${i}:[${typeof(data[i])}] ${data[i]}`)
        //mappableItems.set(i, data[i])
        if(CheckIfObjectType(data[i])){
            console.log(`----Found Complex Object... Converting to Iterable structure...\n`)
            var favoriteThingsObject = data[i];
            for(let item of favoriteThingsObject){
                let newFavThingsObject = new Object(item)
                console.log(`---- l:52 ${JSON.stringify(item)} : [${typeof(favoriteThingsObject[item])}] ${favoriteThingsObject[item]}`)

                //TODO: TESTING NEEDED
                //RECURSIVE_GetItemsFromObject(newFavThingsObject)

                for(let item in newFavThingsObject){
                    console.log(`----------- l:58 ${JSON.stringify(item)} : [${typeof(newFavThingsObject[item])}] ${newFavThingsObject[item]}`)
    
                    if(CheckIfObjectType(newFavThingsObject[item])){
                        console.log(`\nFound Complex Object... Converting to Iterable structure...\n`)
                        var computerObject = new Object(newFavThingsObject[item]);
                        for(let item in computerObject){
                            console.log(`----------- Line:31 ${JSON.stringify(item)} : [${typeof(computerObject[item])}] ${computerObject[item]}`)
                            if(CheckIfObjectType(computerObject[item])){
                                console.log(`\nFound Complex Object... Converting to Iterable structure...\n`)
                                var leftOverObjects = new Object(computerObject[item]);
                                for(let item in leftOverObjects){
                                    console.log(`----------- Line:35 ${JSON.stringify(item)} : [${typeof(leftOverObjects[item])}] ${leftOverObjects[item]}`)
                                    if(CheckIfObjectType(leftOverObjects[item])){
                                        //let resultIsMap = GenerateMappableItems(leftOverObjects[item])
                                        return GenerateMappableItems(leftOverObjects[item])
                                        // console.log('line:80 --- Showing Mappable Items')
                                        // for(let entry of resultIsMap){
                                        //     console.log(entry)
                                        // }
                                        //return resultMap
                                    }
                                    else{
                                        console.log(`l:85 - ${leftOverObjects[item]}`)
                                    }
                                }
                            }
                            else{
                                console.log(`l:38 - ${computerObject[item]}`)
                            }
                        }
                    }
                    else{
                        console.log(`l:43 - ${newFavThingsObject[item]}`)
                    }
                }
            }
        }
        else{
            console.log(`l:49 - ${data[i]}`)
            //mappableItems.set(i, data[i])
        }
    }
}
//var list_of_complexObjects = []
//var mappableItems = new Map()

//let resultMap = ConvertObjectTypes(data);
let resultMap = ConvertObjectTypes(data);

//Final Map!
for(let entry of resultMap){
    console.log(entry)
}
