const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const alertBox = document.getElementById("alert-box");

const handleAlerts = (type, msg) => {
	alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
        ${msg}
    </div>
    `;
};

Dropzone.autoDiscover = false;
const myDropzone = new Dropzone("#my-dropzone", {
	url: "/reports/upload/",
	init: function () {
		this.on("sending", function (file, xhr, formData) {
			console.log("sending");
			formData.append("csrfmiddlewaretoken", csrf);
		});
		this.on("success", function (file, response) {
			console.log(response);
			const ex = response.ex;
			if (ex) {
				handleAlerts("danger", "File is already exists.");
			} else {
				handleAlerts("success", "Your file has been uploaded.");
			}
		});
	},
	maxFiles: 3,
	masFilesize: 3,
	acceptedFiles: ".csv",
});
