function calculateStats() {
    // Get input values
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    var num3 = parseFloat(document.getElementById('num3').value);

    if (isNaN(num1) || isNaN(num2) || isNaN(num3)) {
        alert("Please enter valid numbers.");
        return;
    }

    // Store numbers in an array and sort them
    var numbers = [num1, num2, num3].sort(function(a, b) {
        return a - b;
    });

    // Calculate max, min, mean, median, and range
    var max = numbers[2]; // max is last in sorted array
    var min = numbers[0]; // min is first in sorted array
    var mean = (num1 + num2 + num3) / 3;
    var median = numbers[1]; // median is the middle of the sorted array
    var range = max - min;

    // Display results
    document.getElementById('max').innerText = 'Max: ' + max;
    document.getElementById('min').innerText = 'Min: ' + min;
    document.getElementById('mean').innerText = 'Mean: ' + mean.toFixed(2);
    document.getElementById('median').innerText = 'Median: ' + median;
    document.getElementById('range').innerText = 'Range: ' + range;
}
