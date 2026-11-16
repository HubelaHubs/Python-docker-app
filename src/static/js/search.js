document.addEventListener("DOMContentLoaded", () => {

    const searchInput = document.getElementById("tableSearch");
    const resultCount = document.getElementById("resultCount");

    const rows = document.querySelectorAll("tbody tr");

    resultCount.textContent = `${rows.length} Results`;

    searchInput.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        let visibleRows = 0;

        rows.forEach(row => {

            const text = row.textContent.toLowerCase();

            if (text.includes(filter)) {
                row.style.display = "";
                visibleRows++;
            } else {
                row.style.display = "none";
            }

        });

        resultCount.textContent =
            `${visibleRows} Results`;

    });

});
