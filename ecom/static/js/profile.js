function openModal() {
  document.getElementById("firstName").value =
    document.getElementById("profileFirstName").textContent;
  document.getElementById("lastName").value =
    document.getElementById("profileLastName").textContent;
  document.getElementById("email").value =
    document.getElementById("profileEmail").textContent;
  document.getElementById("phone").value =
    document.getElementById("profilePhone").textContent;
  document.getElementById("bio").value =
    document.getElementById("profileBio").textContent;
  document.getElementById("country").value =
    document.getElementById("profileCountry").textContent;
  document.getElementById("citystate").value =
    document.getElementById("profileCityState").textContent;
  document.getElementById("postalcode").value =
    document.getElementById("profilePostal").textContent;
  document.getElementById("taxid").value =
    document.getElementById("profileTaxId").textContent;
  document.getElementById("avatarPreview").src =
    document.querySelector(".avatar").src;

  document.getElementById("editModal").classList.add("show");
}
// Live preview when user selects new avatar
document.addEventListener("DOMContentLoaded", function () {
  const avatarInput = document.getElementById("avatarInput");
  const avatarPreview = document.getElementById("avatarPreview");
  avatarInput.addEventListener("change", function (e) {
    if (e.target.files && e.target.files[0]) {
      const reader = new FileReader();
      reader.onload = function (ev) {
        avatarPreview.src = ev.target.result;
      };
      reader.readAsDataURL(e.target.files[0]);
    }
  });
});

// In your saveChanges function, update the profile avatar
function saveChanges(e) {
  e.preventDefault();
  // ...existing save logic for other fields...

  // Update avatar in profile
  const avatarPreview = document.getElementById("avatarPreview");
  const profileAvatar = document.querySelector(".avatar");
  if (avatarPreview && profileAvatar) {
    profileAvatar.src = avatarPreview.src;
  }

  closeModal();
}

function closeModal() {
  document.getElementById("editModal").classList.remove("show");
}
function saveChanges(e) {
  e.preventDefault();
  document.getElementById("profileFirstName").textContent =
    document.getElementById("firstName").value;
  document.getElementById("profileLastName").textContent =
    document.getElementById("lastName").value;
  document.getElementById("profileEmail").textContent =
    document.getElementById("email").value;
  document.getElementById("profilePhone").textContent =
    document.getElementById("phone").value;
  document.getElementById("profileBio").textContent =
    document.getElementById("bio").value;
  document.getElementById("profileCountry").textContent =
    document.getElementById("country").value;
  document.getElementById("profileCityState").textContent =
    document.getElementById("citystate").value;
  document.getElementById("profilePostal").textContent =
    document.getElementById("postalcode").value;
  document.getElementById("profileTaxId").textContent =
    document.getElementById("taxid").value;
  document.getElementById("profileName").textContent =
    document.getElementById("firstName").value +
    " " +
    document.getElementById("lastName").value;
  document.getElementById("profileMeta").textContent =
    document.getElementById("bio").value +
    " | " +
    document.getElementById("citystate").value;
  closeModal();
}
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeModal();
});
document.getElementById("editModal").addEventListener("click", (e) => {
  if (e.target === e.currentTarget) closeModal();
});
