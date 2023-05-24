function saveForms() {
    // Get all the forms on the page
    var forms = document.querySelectorAll("form");
    // Iterate through the forms and submit them
    for (var i = 0; i < forms.length; i++) {
      forms[i].submit();
    }
  }