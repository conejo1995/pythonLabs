/**
 * Created by Conner on 6/26/2017.
 */

// var val = Math.floor(Math.random() * 6) + 1;
var round = 1;
var valOne = 1;
var valTwo = 1;
var heldOne = false;
var heldTwo = false;
var idOne = "die1";
var idTwo = "die2";

function setVal(){
  var val = Math.floor(Math.random() * 6) + 1;
  if(!heldOne) {
      valOne = val;
  }
  changeBackground(valOne, idOne, heldOne);
  val = Math.floor(Math.random() * 6) + 1;
  if(!heldTwo) {
      valTwo = val;
  }
  changeBackground(valTwo, idTwo, heldTwo);

}

function changeBackground(value, id, held){
  if(!held) {
        if(value == 1){
          // $(id).css('background-image', 'url(C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/1.png)');
          document.getElementById(id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/1.png')";
        }
        else if(value == 2){
          document.getElementById(id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/2.png')";
        }
        else if(value == 3){
          document.getElementById(id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/angry.png')";
        }
        else if(value == 4){
          document.getElementById(id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/4.png')";
        }
        else if(value == 5){
          document.getElementById(id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/5.png')";
        }
        else if(value == 6){
          document.getElementById(id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/6.png')";
        }

    }

}

function changeRound(){
  $('#round').html(round.toString());
  // document.getElementById('round').innerHTML = round.toString();
}

function releaseHold(){
  heldOne = false;
  heldTwo = false;
  document.getElementById(idOne).style.borderColor = 'black';
  document.getElementById(idTwo).style.borderColor = 'black';
}

function checkRound(){
  if(valOne == 3 && valTwo == 3){
      round = 1;
      changeRound();
      releaseHold();
      document.getElementById('message').innerHTML = "Angry Dice, Start Over"
  }
  else if(round == 1 && valOne + valTwo == 3){
    round = 2;
    changeRound();
    releaseHold();

  }
  else if(round == 2 && ((valOne == 3 && valTwo == 4) || (valOne == 4 && valTwo == 3))){
    round = 3;
    changeRound();
    releaseHold();
  }
  else if(round == 3 && valOne + valTwo === 11){
    document.getElementById('message').innerHTML = 'You Win!!!';
    changeRound();
    releaseHold();
  }
}

$('#roll').click(function(e){
  e.preventDefault();
  setVal();
  setVal();
  $('#message').html("");
  checkRound();
  console.log(valOne, valTwo);
});


$('#reset').click(function(e){
  e.preventDefault();
  round = 1;
  changeRound();
  $('#message').html("");

});



$('.dieClick').click(function(){

    if($(this).attr('id') == 'die1' && !heldOne && !(valOne == 6)){
      heldOne = true;
      $(this).css('borderColor', 'red');
    }
    else if($(this).attr('id') == 'die1' && heldOne){
      heldOne = false;
      $(this).css('borderColor', 'black');
    }
    else if($(this).attr('id') == 'die2' && !heldTwo && !(valTwo == 6)){
      heldTwo = true;
      $(this).css('borderColor', 'red');
    }
    else if($(this).attr('id') == 'die2' && heldTwo){
      heldTwo = false;
      $(this).css('borderColor', 'black');
    }
});

