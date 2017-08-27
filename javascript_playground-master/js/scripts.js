//vars
var name = 'Conner';
// data types
// strings
var string = 'this is a string';

//arrays work like python lists
var array = ['we would call this a list in python']

//javascript objects (look like python dictionaries)
var jsobj = {
    key1: 'value1',
    'key2': 'value2',
    key3: {},
};

// int
var int =1231341451341;

//float
var float = 3.14;

function myFunction(nm){
    //console.log(nm);
    alert(nm);
}

//myFunction(name);

var greeting = function(nm){
    var greet = 'Hello ';
    console.log(greet + nm);
};

//greeting(name)

function testBool(){
    // || is or in python
    //var bool = (true || !true);

    //&& is and in python
    //var bool = (true && false);

    // === is == in python
    //var bool = ('1 == 1); //true
    //var bool = ('1' === 1); //true

    //!== is != or not in python
    //var bool = ('1' !== 1) //false

    var bool = ('1' >= 1); //true
    console.log(bool)
}

//control flow
var num = Math.floor(Math.random() * 100) - 1;
function guessNumber(guess){
    var message;
    var list = document.getElementById('message');
    var li = document.createElement('li');
    if (guess > num){
        message = 'You guessed higher than the number';
    }
    else if (guess < num){
        message = 'You guessed lower than the number';
    }
    else{
        message = ('You Win!! The number was ' + num);
    }
    console.log(message);
    li.appendChild(document.createTextNode(message));
    list.appendChild(li);
    document.getElementById(li);
}

//guessNumber();


document.getElementById('guess').addEventListener('click', function(){
    event.preventDefault();
    var ourGuess = document.getElementById('valueGuess').value;
    guessNumber(ourGuess);
    // console.log('I have been clicked');
});

document.getElementById('mainBoldText').style.color = '#ff0000';
document.getElementById('mainBoldText').style.fontWeight = 'bold';
