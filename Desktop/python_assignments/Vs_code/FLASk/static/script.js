function calculateAddition() {
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;

    if (num1 === "" || num2 === "") {
        document.getElementById("result").innerText = "Please enter both numbers.";
        return;
    }

    fetch(`/addition?num1=${num1}&num2=${num2}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").innerText = data.error;
            } else {
                document.getElementById("result").innerText = data.result;
            }
        })
        .catch(error => console.error("Error:", error));
}
