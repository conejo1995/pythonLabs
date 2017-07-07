/**
 * Created by Conner on 7/6/2017.
 */
$('.ui.checkbox').checkbox();

var total = 6.00;



$("[name='included-ingredients'], [name='extra-ingredients'], [name='meat']").on('change', function(){
    //console.log($(this).next('label').text());
    var list = document.getElementById('ingredients').firstElementChild;
    var li = document.createElement('li');
    li.setAttribute("class", "item");
    var elements = list.getElementsByTagName('li');
    var present = false;
    var index = 0;

    //check list to see if an element is in it
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].innerHTML == $(this).next('label').text()) {
            present = true;
            index = i;
        }
    }


    if(present == false){
     //Add element to list
     li.appendChild(document.createTextNode($(this).next('label').text()));
     list.appendChild(li);
    }

    if(present == true){
        list.removeChild(elements[index]);
    }

});


$("[name='tortilla']").on('change', function(){
    console.log($(this).next('label').text());
    var list = document.getElementById('ingredients').firstElementChild;
    var elements = list.getElementsByTagName('li');
    var li = document.createElement('li');
    li.setAttribute("class", "item");
    li.appendChild(document.createTextNode($(this).next('label').text()));
    list.removeChild(elements[0]);
    list.prepend(li);

});


$("[name='extra-ingredients']").on('change', function(){
    //console.log($(this).next('label').text());
    var list = document.getElementById('ingredients').firstElementChild;
    var li = document.createElement('li');
    li.setAttribute("class", "item");
    var elements = list.getElementsByTagName('li');
    var present = false;


    //check list to see if an element is in it
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].innerHTML == $(this).next('label').text()) {
            present = true;
        }
    }


    if(present == false){
        total = total - 0.50;
    }

    if(present == true){
        total = total + 0.50;
    }
    document.getElementById("total_cost").innerHTML = "Total: $" + total.toString()
    if(total%1 == 0){
        $("#total_cost").append(".00");
    }
    else{
        $("#total_cost").append("0");
    }


});

$("[name='delivery']").on('change', function(){
    console.log($(this).next('label').text());
    if($(this).next('label').text()=="Delivery (additional $5.00 delivery fee)"){
        total = total + 5.00;
    }
    else if($(this).next('label').text()=="Pick-Up"){
        total = total - 5.00;
    }
    document.getElementById("total_cost").innerHTML = "Total: $" + total.toString();
    if(total%1 == 0){
        $("#total_cost").append(".00");
    }
    else{
        $("#total_cost").append("0");
    }

});


$("[type='submit']").click(function(e){
  e.preventDefault();
  document.getElementById("error-messages").innerHTML = "Please correct the following errors before proceeding.<br>";
  var valid1 = validName();
  var valid2 = validCreditCard();
  var valid3 = validCVV();
  var valid4 = validZipCode();
  var valid5 = acceptedTandC();

  if(!valid1 || !valid2 || !valid3 || !valid4 || !valid5){
      document.getElementById('error-messages').style.display = 'block';
  }
  else{
      document.getElementById('error-messages').style.display = 'none';
  }


});


function validName(){
    var name = $("[name='name']").val();
    console.log(name);
    nameRegEx = /^[a-z ,.'-]+$/i;

    if(nameRegEx.test(name)){
        return true;
    }
    else{
        $("#error-messages").append("• Enter a valid name. Can only contain: [A-Z][a-z][,][.][ ]['][-]<br>");
        return false;
    }
}


function validCreditCard() {

  var ccNum = $('#credit-card').val();
  var visaRegEx = /^(?:4[0-9]{15})$/;
  var mastercardRegEx = /^(?:5[1-5][0-9]{14})$/;
  var amexpRegEx = /^(?:3[47][0-9]{13})$/;
  var discovRegEx = /^(?:6(?:011|5[0-9][0-9])[0-9]{12})$/;
  var isValid = false;

  if (visaRegEx.test(ccNum)) {
    isValid = true;
  }
  else if(mastercardRegEx.test(ccNum)) {
    isValid = true;
  }
  else if(amexpRegEx.test(ccNum)) {
    isValid = true;
  }
  else if(amexpRegEx.test(ccNum)) {
    isValid = true;
  }

  if(isValid) {
      return true;
  }
  else {
      $("#error-messages").append("• Enter a credit card number.<br>");
      return false;
  }
}


function validCVV(){
    var cvv = $('#cvv').val();
    var cvvRegEx = /^[0-9]{3,4}$/;

    if (cvvRegEx.test(cvv)){
        return true;
    }
    else{
        $("#error-messages").append("• Enter your credit card's verification number (CVV).<br>");
        return false;
    }


}

function validZipCode(){
    var zipCode = $('#zip').val();
    var zipRegEx = /^[0-9]{5}$/;

    if (zipRegEx.test(zipCode)){
        return true;
    }
    else{
        $("#error-messages").append("• Enter the ZIP Code associated with the credit card.<br>");
        return false;
    }
}

function acceptedTandC(){
    if($('input[name="terms"]:checked').length > 0){
        return true;
    }
    else{
        $("#error-messages").append("• Agree to the Terms & Conditions!!!<br>");
        return false;
    }

}
