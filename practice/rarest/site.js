/**
 * Created by Conner on 6/26/2017.
 */
var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};


function findRarestValue(map){
    var key;
    var occur = {};
    var lowestOccurVal = 999;
    var rarestAge = 0;
    var rarestList = [];
    for(key in map){
        occur[map[key]] =0;
    }
    for(key in map){
        occur[map[key]] = occur[map[key]] + 1;
    }
    console.log(occur);

    for(key in occur){
        if(occur[key] < lowestOccurVal){
            lowestOccurVal = occur[key];
        }
    }
    console.log(lowestOccurVal);

    for(key in occur){
        if(occur[key] == lowestOccurVal){
            rarestAge = key;
        }
    }
    console.log(rarestAge);


    for(key in map){
        if(map[key] == rarestAge){
            rarestList.push(key);
        }
    }
    console.log(rarestList);

}


findRarestValue(namesToAges);