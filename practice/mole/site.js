/**
 * Created by Conner on 6/29/2017.
 */
var rowID = ['#row1', '#row2', '#row3', '#row4', '#row5'];
var childString = [' div:nth-child(1)',' div:nth-child(2)',' div:nth-child(3)',' div:nth-child(4)'];
var gridBackgrounds = ["url('https://lh3.googleusercontent.com/35cwworGsxBUr4bm1Nv3RV6iDedCpQp002kqicY4tiM9nJG6_ft6YqC85gws_u-EO3gGRQY=s103')",
    "url('https://s-media-cache-ak0.pinimg.com/originals/d6/71/79/d6717919294eed8c11d6542332fe62db.png')"
];
// var boardData;
//
// function leaderBoard() {
//     $.ajax({
//         url: "http://demo8461502.mockable.io/this",
//         data: {
//
//         },
//         dataType: "json",
//         type: "post",
//         success: function (data) {
//             console.log(data);
//
//         }
//     });
//
// }
//
// leaderBoard();





var running = false;
var t = 0;
var inter = 1000;
var timer;
var score = 0;
var moles = 0;

$('#start').click(function () {
    running = true;
    timer = setInterval(function () {
        t += 1;
        console.log(t);
        $('#timer').html(t);
        updateGrid();
    }, inter)
});

$('#stop').click(function () {
    running = false;
    clearInterval(timer);
});

$('#reset').click(function () {
    clearInterval(timer);
    running = false;
    t = 0;
    score = 0;
    $('#timer').html('-');
    $('#score').html('-');

    var row = 0;
    var column =0;
    var string;
    var type;
    for(row = 0; row <= 4; row++){
        for(column = 0; column <= 5; column++){
            type = $(rowID[row] + childString[column]).html();
            if(type == 'mole'){
                $(rowID[row] + childString[column]).html("hole");
            }
        }
    }
    inter = 1000;
    clearMoles();
});

$('div').click(function(el){
    var type = this.innerHTML;
    // console.log(type);
    if(type == 'mole' && running){
        score += 100;
        $('#score').html(score);
        moles -= 1;
        this.innerHTML = 'hole';
        clearMoles();
    }
    else if(type == 'hole' && running){
        score -= 50;
        $('#score').html(score);
    }

});

function clearMoles(){
    var row = 0;
    var column =0;
    var string;
    var type;
    for(row = 0; row <= 4; row++){
        for(column = 0; column <= 5; column++){
            type = $(rowID[row] + childString[column]).html();
            if(type == 'hole'){
                $(rowID[row] + childString[column]).css("background-image", gridBackgrounds[0]);
            }
        }
    }
}


function updateGrid(){
    var row = rowID[Math.floor(Math.random() * 5)];
    var column = childString[Math.floor(Math.random() * 4)];
    console.log(row + column);
    var type = $(row + column).html();
    // console.log(type);
    if(t%10 == 0){
        inter -= 100;
        clearInterval(timer);
        timer = setInterval(function () {
            t += 1;
            console.log(t);
            $('#timer').html(t);


            updateGrid();
        }, inter)
    }

    if(type == 'hole') {
        $(row + column).css("background-image", gridBackgrounds[1]);
        $(row + column).html('mole');
        moles +=1;
    }
    else if(moles == 20){
        clearInterval(timer);
        running = false;
        alert("You scored " + score + " in " + t + "seconds");
    }
    else{
        updateGrid();
    }




}