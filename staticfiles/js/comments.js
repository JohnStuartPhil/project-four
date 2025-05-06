const editButtons = document.getElementsByClassName("btn-edit");
const opinionText = document.getElementById("id_your_opinion");
const opinionForm = document.getElementById("opinionForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let opinionId = e.target.getAttribute("comment_id");
    let opinionContent = document.getElementById(`comment${opinionId}`).innerText;
    opinionText.value = opinionContent;
    submitButton.innerText = "Update";
    opinionForm.setAttribute("action", `edit_opinion/${opinionId}`);
  });
}