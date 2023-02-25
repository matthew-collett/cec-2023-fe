document.addEventListener("click", e => {
    const isDropdownButton = e.target.matches(".dropdown-button")
    if (!isDropdownButton && e.target.closest(".dropdown") != null) return

    let currentDropdown
    if (isDropdownButton) {
        currentDropdown = e.target.closest(".dropdown")
        currentDropdown.classList.toggle("active")
    }

    document.querySelectorAll(".dropdown.active").forEach(dropdown => {
        if (dropdown === currentDropdown) return
        dropdown.classList.remove("active")
    })
})