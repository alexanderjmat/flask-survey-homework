input = document.querySelector("body")
form = document.querySelector("form")

input.addEventListener("click", function(e) {
    if (e.target.type == "radio") {
        form.submit()

    }
})