// Use google places api to have searchbox autocomplete with google places
function activatePlacesSearch() {
    var input = document.getElementById('places_auto');
    var autocomplete = new google.maps.places.Autocomplete(input);
}

// Function to expand/collapse extra place details
function showHideDetails() {
    var advanced = document.getElementById("advanced");
    if (advanced.style.display == "none") {
        advanced.style.display = "block";
    }
    else {
        advanced.style.display = "none";
    }
}

// https://stackoverflow.com/questions/133925/javascript-post-request-like-a-form-submit
function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}

// Call map initialization and active google places api autocomplete
function init() {
    initMap(activatePlacesSearch);
}