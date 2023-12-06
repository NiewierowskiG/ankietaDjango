function addRandomColor() {
    let inputs = document.getElementsByName("ulubiony_kolor");
    const colors = ["czerwony", "niebieski", "zielony"];
    inputs.forEach((ulubiony_kolor) => {
        ulubiony_kolor.value = colors[Math.floor(Math.random()*colors.length)];
    });

}