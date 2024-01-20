// alert("Welcome user")
// const myHeading = document.querySelector("h1");
// myHeading.textContent = "Hello world!";
// document.querySelector("html").addEventListener("click", function () {
//     alert("Ouch! Stop poking me!");
//   });

// var deposit = prompt("How much would you like to deposit today?");
// alert("You've deposited: "+deposit);
// console.log("joss!")

// var convert = prompt("How much would you like to convert the pounds?");
// convert = convert * 0.454;
// alert("You've converted into: "+convert+" KG");
// console.log("joss conversion!")

// var temperature = prompt("What is the temperature today?");
// var hot = false;
// var report = "ksiuna"
// if (temperature > 80  && temperature < 100) {
//   hot = true;
//   report= "It's hot outside!";
// }
// else{
//     report= "It's thanda outside!";
// }

// console.log(report)


// var elaf = prompt("Enter a number");

// while (elaf < 20) {
//   console.log(" Elaf is currently " + elaf + " years old which isnt");
//     if (elaf === "12") {
//       console.log(" Elaf is currently " + elaf + " years old. WHICH IS TRUUUUUUUUUUUU");
//       break;
//     }
//     // else {
//     //   console.log(" Elaf is not currently " + elaf + " years old.");
//     // }
    
//     elaf++;
// }

// var elaf = Number(prompt("Enter a number"));

// for (var i = 0; i < elaf; i++) {
//   console.log(" Elaf is currently " + i + " years old which isnt");
//   // if (i === 12) {
//   //   console.log(" Elaf is currently " + i + " years old. WHICH IS TRUUUUUUUUUUUU");
//   //   break;
//   // }
//   // else {
//   //   console.log(" Elaf is not currently " + i + " years old.");
//   // }

// }

// var elaf = Number(prompt("Enter a number"));

// for (var i = 0; i < elaf; i++) {
//   if (i % 2 !== 0) {
//     console.log(" Elaf is currently " + i + " years old which is odd");
//   }
//   else {
//     console.log(" Elaf is not currently " + i + " years old which is even");
//   }

// }




// var name = prompt("Enter name");
// var Age = prompt("Enter your age");
// var Height = prompt("Enter your height");
// var Pet = prompt("Enter your pet name");
// var nameParts = name.split(" "); // splits the name into two parts

// if (nameParts[0][0] === nameParts[1][0]) {
// // nameParts[0][0] is the first letter of the first name
// // nameParts[1][0] is the first letter of the second name
// // 0 is the first character and 0 is the first letter of the first name
// // 1 is the second character and 0 is the first letter of the second name
//  console.log("The first and second names share the same initial letter.");
// } else {
//  console.log("The first and second names do not share the same initial letter.");
// }

// if (Age > 20 && Age < 30) {
//     console.log("Age is between 20 and 30");
// }

// if (Height >= 170) {
//     console.log("Height is greater than 170");
// }

// if (Pet[Pet.length-1] === "y"){
//     console.log("Pet name ends with y");  
// }

// if (nameParts[0][0] === nameParts[1][0] && Age > 20 && Age < 30 && Height >= 170 && Pet[Pet.length-1] === "y") {
//     alert("Welcome spy!");
// }
// else{
//     alert("Welcome" + name + "! You have passed the spy test");
// }

// var v = " GLOBAL V";
// var stuff = "GLOBAL STUFF";

// function fun(stuff) {
//     console.log(v);
//     // stuff = "Reassign stuff inside func";
//     console.log(stuff);
//     }

// fun();
// console.log(stuff);

// var dhukaArray = []

// function addNew() {
//     var askName = prompt("What would you add here?")
//     dhukaArray.push(askName)
// }
// function remove(){
//     var removeName = prompt("What would you remove here?")
// // This line finds the index of the removeName in the dhukaArray. The indexOf method returns the first index at which a given element can be found in the array, or -1 if it is not present.
//     var index = dhukaArray.indexOf(removeName)
// // This line removes the item at the specified index from the dhukaArray. The splice method changes the contents of an array by removing or replacing existing elements. In this case, it's removing one element at the position index.
//     dhukaArray.splice(index,1)
// } 
// function display(){
//     console.log(dhukaArray)
// }
// var start = prompt("Would you like to start the app? y/n")
// var request = "empty"

// if (start === 'y'){
//     while (request!== "quit"){
//         request = prompt("Please select an action: add, remove, display, or quit")
//         if (request === 'add'){
//             addNew() //call function
//         }
//         else if (request === 'display'){
//             display()
//         }
//         else if (request === 'remove'){
//             remove()
//         }
//         else{
//             alert("Not recognized")
//             request = "quit"
//         }
//     }
// }


var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,
    nameLength: function(){
        console.log(this.name.length)
    }
}


var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,
    report: function(){
        alert("Name is "+this.name+", Job is "+this.job+", Age is "+this.age)
    }
}
var employee = { 
    name: "John Smith",
    job: "Programmer",
    age: 31,
    lastName: function(){
        var splitName = this.name.split(" ")
        console.log(splitName[1])
    }
}