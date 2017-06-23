//
// //control flow
// var num = Math.floor(Math.random() * 100) - 1;
// function guessNumber(guess){
//     var message;
//     var list = document.getElementById('message');
//     var li = document.createElement('li');
//     if (guess > num){
//         message = 'You guessed higher than the number';
//     }
//     else if (guess < num){
//         message = 'You guessed lower than the number';
//     }
//     else{
//         message = ('You Win!! The number was ' + num);
//     }
//     console.log(message);
//     li.appendChild(document.createTextNode(message));
//     list.appendChild(li);
//
// }
//
//
// document.getElementById('guess').addEventListener('click', function(){
//     event.preventDefault();
//     var ourGuess = document.getElementById('valueGuess').value;
//     guessNumber(ourGuess);
// });
//
// document.getElementById('mainBoldText').style.color = '#ff0000';
// document.getElementById('mainBoldText').style.fontWeight = 'bold';

document.getElementById('changeBackground').addEventListener('click', function(){
     event.preventDefault();
     var ourColor = document.getElementById('valueColor').value;
     background(ourColor);
 });

function background(aColor){
    var backgroundColor = document.getElementById('body');
    backgroundColor.style.backgroundColor = aColor;

};

function Color(r, g, b){
    if(r < 255){
        this.r = r;
    }
    else if (r>=255){
        this.r = 255;
    }
    else{
        this.r
    }

    if(g < 255){
        this.g = g;
    }
    else if (g>=255){
        this.g = 255;
    }

    if(b < 255){
        this.b = b;
    }
    else if (b>=255){
        this.b = 255;
    }

    this.toHex = function() {
        var hexValue = '#';
        hexString = this.r.toString(16);
        hexValue = hexValue + hexString;
        hexString = this.g.toString(16);
        hexValue = hexValue + hexString;
        hexString = this.b.toString(16);
        hexValue = hexValue + hexString;
        console.log(hexValue);
        return hexValue;

    };

    this.blendAdd = function(otherColor) {
        newR = this.r + otherColor.r;
        newG = this.g + otherColor.g;
        newB = this.b + otherColor.b;
        return new Color(newR, newG, newB)
    };
}

var yellow = new Color(255, 255, 0);
yellow.toHex();  //> '#FFFF00'
var purple = new Color(255, 0, 255);
purple.toHex();  //> '#FF00FF'
var white = yellow.blendAdd(purple);
white.toHex(); 