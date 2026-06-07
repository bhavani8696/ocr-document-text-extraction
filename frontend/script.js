document.getElementById("extract-btn").addEventListener("click", async () => {

    const fileInput = document.getElementById("file-input");

    if (fileInput.files.length === 0) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();

    formData.append("image", fileInput.files[0]);

    try {

        const response = await fetch("http://127.0.0.1:5000/ocr", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("output").innerText = data.text;

    } catch (error) {

        alert("Something went wrong");
        console.log(error);

    }

});