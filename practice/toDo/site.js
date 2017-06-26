/**
 * Created by Conner on 6/26/2017.
 */
document.getElementById('submit').addEventListener('click', function(){
    event.preventDefault();
    var toDo = document.getElementById('toDo').value;
    addToList(toDo);
    console.log(toDo);
});

function addToList(task){
    var list = document.getElementById('message');
    var li = document.createElement('li');
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "name";
    checkbox.value = "value";
    checkbox.id = "id";
    // if (guess > num){
    //     message = 'You guessed higher than the number';
    // }
    // else if (guess < num){
    //     message = 'You guessed lower than the number';
    // }
    // else{
    //     message = ('You Win!! The number was ' + num);
    // }
    li.appendChild(document.createTextNode(task));
    li.appendChild(checkbox);
    list.appendChild(li);
    document.getElementById('toDo').value = "";
}