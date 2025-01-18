

// Tools Logic

// Snake Water Gun Game
function snakeWaterGun() {
    alert('Starting Snake Water Gun Game!');
    // Game logic
    // ...
    let userScore = 0;
    let botScore = 0;
    const choices = ['snake', 'water', 'gun'];
    const rounds = 5;

    for (let i = 0; i < rounds; i++) {
        let userChoice = prompt("Choose snake, water, or gun:").toLowerCase();
        let botChoice = choices[Math.floor(Math.random() * choices.length)];

        if ((userChoice === 'snake' && botChoice === 'water') ||
            (userChoice === 'water' && botChoice === 'gun') ||
            (userChoice === 'gun' && botChoice === 'snake')) {
            userScore++;
            alert(`Round ${i + 1}: You win! Bot chose ${botChoice}.`);
        } else if (userChoice === botChoice) {
            alert(`Round ${i + 1}: It's a tie! Both chose ${botChoice}.`);
        } else {
            botScore++;
            alert(`Round ${i + 1}: You lose! Bot chose ${botChoice}.`);
        }
    }

    alert(`Final Score: You: ${userScore}, Bot: ${botScore}`);

}

// Attach the function to the global window object
window.snakeWaterGun = snakeWaterGun;

// Secret Message Encoder/Decoder
function secretMessage() {
    alert('Starting Secret Message Encoder/Decoder!');
    // Encoder/Decoder logic
    // ...
    alert('Starting Secret Message Encoder/Decoder!');
    let message = prompt("Enter your message to encode or decode:");
    let action = prompt("Type 'encode' to encode the message or 'decode' to decode it:").toLowerCase();
    let transformedMessage = "";

    if (action === "encode") {
        transformedMessage = message.split(' ').map(word => {
            let prefix = Math.random().toString(36).substring(2, 6);
            let suffix = Math.random().toString(36).substring(2, 6);
            let newWord = word.length > 3 ? word.slice(1) + word[0] : word.split('').reverse().join('');
            return prefix + newWord + suffix;
        }).join(' ');
        alert(`Encoded message: ${transformedMessage}`);
    } else if (action === "decode") {
        transformedMessage = message.split(' ').map(word => {
            let cleanWord = word.slice(4, -4);
            let newWord = cleanWord.length > 3 ? cleanWord.slice(-1) + cleanWord.slice(0, -1) : cleanWord.split('').reverse().join('');
            return newWord;
        }).join(' ');
        alert(`Decoded message: ${transformedMessage}`);
    } else {
        alert("Invalid action. Please type 'encode' or 'decode'.");
    }
}

// Attach the function to the global window object
window.secretMessage = secretMessage;

// Kaun Banega Arabpati Quiz
function kaunBanega() {
    alert('Starting Kaun Banega Arabpati Quiz!');
    // Quiz logic
    // ...
    const questions = [
        {
            question: "What is the capital of France?",
            options: ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            correctAnswer: "A"
        },
        {
            question: "Which planet is known as the Red Planet?",
            options: ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            correctAnswer: "B"
        },
        {
            question: "Who wrote 'Hamlet'?",
            options: ["A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Jane Austen"],
            correctAnswer: "A"
        }
    ];

    let score = 0;

    questions.forEach((q, index) => {
        let answer = prompt(`${q.question}\n${q.options.join('\n')}`).toUpperCase();
        if (answer === q.correctAnswer) {
            score += 1000;
            alert(`Correct! You've earned ₹${score}.`);
        } else {
            alert("Wrong answer!");
        }
    });

    alert(`Your final winnings: ₹${score}`);
}

window.kaunBanega = kaunBanega;

// Marks Calculator
function marksCalculator() {
    alert('Starting Marks, Pass, and Fail Calculator!');
    // Calculator logic
    // ...
    let p = parseFloat(prompt("Enter marks obtained in Physics:"));
    let c = parseFloat(prompt("Enter marks obtained in Chemistry:"));
    let m = parseFloat(prompt("Enter marks obtained in Maths:"));
    let passingPercent = parseFloat(prompt("Enter your passing percentage:"));

    let total = p + c + m;
    let percent = (total * 100) / 300;

    alert(`Total marks obtained: ${total}/300`);
    alert(`Percentage: ${percent}%`);

    if (percent >= passingPercent) {
        if (percent <= 50) {
            alert("Passed with 3rd Division");
        } else if (percent <= 74) {
            alert("Passed with 2nd Division");
        } else {
            alert("Passed with 1st and Topper Division");
        }
    } else {
        alert("Fail");
    }
}

window.marksCalculator = marksCalculator;

// Scientific Calculator
function scientificCalculator() {
    alert('Starting Scientific Calculator!');
    // Calculator logic
    // ...
    let op = prompt("Choose an operation: /, *, +, -, power, root, trigonometric ratio:").toLowerCase();

    switch (op) {
        case "/":
            let n1 = parseFloat(prompt("Enter your 1st number:"));
            let n2 = parseFloat(prompt("Enter your 2nd number:"));
            if (n2 === 0) {
                alert("Zero is not allowed in the denominator.");
            } else {
                alert(`Division: ${n1 / n2}`);
            }
            break;
        case "*":
            n1 = parseFloat(prompt("Enter your 1st number:"));
            n2 = parseFloat(prompt("Enter your 2nd number:"));
            alert(`Multiplication: ${n1 * n2}`);
            break;
        case "+":
            n1 = parseFloat(prompt("Enter your 1st number:"));
            n2 = parseFloat(prompt("Enter your 2nd number:"));
            alert(`Sum: ${n1 + n2}`);
            break;
        case "-":
            n1 = parseFloat(prompt("Enter your 1st number:"));
            n2 = parseFloat(prompt("Enter your 2nd number:"));
            alert(`Subtraction: ${n1 - n2}`);
            break;
        case "power":
            n1 = parseFloat(prompt("Enter your number:"));
            n2 = parseFloat(prompt("Enter power of your number:"));
            alert(`Power: ${n1 ** n2}`);
            break;
        case "root":
            n1 = parseFloat(prompt("Enter your number:"));
            alert(`Square Root: ${Math.sqrt(n1)}`);
            break;
        case "trigonometric ratio":
            let theta = parseFloat(prompt("Enter the value of Theta (in degrees):"));
            let trigOp = prompt("Sin, Cos, Tan, Cosec, Sec, Cot:").toLowerCase();
            let rad = (theta * Math.PI) / 180;

            switch (trigOp) {
                case "sin":
                    alert(`Sin(${theta}): ${Math.sin(rad)}`);
                    break;
                case "cos":
                    alert(`Cos(${theta}): ${Math.cos(rad)}`);
                    break;
                case "tan":
                    alert(`Tan(${theta}): ${Math.tan(rad)}`);
                    break;
                case "cosec":
                    alert(`Cosec(${theta}): ${1 / Math.sin(rad)}`);
                    break;
                case "sec":
                    alert(`Sec(${theta}): ${1 / Math.cos(rad)}`);
                    break;
                case "cot":
                    alert(`Cot(${theta}): ${1 / Math.tan(rad)}`);
                    break;
                default:
                    alert("Invalid trigonometric ratio.");
            }
            break;
        default:
            alert("Invalid operation.");
    }

}

window.scientificCalculator = scientificCalculator;
