// Declare global elements with jQuery
var clipboardIconTemplate = `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">
<path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/>
<path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/>
</svg>`

var backButton = $("<button class='send-button' id='send' onclick='backToMainForm()></button>'");
var contentBox = $(".content-box");
var clipboardIcon = $(clipboardIconTemplate);


function retrieveFormData() {

    var jobUrl = document.querySelector("#job-link").value;
    var jobTitle = document.querySelector("#job-title").value;
    var language = document.querySelector("#language").value;
    var firstName = document.querySelector('#name').value;
    var lastName = document.querySelector('#surname').value;
    var age = document.querySelector('#age').value;
    var interests = document.querySelector('#interests').value;
    var aboutMe = document.querySelector('#about').value;

    var details = {
        "job_url": jobUrl,
        "details": {
            "job_title": jobTitle,
            "language": language,
            "person_name": firstName,
            "person_surname": lastName,
            "person_age": age,
            "person_interests": interests,
            "person_about": aboutMe
        }
    };

    return details;
}


function validateFormData(data_dict) {

    for (const key in data_dict) {
        // Declare current item in the list as variable
        var currentInputElement = data_dict[key];
        if (currentInputElement == null) {
            return false; 
        } 
        
    return true;
    }


}
// Center main box 
function centerElements(boxWidth, boxHeight) {
    var width = screen.availWidth;
    var height = screen.availHeight;

    var top = ((height - boxHeight) / 2)
    var left = (((width - boxWidth) / 2) / 1080) * 100;

    // Can make this connected to shadow and center both of them

    var containerDiv = $(".form-box-main");

    containerDiv.css(
        {
            "top": top / 4 + "px",
        }
    );
}


// This functions animate text in labels to go above the input form 
function animateInputsLabels(side) {
    if (side == "age") {
        var topUp = "0px";
        var topDown = "60px";
    } else if (side == "about") {
        var topUp = "140px";
        var topDown = "200px";
    } else {
        var topUp = "-30px";
        var topDown = "35px";
    }

    $("." + side + "-input").focus(function() {
    var id = this.id;
    var element = "label[for=" + this.id + "]";

    $(element).css({"top": topUp});
})

// Make the text go back to its root position
$("." + side + "-input").on("focusout", function() {
    if (this.value.length == 0) {
        var labelElement = "label[for=" + this.id + "]";

        $(labelElement).css({"top": topDown});
    }
});
}


// Update Send Button so it has unique id and tex for each state e.g = 'send', 'loading', 'back'
function updateBackButton(state) {
    var loadingSquare = $("<div class=\"square\"></div>");

    // state="send" means convert button id="send" text="Send"
    if (state == "send") {
        sendButton.id = "send";
        sendButton.text("Send");
    }
    else if (state == "loading") {
        contentBox.append(backButton);
        backButton.text("");
        backButton.append(loadingSquare);
    }
    else if (state == "back") {
        backButton.remove(loadingSquare);
        backButton.id = "back";
        backButton.text("Back");
    }
    else {
        console.log({"error": "Button cannot be set to state: " + state});
    }
}


// Fill the main box either with form or clean it
function updateContentBox(mode) {

    // Declare the HTML for form 
    var contentBoxHtml = `
    <form onsubmit="sendDataToEndpoint()">
            <div class="input-box">
            <label for="name" class="left-input-label">Name</label>
            <input class="left-input" id="name" type="text" name="name" placeholder=" " required>

            <label for="surname" class="left-input-label" style="left: 320px; text-align: right;">Surname</label>
            <input class="right-input" id="surname" type="text" value=" " name="surname" placeholder=" " required>
        </div>

        <div class="input-box">
            <label for="interests" class="left-input-label">Interests</label>
            <input class="left-input" id="interests" type="text" name="interests" placeholder=" " required>

            <label for="language" class="left-input-label" style="left: 320px;">Language</label>
            <input class="right-input" id="language" type="text" name="language" placeholder=" " required>
        </div>

        <div class="input-box">
            <label for="job-title" class="left-input-label">Job Title</label>
            <input class="left-input" id="job-title" type="text" name="job-title" placeholder=" "required>

            <label for="job-link" class="left-input-label" style="left: 320px;">Job Link</label>
            <input class="right-input" id="job-link" type="text" name="job-link" placeholder=" "required>
        </div>

        <label for="age" class="left-input-label" style="left: 630px; top: 62px;">Age</label>
        <input class="age-input" id="age" type="text" name="age" placeholder="" required>

        <label for="about" class="left-input-label" style="left: 630px; top: 200px;">About</label>
        <textarea class="about-input" id="about" type="text" name="about" placeholder=" " required></textarea>

        <input class="send-button" type="submit" value="Send">
    </form>`;

    if (mode == "empty") {
        contentBox.empty();
        updateBackButton("back");
    } 
    else if (mode == "fill") {
        contentBox.append(contentBoxHtml);
        animateInputsLabels("left");
        animateInputsLabels("right");
        animateInputsLabels("age");
        animateInputsLabels("about");
    }
}


function sendDataToEndpoint() {
    

        var details = retrieveFormData();
        console.log(details);

        var valid = validateFormData(details);

        var jsonDetails = JSON.stringify(details);

        contentBox.remove($("input .send-button"));
        // Zamien tekst 'Send' w buttonie na element ladowania
        updateBackButton("loading");

        // Wyslij zapytanie do serwera
        /* fetch("http://localhost:5000/api/complete/", {headers: {"Content-Type": "application/json"}, method: "POST", body: jsonDetails})
            .then(response => {

                if (response.ok) {
                    return response.json()
                }
            })
                .then(data => {

                    updateContentBox("empty");
                    contentBox.text(data["data"]);

                }) */
            updateContentBox("empty");
            contentBox.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer efficitur nibh nec justo efficitur interdum. Duis consequat diam sit amet nulla pellentesque ultrices. Pellentesque mattis dapibus eleifend. Aenean dignissim lobortis libero sit amet pretium. Morbi id libero massa. Pellentesque efficitur lacus nec tempus molestie. Quisque at pellentesque dolor. Curabitur id diam ac justo commodo pellentesque quis ut quam. Fusce est velit, viverra quis odio sit amet, condimentum fringilla magna. Vivamus non ex ut dui tristique hendrerit eget ac lectus. Fusce tincidunt laoreet nibh, eu mattis dui rhoncus sit amet. Quisque condimentum cursus felis, at tristique orci convallis et.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer efficitur nibh nec justo efficitur interdum. Duis consequat diam sit amet nulla pellentesque ultrices. Pellentesque mattis dapibus eleifend. Aenean dignissim lobortis libero sit amet pretium. Morbi id libero massa. Pellentesque efficitur lacus nec tempus molestie. Quisque at pellentesque dolor. Curabitur id diam ac justo commodo pellentesque quis ut quam. Fusce est velit, viverra quis odio sit amet, condimentum fringilla magna. Vivamus non ex ut dui tristique hendrerit eget ac lectus. Fusce tincidunt laoreet nibh, eu mattis dui rhoncus sit amet. Quisque condimentum cursus felis, at tristique orci convallis et.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer efficitur nibh nec justo efficitur interdum. Duis consequat diam sit amet nulla pellentesque ultrices. Pellentesque mattis dapibus eleifend. Aenean dignissim lobortis libero sit amet pretium. Morbi id libero massa. Pellentesque efficitur lacus nec tempus molestie. Quisque at pellentesque dolor. Curabitur id diam ac justo commodo pellentesque quis ut quam. Fusce est velit, viverra quis odio sit amet, condimentum fringilla magna. Vivamus non ex ut dui tristique hendrerit eget ac lectus. Fusce tincidunt laoreet nibh, eu mattis dui rhoncus sit amet. Quisque condimentum cursus felis, at tristique orci convallis et.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer efficitur nibh nec justo efficitur interdum. Duis consequat diam sit amet nulla pellentesque ultrices. Pellentesque mattis dapibus eleifend. Aenean dignissim lobortis libero sit amet pretium. Morbi id libero massa. Pellentesque efficitur lacus nec tempus molestie. Quisque at pellentesque dolor. Curabitur id diam ac justo commodo pellentesque quis ut quam. Fusce est velit, viverra quis odio sit amet, condimentum fringilla magna. Vivamus non ex ut dui tristique hendrerit eget ac lectus. Fusce tincidunt laoreet nibh, eu mattis dui rhoncus sit amet. Quisque condimentum cursus felis, at tristique orci convallis et.");
            contentBox.append(clipboardIcon);

}
function backToMainForm() { 

        contentBox.empty();
        updateContentBox("fill");
}
    