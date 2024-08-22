// by: neverfriendme;
// Prompt calculator starting!;
function Calculator(){
    var choice = prompt("Division, Addition, Multiplication, Subtraction.");
    if (choice === "Division") {
        const div1 = Number(prompt("First number: "));
        const div2 = Number(prompt("Second number: "));
        const ans = div1 / div2;
        alert("The quotent is " + ans);
    }
    if (choice === "Addition") {
        const add1 = Number(prompt("First number: "));
        const add2 = Number(prompt("Second number: "));
        const ans2 = add1 + add2;
        alert("The sum is " + ans2);
    }
    if (choice === "Multiplication") {
        const mul1 = Number(prompt("First number: "));
        const mul2 = Number(prompt("Second number: "));
        const ans3 = mul1 * mul2;
        alert("The product is " + ans3);
    }
    if (choice === "Subtraction") {
        const sub1 = Number(prompt("First number: "));
        const sub2 = Number(prompt("Second number: "));
        const ans4 = sub1 - sub2;
        alert("The product is " + ans4);
    }
}

