let currentProductID;
function closePopUp() {
    document.getElementById("pop-up").classList.add("hidden");
}
function openPopUp(id) {
    document.getElementById("pop-up").classList.remove("hidden");
    currentProductID = id;
}
function deleteProduct() {
    window.location.href = `/Venta/${currentProductID}/delete`;
};