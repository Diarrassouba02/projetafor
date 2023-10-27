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
