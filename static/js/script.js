document.addEventListener("DOMContentLoaded", function () {
    console.log("BHAVANAM JS Loaded");

    const district = document.getElementById("district");
    const location = document.getElementById("location");

    district.addEventListener("change", function () {
        const districtId = this.value;

        fetch(`/locations/get-locations/?district=${districtId}`)
            .then(response => response.json())
            .then(data => {
                location.innerHTML = '<option value="">Select Location</option>';

                data.forEach(item => {
                    const option = document.createElement("option");
                    option.value = item.id;
                    option.textContent = item.name;
                    location.appendChild(option);
                });
            })
            .catch(error => console.error(error));
    });
});
function changeImage(image){

    document.getElementById("mainImage").src = image.src;

}