/**
 * Created by Conner on 6/26/2017.
 */

// var val = Math.floor(Math.random() * 6) + 1;
var round = 1;


function Die (id) {
  this.dieImage = ""
  this.id = id;
  this.val = 0;
  this.held = false;
  this.setVal= function(){
    if(!this.held) {
        this.val = Math.floor(Math.random() * 6) + 1;
        if(this.val == 1){
          this.dieImage = "C:\Users\Conner\Desktop\Web_Bootcamp\Labs\dice_angry\imgs\die_01_42158_sm.jpg";
          document.getElementById(this.id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/1.png')";
        }
        else if(this.val == 2){
          this.dieImage = "C:\Users\Conner\Desktop\Web_Bootcamp\Labs\dice_angry\imgs\die_02_42159_sm.jpg";
          document.getElementById(this.id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/2.png')";
        }
        else if(this.val == 3){
          this.dieImage = "C:\Users\Conner\Desktop\Web_Bootcamp\Labs\dice_angry\imgs\die_03_42160_sm.jpg";
          document.getElementById(this.id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/angry.png')";
        }
        else if(this.val == 4){
          this.dieImage = "C:\Users\Conner\Desktop\Web_Bootcamp\Labs\dice_angry\imgs\die_04_42161_sm.jpg";
          document.getElementById(this.id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/4.png')";
        }
        else if(this.val == 5){
          this.dieImage = "C:\Users\Conner\Desktop\Web_Bootcamp\Labs\dice_angry\imgs\die_05_42162_sm.jpg";
          document.getElementById(this.id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/5.png')";
        }
        else if(this.val == 6){
          this.dieImage = "C:\Users\Conner\Desktop\Web_Bootcamp\Labs\dice_angry\imgs\die_06_42164_sm.jpg";
          document.getElementById(this.id).style.backgroundImage = "url('C:/Users/Conner/Desktop/Web_Bootcamp/Labs/dice_angry/imgs/6.png')";
        }

    }

  };

}

function changeRound(){
  document.getElementById('round').innerHTML = round.toString();
}

function releaseHold(){
  die1.held = false;
  die2.held = false;
  document.getElementById(die1.id).style.borderColor = 'black';
  document.getElementById(die2.id).style.borderColor = 'black';
}

function checkRound(){
  if(die1.val == 3 && die2.val == 3){
      round = 1;
      changeRound();
      releaseHold();
      document.getElementById('message').innerHTML = "Angry Dice, Start Over"
  }
  else if(round == 1 && die1.val + die2.val == 3){
    round = 2;
    changeRound();
    releaseHold();

  }
  else if(round == 2 && ((die1.val == 3 && die2.val == 4) || (die1.val == 4 && die2.val == 3))){
    round = 3;
    changeRound();
    releaseHold();
  }
  else if(round == 3 && die1.val + die2.val === 11){
    document.getElementById('message').innerHTML = 'You Win!!!';
    changeRound();
    releaseHold();
  }


}

var die1 = new Die('die1');
var die2 = new Die('die2');

document.getElementById('roll').addEventListener('click', function(e){
  e.preventDefault();
  die1.setVal();
  die2.setVal();
  document.getElementById('message').innerHTML = '';
  checkRound();

});

document.getElementById('reset').addEventListener('click', function(e){
  e.preventDefault();
  round = 1;
  changeRound();
  document.getElementById('message').innerHTML = '';
});

var dieDivs = document.getElementsByClassName('dieClick');

Array.from(dieDivs).forEach(function(el){
  el.addEventListener('click', function(){

    if(this.id == 'die1' && !die1.held && !(die1.val == 6)){
      die1.held = true;
      this.style.borderColor = 'red';
    }
    else if(this.id == 'die1' && die1.held){
      die1.held = false;
      this.style.borderColor = 'black';
    }
    else if(this.id == 'die2' && !die2.held && !(die2.val == 6)){
      die2.held = true;
      this.style.borderColor = 'red';
    }
    else if(this.id == 'die2' && die2.held){
      die2.held = false;
      this.style.borderColor = 'black';
    }
  })
});


//
// console.log(die1);
// console.log(die2);