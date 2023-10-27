document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const successorsContainer = document.getElementById("successors");
            const addSuccessorButton = document.getElementById("add-successor");
            const successorCountInput = document.getElementById("successor_count");

            let successorCount = 0;

            function createSuccessorInputs() {
                const successorDiv = document.createElement("div");
                successorDiv.className = "successor";

                const nameLabel = document.createElement("label");
                nameLabel.className = "successor-label";
                nameLabel.textContent = "Nom du successeur";

                const nameInput = document.createElement("input");
                nameInput.type = "text";
                nameInput.name = `name_${successorCount}`;
                nameInput.className = "successor-input";

                const firstNameLabel = document.createElement("label");
                firstNameLabel.className = "successor-label";
                firstNameLabel.textContent = "Prénom du successeur";

                const firstNameInput = document.createElement("input");
                firstNameInput.type = "text";
                firstNameInput.name = `first_name_${successorCount}`;
                firstNameInput.className = "successor-input";

                const accessionDateLabel = document.createElement("label");
                accessionDateLabel.className = "successor-label";
                accessionDateLabel.textContent = "Date d'accession";

                const accessionDateInput = document.createElement("input");
                accessionDateInput.type = "date";
                accessionDateInput.name = `accession_date_${successorCount}`;
                accessionDateInput.className = "successor-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-successor";

                successorDiv.appendChild(nameLabel);
                successorDiv.appendChild(nameInput);
                successorDiv.appendChild(firstNameLabel);
                successorDiv.appendChild(firstNameInput);
                successorDiv.appendChild(accessionDateLabel);
                successorDiv.appendChild(accessionDateInput);
                successorDiv.appendChild(removeButton);
                successorsContainer.appendChild(successorDiv);

                removeButton.addEventListener("click", function() {
                    successorsContainer.removeChild(successorDiv);
                    successorCount--;
                    updateSuccessorCount();
                });

                successorCount++;
                updateSuccessorCount();
            }

            function updateSuccessorCount() {
                successorCountInput.value = successorCount;
            }

            // Appeler la fonction pour afficher un champ pour un successeur par défaut
            createSuccessorInputs();

            addSuccessorButton.addEventListener("click", createSuccessorInputs);
        });





document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const lignagesContainer = document.getElementById("lignages");
            const addLignageButton = document.getElementById("add-lignage");
            const lignageCountInput = document.getElementById("lignage_count");

            let lignageCount = 0;

            function createLignageInputs() {
                const lignageDiv = document.createElement("div");
                lignageDiv.className = "lignage";

                const ordreLabel = document.createElement("label");
                ordreLabel.className = "lignage-label";
                ordreLabel.textContent = "Ordre du lignage";

                const ordreInput = document.createElement("input");
                ordreInput.type = "text";
                ordreInput.name = `ordre_${lignageCount}`;
                ordreInput.className = "lignage-input";

                const nomLabel = document.createElement("label");
                nomLabel.className = "lignage-label";
                nomLabel.textContent = "Nom du lignage";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `nom_${lignageCount}`;
                nomInput.className = "lignage-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-lignage";

                lignageDiv.appendChild(ordreLabel);
                lignageDiv.appendChild(ordreInput);
                lignageDiv.appendChild(nomLabel);
                lignageDiv.appendChild(nomInput);
                lignageDiv.appendChild(removeButton);
                lignagesContainer.appendChild(lignageDiv);

                removeButton.addEventListener("click", function() {
                    lignagesContainer.removeChild(lignageDiv);
                    lignageCount--;
                    updateLignageCount();
                });

                lignageCount++;
                updateLignageCount();
            }

            function updateLignageCount() {
                lignageCountInput.value = lignageCount;
            }

            // Appeler la fonction pour afficher un champ pour un lignage par défaut
            createLignageInputs();

            addLignageButton.addEventListener("click", createLignageInputs);
        });





document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const campementsContainer = document.getElementById("campements");
            const addCampementButton = document.getElementById("add-campement");
            const campementCountInput = document.getElementById("campement_count");

            let campementCount = 0;

            function createCampementInputs() {
                const campementDiv = document.createElement("div");
                campementDiv.className = "campement";

                const nomLabel = document.createElement("label");
                nomLabel.className = "campement-label";
                nomLabel.textContent = "Nom du campement";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `nom_${campementCount}`;
                nomInput.className = "campement-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-campement";

                campementDiv.appendChild(nomLabel);
                campementDiv.appendChild(nomInput);
                campementDiv.appendChild(removeButton);
                campementsContainer.appendChild(campementDiv);

                removeButton.addEventListener("click", function() {
                    campementsContainer.removeChild(campementDiv);
                    campementCount--;
                    updateCampementCount();
                });

                campementCount++;
                updateCampementCount();
            }

            function updateCampementCount() {
                campementCountInput.value = campementCount;
            }

            // Appeler la fonction pour afficher un champ pour un campement par défaut
            createCampementInputs();

            addCampementButton.addEventListener("click", createCampementInputs);
        });






        document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const sudsContainer = document.getElementById("suds");
            const addSudButton = document.getElementById("add-sud");
            const sudCountInput = document.getElementById("sud_count");

            let sudCount = 0;

            function createSudInputs() {
                const sudDiv = document.createElement("div");
                sudDiv.className = "sud";

                const nomLabel = document.createElement("label");
                nomLabel.className = "sud-label";
                nomLabel.textContent = "Sud";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `sud_${sudCount}`;
                nomInput.className = "sud-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-sud";

                sudDiv.appendChild(nomLabel);
                sudDiv.appendChild(nomInput);
                sudDiv.appendChild(removeButton);
                sudsContainer.appendChild(sudDiv);

                removeButton.addEventListener("click", function() {
                    sudsContainer.removeChild(sudDiv);
                    sudCount--;
                    updateSudCount();
                });

                sudCount++;
                updateSudCount();
            }

            function updateSudCount() {
                sudCountInput.value = sudCount;
            }

            // Appeler la fonction pour afficher un champ pour un sud par défaut
            createSudInputs();

            addSudButton.addEventListener("click", createSudInputs);
        });





document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const nordsContainer = document.getElementById("nords");
            const addNordButton = document.getElementById("add-nord");
            const nordCountInput = document.getElementById("nord_count");

            let nordCount = 0;

            function createNordInputs() {
                const nordDiv = document.createElement("div");
                nordDiv.className = "nord";

                const nomLabel = document.createElement("label");
                nomLabel.className = "nord-label";
                nomLabel.textContent = "Nord";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `nord_${nordCount}`;
                nomInput.className = "nord-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-nord";

                nordDiv.appendChild(nomLabel);
                nordDiv.appendChild(nomInput);
                nordDiv.appendChild(removeButton);
                nordsContainer.appendChild(nordDiv);

                removeButton.addEventListener("click", function() {
                    nordsContainer.removeChild(nordDiv);
                    nordCount--;
                    updateNordCount();
                });

                nordCount++;
                updateNordCount();
            }

            function updateNordCount() {
                nordCountInput.value = nordCount;
            }

            // Appeler la fonction pour afficher un champ pour un nord par défaut
            createNordInputs();

            addNordButton.addEventListener("click", createNordInputs);
        });



document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const ouestsContainer = document.getElementById("ouests");
            const addOuestButton = document.getElementById("add-ouest");
            const ouestCountInput = document.getElementById("ouest_count");

            let ouestCount = 0;

            function createOuestInputs() {
                const ouestDiv = document.createElement("div");
                ouestDiv.className = "ouest";

                const nomLabel = document.createElement("label");
                nomLabel.className = "ouest-label";
                nomLabel.textContent = "Ouest";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `ouest_${ouestCount}`;
                nomInput.className = "ouest-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-ouest";

                ouestDiv.appendChild(nomLabel);
                ouestDiv.appendChild(nomInput);
                ouestDiv.appendChild(removeButton);
                ouestsContainer.appendChild(ouestDiv);

                removeButton.addEventListener("click", function() {
                    ouestsContainer.removeChild(ouestDiv);
                    ouestCount--;
                    updateOuestCount();
                });

                ouestCount++;
                updateOuestCount();
            }

            function updateOuestCount() {
                ouestCountInput.value = ouestCount;
            }

            // Appeler la fonction pour afficher un champ pour un ouest par défaut
            createOuestInputs();

            addOuestButton.addEventListener("click", createOuestInputs);
        });