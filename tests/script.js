Apologies, but there seems to be misunderstanding. Since your original code is not provided, I cannot modify it for you. However, here is an example of calculating Simple Interest using parseFloat in JavaScript:

```javascript
// Input values
let principle = prompt("Please enter the principle amount");
let rate = prompt("Please enter the rate of interest (in %)");
let time = prompt("Please enter the time (in years)");

// Change the input to float numbers
principle = parseFloat(principle);
rate = parseFloat(rate);
time = parseFloat(time);

// Calculate Simple Interest
let simpleInterest = (principle * rate * time) / 100;

// Output the result
console.log(`The simple interest is: ${simpleInterest}`);
```

This code asks for user inputs for the principle amount, rate of interest, and time. parseFloat() method is used here to convert the string numerical input to a floating number. The formula for Simple Interest is then applied, and the result is printed using console.log().