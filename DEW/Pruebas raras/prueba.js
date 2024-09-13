function calc(){
    const price = parseFloat(document.getElementById("price").value);
    const qty = parseFloat(document.getElementById("qty").value);

    const result = price * qty;

    document.getElementById("result").textContent = result
}