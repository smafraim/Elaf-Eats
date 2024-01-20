// taking variable of header and changing color
var header = document.querySelector("h1")
var navheader = document.querySelector("a.navabar-brand")

// function getRandomColor() {
//     var letters = "0123456789ABCDEF";
//     var color = "#";
//     for (var i=0; i<6; i++) {
//         // Math.floor(Math.random()*16) part generates a random integer between 0 and 15, which is used as an index to pick a character from letters
//         color += letters[Math.floor(Math.random()*16)];
//     }
//     return color;
// }

// function changeHeaderColor() {
//     colorInput = getRandomColor();
//     header.style.color = colorInput;
//     navheader.style.color = colorInput;

// }

// setInterval("changeHeaderColor()",1000);

// var p = document.querySelector("p")
// var pA = document.querySelector("a")

var head1 = document.querySelector("#nigga")
var head2 = document.querySelector("#niggabai")

head1.addEventListener("mouseover", function() {
    head1.textContent = "YOURE A NIGGA";
    head1.style.color = "red";
})
head1.addEventListener("mouseout", function(){
    head1.textContent = "You;re back to human1!!"
    head1.style.color= "black";
})
let isClicked = false;

head2.addEventListener("click", function(){
   if (!isClicked) {
       head2.textContent = "you killed a nigga";
       head2.style.color = "red";
       isClicked = true;
   } else {
       head2.textContent = "You unkilled that nigga";
       head2.style.color = "black";
       isClicked = false;
   }
});