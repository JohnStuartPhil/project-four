const editButtons = document.getElementsByClassName("btn-edit");
const opinionText = document.getElementById("id_your_opinion");
const opinionForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated opinion's ID upon click.
* - Fetches the content of the corresponding opinion.
* - Populates the `opinionText` input/textarea with the opinion's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_opinion/{opinionId}` endpoint.
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

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated opinion's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific opinion.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let opinionId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_opinion/${opinionId}`;
    deleteModal.show();
  });
}