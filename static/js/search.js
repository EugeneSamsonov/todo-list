var search = document.getElementById("search-input");

search.addEventListener("input", () => {
    let value = search.value;
    // list.innerHTML = render(USERS.filter((user) => {
    //     return user.name.toLowerCase().includes(value.toLowerCase())
    // }))
    console.log(value);
})