// Dismiss functionality for all notifications
document.querySelectorAll(".dismissible .close-btn").forEach((btn) => {
  btn.addEventListener("click", function () {
    this.parentElement.style.display = "none";
  });
});
