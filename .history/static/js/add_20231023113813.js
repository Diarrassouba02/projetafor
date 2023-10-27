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

                nameInput.setAttribute('placeholder', 'Parlez maintenant');
                nameInput.type = "text";
                nameInput.name = `name_${successorCount}`;
                nameInput.className = "successor-input speech-input";

                const firstNameLabel = document.createElement("label");
                firstNameLabel.className = "successor-label";
                firstNameLabel.textContent = "Prénom du successeur";

                const firstNameInput = document.createElement("input");
                firstNameInput.type = "text";
                firstNameInput.name = `first_name_${successorCount}`;
                firstNameInput.className = "speech-input";

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
                ordreInput.classList.add("speech-input");
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
                campementDiv.classList.add("form-control","col-md-6")
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




        document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const estsContainer = document.getElementById("ests");
            const addEstButton = document.getElementById("add-est");
            const estCountInput = document.getElementById("est_count");

            let estCount = 0;

            function createEstInputs() {
                const estDiv = document.createElement("div");
                estDiv.className = "est";

                const nomLabel = document.createElement("label");
                nomLabel.className = "est-label";
                nomLabel.textContent = "Est";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `est_${estCount}`;
                nomInput.className = "est-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-est";

                estDiv.appendChild(nomLabel);
                estDiv.appendChild(nomInput);
                estDiv.appendChild(removeButton);
                estsContainer.appendChild(estDiv);

                removeButton.addEventListener("click", function() {
                    estsContainer.removeChild(estDiv);
                    estCount--;
                    updateEstCount();
                });

                estCount++;
                updateEstCount();
            }

            function updateEstCount() {
                estCountInput.value = estCount;
            }

            // Appeler la fonction pour afficher un champ pour un est par défaut
            createEstInputs();

            addEstButton.addEventListener("click", createEstInputs);
        });



document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const centresContainer = document.getElementById("centres");
            const addCentreButton = document.getElementById("add-centre");
            const centreCountInput = document.getElementById("centre_count");

            let centreCount = 0;

            function createCentreInputs() {
                const centreDiv = document.createElement("div");
                centreDiv.className = "centre";

                const nomLabel = document.createElement("label");
                nomLabel.className = "centre-label";
                nomLabel.textContent = "Centre";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `centre_${centreCount}`;
                nomInput.className = "centre-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-centre";

                centreDiv.appendChild(nomLabel);
                centreDiv.appendChild(nomInput);
                centreDiv.appendChild(removeButton);
                centresContainer.appendChild(centreDiv);

                removeButton.addEventListener("click", function() {
                    centresContainer.removeChild(centreDiv);
                    centreCount--;
                    updateCentreCount();
                });

                centreCount++;
                updateCentreCount();
            }

            function updateCentreCount() {
                centreCountInput.value = centreCount;
            }

            // Appeler la fonction pour afficher un champ pour un centre par défaut
            createCentreInputs();

            addCentreButton.addEventListener("click", createCentreInputs);
        });





 document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const anciensSitesContainer = document.getElementById("anciens-sites");
            const addAncienSiteButton = document.getElementById("add-ancien-site");
            const ancienSiteCountInput = document.getElementById("ancien_site_count");

            let ancienSiteCount = 0;

            function createAncienSiteInputs() {
                const ancienSiteDiv = document.createElement("div");
                ancienSiteDiv.className = "ancien-site";

                const nomLabel = document.createElement("label");
                nomLabel.className = "ancien-site-label";
                nomLabel.textContent = "Ancien Site";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `ancien_site_${ancienSiteCount}`;
                nomInput.className = "ancien-site-input";

                const motifLabel = document.createElement("label");
                motifLabel.className = "ancien-site-label";
                motifLabel.textContent = "Motif";

                const motifInput = document.createElement("input");
                motifInput.type = "text";
                motifInput.name = `motif_${ancienSiteCount}`;
                motifInput.className = "ancien-site-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-ancien-site";

                ancienSiteDiv.appendChild(nomLabel);
                ancienSiteDiv.appendChild(nomInput);
                ancienSiteDiv.appendChild(motifLabel);
                ancienSiteDiv.appendChild(motifInput);
                ancienSiteDiv.appendChild(removeButton);
                anciensSitesContainer.appendChild(ancienSiteDiv);

                removeButton.addEventListener("click", function() {
                    anciensSitesContainer.removeChild(ancienSiteDiv);
                    ancienSiteCount--;
                    updateAncienSiteCount();
                });

                ancienSiteCount++;
                updateAncienSiteCount();
            }

            function updateAncienSiteCount() {
                ancienSiteCountInput.value = ancienSiteCount;
            }

            // Appeler la fonction pour afficher un champ pour un ancien site par défaut
            createAncienSiteInputs();

            addAncienSiteButton.addEventListener("click", createAncienSiteInputs);
        });





document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const groupementsContainer = document.getElementById("groupements");
            const addGroupementButton = document.getElementById("add-groupement");
            const groupementCountInput = document.getElementById("groupement_count");

            let groupementCount = 0;

            function createGroupementInputs() {
                const groupementDiv = document.createElement("div");
                groupementDiv.className = "groupement";

                const nomLabel = document.createElement("label");
                nomLabel.className = "groupement-label";
                nomLabel.textContent = "Groupement";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `groupement_${groupementCount}`;
                nomInput.className = "groupement-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-groupement";

                groupementDiv.appendChild(nomLabel);
                groupementDiv.appendChild(nomInput);
                groupementDiv.appendChild(removeButton);
                groupementsContainer.appendChild(groupementDiv);

                removeButton.addEventListener("click", function() {
                    groupementsContainer.removeChild(groupementDiv);
                    groupementCount--;
                    updateGroupementCount();
                });

                groupementCount++;
                updateGroupementCount();
            }

            function updateGroupementCount() {
                groupementCountInput.value = groupementCount;
            }

            // Appeler la fonction pour afficher un champ pour un groupement par défaut
            createGroupementInputs();

            addGroupementButton.addEventListener("click", createGroupementInputs);
        });




        document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const villageVoisinsContainer = document.getElementById("village-voisins");
            const addVillageVoisinButton = document.getElementById("add-village-voisin");
            const villageVoisinCountInput = document.getElementById("village_voisin_count");

            let villageVoisinCount = 0;

            function createVillageVoisinInputs() {
                const villageVoisinDiv = document.createElement("div");
                villageVoisinDiv.className = "village-voisin";

                const nomLabel = document.createElement("label");
                nomLabel.className = "village-voisin-label";
                nomLabel.textContent = "Village Voisin";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `village_voisin_${villageVoisinCount}`;
                nomInput.className = "village-voisin-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-village-voisin";

                villageVoisinDiv.appendChild(nomLabel);
                villageVoisinDiv.appendChild(nomInput);
                villageVoisinDiv.appendChild(removeButton);
                villageVoisinsContainer.appendChild(villageVoisinDiv);

                removeButton.addEventListener("click", function() {
                    villageVoisinsContainer.removeChild(villageVoisinDiv);
                    villageVoisinCount--;
                    updateVillageVoisinCount();
                });

                villageVoisinCount++;
                updateVillageVoisinCount();
            }

            function updateVillageVoisinCount() {
                villageVoisinCountInput.value = villageVoisinCount;
            }

            // Appeler la fonction pour afficher un champ pour un village voisin par défaut
            createVillageVoisinInputs();

            addVillageVoisinButton.addEventListener("click", createVillageVoisinInputs);
        });



document.addEventListener("DOMContentLoaded", function() {
            const form = document.querySelector("form");
            const villagesContainer = document.getElementById("villages");
            const addVillageButton = document.getElementById("add-village");
            const villageCountInput = document.getElementById("village_count");

            let villageCount = 0;

            function createVillageInputs() {
                const villageDiv = document.createElement("div");
                villageDiv.className = "village";

                const nomLabel = document.createElement("label");
                nomLabel.className = "village-label";
                nomLabel.textContent = "Village";

                const nomInput = document.createElement("input");
                nomInput.type = "text";
                nomInput.name = `village_${villageCount}`;
                nomInput.className = "village-input";

                const limiteLabel = document.createElement("label");
                limiteLabel.className = "village-label";
                limiteLabel.textContent = "Limite";

                const limiteInput = document.createElement("input");
                limiteInput.type = "text";
                limiteInput.name = `limite_${villageCount}`;
                limiteInput.className = "village-input";

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "remove-village";

                villageDiv.appendChild(nomLabel);
                villageDiv.appendChild(nomInput);
                villageDiv.appendChild(limiteLabel);
                villageDiv.appendChild(limiteInput);
                villageDiv.appendChild(removeButton);
                villagesContainer.appendChild(villageDiv);

                removeButton.addEventListener("click", function() {
                    villagesContainer.removeChild(villageDiv);
                    villageCount--;
                    updateVillageCount();
                });

                villageCount++;
                updateVillageCount();
            }

            function updateVillageCount() {
                villageCountInput.value = villageCount;
            }

            // Appeler la fonction pour afficher un champ pour un village par défaut
            createVillageInputs();

            addVillageButton.addEventListener("click", createVillageInputs);
        });