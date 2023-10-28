function setupSpeechInput() {
    'use strict';

    // check for support (webkit only)
    if (!('webkitSpeechRecognition' in window)) return;

    var talkMsg = 'Speak now';
    // seconds to wait for more input after last
    var defaultPatienceThreshold = 6;

    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    var inputEls = document.getElementsByClassName('speech-input');

    [].forEach.call(inputEls, function(inputEl) {
        var patience = parseInt(inputEl.dataset.patience, 10) || defaultPatienceThreshold;
        var micBtn, micIcon, holderIcon, newWrapper;
        var shouldCapitalize = true;

        // gather inputEl data
        var nextNode = inputEl.nextSibling;
        var parent = inputEl.parentNode;
        var inputRightBorder = parseInt(getComputedStyle(inputEl).borderRightWidth, 10);
        var buttonSize = 0.8 * (inputEl.dataset.buttonsize || inputEl.offsetHeight);

        // default max size for textareas
        if (!inputEl.dataset.buttonsize && inputEl.tagName === 'TEXTAREA' && buttonSize > 26) {
            buttonSize = 26;
        }

        // create wrapper if not present
        var wrapper = inputEl.parentNode;
        if (!wrapper.classList.contains('si-wrapper')) {
            wrapper = document.createElement('div');
            wrapper.classList.add('si-wrapper');
            wrapper.appendChild(parent.removeChild(inputEl));
            newWrapper = true;
        }

        // create mic button if not present
        micBtn = wrapper.querySelector('.si-btn');
        if (!micBtn) {
            micBtn = document.createElement('button');
            micBtn.type = 'button';
            micBtn.classList.add('si-btn');
            micBtn.textContent = 'speech input';
            micIcon = document.createElement('span');
            holderIcon = document.createElement('span');
            micIcon.classList.add('si-mic');
            holderIcon.classList.add('si-holder');
            micBtn.appendChild(micIcon);
            micBtn.appendChild(holderIcon);
            wrapper.appendChild(micBtn);

            // size and position mic and input
            micBtn.style.cursor = 'pointer';
            micBtn.style.top = 0.125 * buttonSize + 'px';
            micBtn.style.height = micBtn.style.width = buttonSize + 'px';
            inputEl.style.paddingRight = buttonSize - inputRightBorder + 'px';
        }

        // append wrapper where input was
        if (newWrapper) parent.insertBefore(wrapper, nextNode);

        // setup recognition
        var prefix = '';
        var isSentence;
        var recognizing = false;
        var timeout;
        var oldPlaceholder = null;
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        // if lang attribute is set on field use that
        // (defaults to use the lang of the root element)
        if (inputEl.lang) recognition.lang = inputEl.lang;

        function restartTimer() {
            timeout = setTimeout(function() {
                recognition.stop();
            }, patience * 1000);
        }

        recognition.onstart = function() {
            oldPlaceholder = inputEl.placeholder;
            inputEl.placeholder = inputEl.dataset.ready || talkMsg;
            recognizing = true;
            micBtn.classList.add('listening');
            restartTimer();
        };

        recognition.onend = function() {
            recognizing = false;
            clearTimeout(timeout);
            micBtn.classList.remove('listening');
            if (oldPlaceholder !== null) inputEl.placeholder = oldPlaceholder;
        };

        recognition.onresult = function(event) {
            clearTimeout(timeout);

            // get SpeechRecognitionResultList object
            var resultList = event.results;

            // go through each SpeechRecognitionResult object in the list
            var finalTranscript = '';
            var interimTranscript = '';
            for (var i = event.resultIndex; i < resultList.length; ++i) {
                var result = resultList[i];

                // get this result's first SpeechRecognitionAlternative object
                var firstAlternative = result[0];

                if (result.isFinal) {
                    finalTranscript = firstAlternative.transcript;
                } else {
                    interimTranscript += firstAlternative.transcript;
                }
            }

            // capitalize transcript if start of new sentence
            var transcript = finalTranscript || interimTranscript;
            transcript = !prefix || isSentence ? capitalize(transcript) : transcript;

            // append transcript to cached input value
            inputEl.value = prefix + transcript;

            // set cursor and scroll to end
            inputEl.focus();
            if (inputEl.tagName === 'INPUT') {
                inputEl.scrollLeft = inputEl.scrollWidth;
            } else {
                inputEl.scrollTop = inputEl.scrollHeight;
            }

            restartTimer();
        };

        micBtn.addEventListener('click', function(event) {
            event.preventDefault();

            // stop and exit if already going
            if (recognizing) {
                recognition.stop();
                return;
            }

            // Cache current input value which the new transcript will be appended to
            var endsWithWhitespace = inputEl.value.slice(-1).match(/\s/);
            prefix = !inputEl.value || endsWithWhitespace ? inputEl.value : inputEl.value + ' ';

            // check if value ends with a sentence
            isSentence = prefix.trim().slice(-1).match(/[\.\?\!]/);

            // restart recognition
            recognition.start();
        }, false);
    });
}



document.addEventListener("DOMContentLoaded", function() {
    const successorsContainer = document.getElementById("successors");
    const addSuccessorButton = document.getElementById("add-successor");
    const successorCountInput = document.getElementById("successor_count");

    let successorCount = 0;

    function createSuccessorInputs() {
        const successorDiv = document.createElement("div");
        successorDiv.className = "form-row mb-3";

        const nameDiv = document.createElement("div");
        nameDiv.className = "col-md-3";
        const nameInput = document.createElement("input");
        nameInput.type = "text";
        nameInput.name = `name_${successorCount}`;
        nameInput.placeholder = "Nom du successeur";
        nameInput.className = "form-control speech-input";
        nameDiv.appendChild(nameInput);

        const firstNameDiv = document.createElement("div");
        firstNameDiv.className = "col-md-3";
        const firstNameInput = document.createElement("input");
        firstNameInput.type = "text";
        firstNameInput.name = `first_name_${successorCount}`;
        firstNameInput.placeholder = "Prénom du successeur";
        firstNameInput.className = "form-control speech-input";
        firstNameDiv.appendChild(firstNameInput);

        const accessionDateDiv = document.createElement("div");
        accessionDateDiv.className = "col-md-3";
        const accessionDateInput = document.createElement("input");
        accessionDateInput.type = "date";
        accessionDateInput.name = `accessiondate_${successorCount}`;
        accessionDateInput.placeholder = "date d'accession";
        accessionDateInput.className = "form-control";
        accessionDateDiv.appendChild(accessionDateInput);

        const removeButtonDiv = document.createElement("div");
        removeButtonDiv.className = "col-md-3";
        const removeButton = document.createElement("button");
        removeButton.type = "button";
        removeButton.textContent = "-";
        removeButton.className = "btn btn-danger remove-successor";
        removeButtonDiv.appendChild(removeButton);

        successorDiv.appendChild(nameDiv);
        successorDiv.appendChild(firstNameDiv);
        successorDiv.appendChild(accessionDateDiv);
        successorDiv.appendChild(removeButtonDiv);
        successorsContainer.appendChild(successorDiv);

        removeButton.addEventListener("click", function() {
            successorsContainer.removeChild(successorDiv);
            successorCount--; // Mettez à jour le compteur lors de la suppression
            successorCountInput.value = successorCount; // Mettez à jour la valeur du champ caché
        });

        successorCountInput.value = ++successorCount; // Mettez à jour la valeur du champ caché après chaque ajout
        setupSpeechInput();


    }

    // Appeler la fonction pour afficher par défaut les champs pour un successeur
    createSuccessorInputs();

    addSuccessorButton.addEventListener("click", createSuccessorInputs);
});




document.addEventListener("DOMContentLoaded", function() {
    const linesContainer = document.getElementById("lines");
    const addLineButton = document.getElementById("add-line");
    const lineCountInput = document.getElementById("line_count");

    let lineCount = 0;

    function createLineInputs() {
        const lineDiv = document.createElement("div");
        lineDiv.className = "form-row mb-3";

        const nameDiv = document.createElement("div");
        nameDiv.className = "col-md-4";
        const nameInput = document.createElement("input");
        nameInput.type = "text";
        nameInput.name = `lineName_${lineCount}`;
        nameInput.placeholder = "Nom de la lignée";
        nameInput.className = "form-control speech-input";
        nameDiv.appendChild(nameInput);

        const orderDiv = document.createElement("div");
        orderDiv.className = "col-md-4";
        const orderInput = document.createElement("input");
        orderInput.type = "number";
        orderInput.name = `lineOrder_${lineCount}`;
        orderInput.placeholder = "Ordre d'arrivée";
        orderInput.className = "form-control";
        orderDiv.appendChild(orderInput);

        const removeButtonDiv = document.createElement("div");
        removeButtonDiv.className = "col-md-4";
        const removeButton = document.createElement("button");
        removeButton.type = "button";
        removeButton.textContent = "-";
        removeButton.className = "btn btn-danger remove-line";
        removeButtonDiv.appendChild(removeButton);

        lineDiv.appendChild(nameDiv);
        lineDiv.appendChild(orderDiv);
        lineDiv.appendChild(removeButtonDiv);
        linesContainer.appendChild(lineDiv);

        removeButton.addEventListener("click", function() {
            linesContainer.removeChild(lineDiv);
            lineCount--; // Mettez à jour le compteur lors de la suppression
            lineCountInput.value = lineCount; // Mettez à jour la valeur du champ caché
        });

        lineCountInput.value = ++lineCount; // Mettez à jour la valeur du champ caché après chaque ajout
        setupSpeechInput();
    }

    // Appeler la fonction pour afficher par défaut les champs pour une lignée
    createLineInputs();

    addLineButton.addEventListener("click", createLineInputs);
});


document.addEventListener("DOMContentLoaded", function() {
    const campementsContainer = document.getElementById("campements");
    const addCampementButton = document.getElementById("add-campement");
    const campementCountInput = document.getElementById("campement_count");

    let campementCount = 0;

    function createCampementInputs() {
        const campementDiv = document.createElement("div");
        campementDiv.className = "form-row mb-3";

        const campementNameDiv = document.createElement("div");
        campementNameDiv.className = "col-md-3";
        const campementNameInput = document.createElement("input");
        campementNameInput.type = "text";
        campementNameInput.name = `campementName_${campementCount}`;
        campementNameInput.placeholder = "Campement du village";
        campementNameInput.className = "form-control speech-input";
        campementNameDiv.appendChild(campementNameInput);

        const campementPeupleDiv = document.createElement("div");
        campementPeupleDiv.className = "col-md-3";
        const campementPeupleInput = document.createElement("input");
        campementPeupleInput.type = "text";
        campementPeupleInput.name = `campementPeuple_${campementCount}`;
        campementPeupleInput.placeholder = "Peuple";
        campementPeupleInput.className = "form-control speech-input";
        campementPeupleDiv.appendChild(campementPeupleInput);

        const campementOrigineDiv = document.createElement("div");
        campementOrigineDiv.className = "col-md-3";
        const campementOrigineInput = document.createElement("input");
        campementOrigineInput.type = "text";
        campementOrigineInput.name = `campementOrigine_${campementCount}`;
        campementOrigineInput.placeholder = "Origine";
        campementOrigineInput.className = "form-control speech-input";
        campementOrigineDiv.appendChild(campementOrigineInput);

        const removeCampementButtonDiv = document.createElement("div");
        removeCampementButtonDiv.className = "col-md-3";
        const removeCampementButton = document.createElement("button");
        removeCampementButton.type = "button";
        removeCampementButton.textContent = "-";
        removeCampementButton.className = "btn btn-danger remove-campement";
        removeCampementButtonDiv.appendChild(removeCampementButton);

        campementDiv.appendChild(campementNameDiv);
        campementDiv.appendChild(campementPeupleDiv);
        campementDiv.appendChild(campementOrigineDiv);
        campementDiv.appendChild(removeCampementButtonDiv);
        campementsContainer.appendChild(campementDiv);

        removeCampementButton.addEventListener("click", function() {
            campementsContainer.removeChild(campementDiv);
            campementCount--; // Mettez à jour le compteur lors de la suppression
            campementCountInput.value = campementCount; // Mettez à jour la valeur du champ caché
        });

        campementCountInput.value = ++campementCount; // Mettez à jour la valeur du champ caché après chaque ajout
        setupSpeechInput();
    }

    // Appeler la fonction pour afficher par défaut les champs pour un campement
    createCampementInputs();

    addCampementButton.addEventListener("click", createCampementInputs);
});




document.addEventListener("DOMContentLoaded", function() {
            const sitesContainer = document.getElementById("sites");
            const addSiteButton = document.getElementById("add-site");

            let siteCount = 0;

            function createSiteInputs() {
                const siteDiv = document.createElement("div");
                siteDiv.className = "form-row mb-3";

                const siteNameDiv = document.createElement("div");
                siteNameDiv.className = "col-md-3";
                const siteNameInput = document.createElement("input");
                siteNameInput.type = "text";
                siteNameInput.id = `siteName_${siteCount}`;
                siteNameInput.placeholder = "Site d'adoration";
                siteNameInput.className = "form-control speech-input";
                siteNameDiv.appendChild(siteNameInput);

                const localisationDiv = document.createElement("div");
                localisationDiv.className = "col-md-3";
                const localisationInput = document.createElement("input");
                localisationInput.type = "text";
                localisationInput.id = `localisation_${siteCount}`;
                localisationInput.placeholder = "Localisation";
                localisationInput.className = "form-control speech-input";
                localisationDiv.appendChild(localisationInput);

                const removeSiteButtonDiv = document.createElement("div");
                removeSiteButtonDiv.className = "col-md-3";
                const removeSiteButton = document.createElement("button");
                removeSiteButton.type = "button";
                removeSiteButton.textContent = "-";
                removeSiteButton.className = "btn btn-danger remove-successor";
                removeSiteButtonDiv.appendChild(removeSiteButton);

                siteDiv.appendChild(siteNameDiv);
                siteDiv.appendChild(localisationDiv);
                siteDiv.appendChild(removeSiteButtonDiv);
                sitesContainer.appendChild(siteDiv);

                removeSiteButton.addEventListener("click", function() {
                    sitesContainer.removeChild(siteDiv);
                });

                siteCount++;
            setupSpeechInput();
            }

            // Appeler la fonction pour afficher par défaut les champs pour un site d'adoration
            createSiteInputs();


            addSiteButton.addEventListener("click", createSiteInputs);
        });





document.addEventListener("DOMContentLoaded", function() {
            const ancientSitesContainer = document.getElementById("ancient-sites");
            const addAncientSiteButton = document.getElementById("add-ancient-site");

            let ancientSiteCount = 0;

            function createAncientSiteInputs() {
                const ancientSiteDiv = document.createElement("div");
                ancientSiteDiv.className = "form-row mb-3";

                const ancientSiteNameDiv = document.createElement("div");
                ancientSiteNameDiv.className = "col-md-4";
                const ancientSiteNameInput = document.createElement("input");
                ancientSiteNameInput.type = "text";
                ancientSiteNameInput.id = `ancientSiteName_${ancientSiteCount}`;
                ancientSiteNameInput.placeholder = "Ancient Site";
                ancientSiteNameInput.className = "form-control speech-input";
                ancientSiteNameDiv.appendChild(ancientSiteNameInput);

                const ancientSiteMotifDiv = document.createElement("div");
                ancientSiteMotifDiv.className = "col-md-4";
                const ancientSiteMotifInput = document.createElement("input");
                ancientSiteMotifInput.type = "text";
                ancientSiteMotifInput.id = `ancientSiteMotif_${ancientSiteCount}`;
                ancientSiteMotifInput.placeholder = "Motif";
                ancientSiteMotifInput.className = "form-control speech-input";
                ancientSiteMotifDiv.appendChild(ancientSiteMotifInput);

                const removeAncientSiteButtonDiv = document.createElement("div");
                removeAncientSiteButtonDiv.className = "col-md-4";
                const removeAncientSiteButton = document.createElement("button");
                removeAncientSiteButton.type = "button";
                removeAncientSiteButton.textContent = "-";
                removeAncientSiteButton.className = "btn btn-danger remove-successor";
                removeAncientSiteButtonDiv.appendChild(removeAncientSiteButton);

                ancientSiteDiv.appendChild(ancientSiteNameDiv);
                ancientSiteDiv.appendChild(ancientSiteMotifDiv);
                ancientSiteDiv.appendChild(removeAncientSiteButtonDiv);
                ancientSitesContainer.appendChild(ancientSiteDiv);

                removeAncientSiteButton.addEventListener("click", function() {
                    ancientSitesContainer.removeChild(ancientSiteDiv);
                });

                ancientSiteCount++;
            setupSpeechInput();
            }

            // Appeler la fonction pour afficher par défaut les champs pour un ancien site
            createAncientSiteInputs();

            addAncientSiteButton.addEventListener("click", createAncientSiteInputs);
        });




 document.addEventListener("DOMContentLoaded", function() {
            const villagesContainer = document.getElementById("villages");
            const addVillageButton = document.getElementById("add-village");

            let villageCount = 0;

            function createVillageInputs() {
                const villageDiv = document.createElement("div");
                villageDiv.className = "form-row mb-3";

                const villageNameDiv = document.createElement("div");
                villageNameDiv.className = "col-md-9";
                const villageNameInput = document.createElement("input");
                villageNameInput.type = "text";
                villageNameInput.id = `villageName_${villageCount}`;
                villageNameInput.placeholder = "Citer les Villages Regroupés pour Créer ce Village";
                villageNameInput.className = "form-control speech-input";
                villageNameDiv.appendChild(villageNameInput);

                const removeVillageButtonDiv = document.createElement("div");
                removeVillageButtonDiv.className = "col-md-19";
                const removeVillageButton = document.createElement("button");
                removeVillageButton.type = "button";
                removeVillageButton.textContent = "-";
                removeVillageButton.className = "btn btn-danger remove-successor";
                removeVillageButtonDiv.appendChild(removeVillageButton);

                villageDiv.appendChild(villageNameDiv);
                villageDiv.appendChild(removeVillageButtonDiv);
                villagesContainer.appendChild(villageDiv);

                removeVillageButton.addEventListener("click", function() {
                    villagesContainer.removeChild(villageDiv);
                });

                villageCount++;
            setupSpeechInput();
            }

            // Appeler la fonction pour afficher par défaut les champs pour une cité des villages regroupés
            createVillageInputs();

            addVillageButton.addEventListener("click", createVillageInputs);
        });



document.addEventListener("DOMContentLoaded", function() {
            const limite_vilage_litigeContainer = document.getElementById("limite_vilage_litige");
            const addLimite_vilage_litigeButton = document.getElementById("add-limite_vilage_litige");

            let limite_vilage_litigeCount = 0;

            function createLimite_vilage_litigeInputs() {
                const limite_vilage_litigeDiv = document.createElement("div");
                limite_vilage_litigeDiv.className = "form-row mb-3";

                const villageDiv = document.createElement("div");
                villageDiv.className = "col-md-3";
                const villageInput = document.createElement("input");
                villageInput.type = "text";
                villageInput.name = `village_${limite_vilage_litigeCount}`;
                villageInput.placeholder = "Village voisin";
                villageInput.className = "form-control speech-input";
                villageDiv.appendChild(villageInput);

                const limiteDiv = document.createElement("div");
                limiteDiv.className = "col-md-3";
                const limiteInput = document.createElement("input");
                limiteInput.type = "text";
                limiteInput.name = `limite_${limite_vilage_litigeCount}`;
                limiteInput.placeholder = "Limite";
                limiteInput.className = "form-control speech-input";
                limiteDiv.appendChild(limiteInput);

                const zoneLitigeeDiv = document.createElement("div");
                zoneLitigeeDiv.className = "col-md-3";
                const zoneLitigeeInput = document.createElement("input");
                zoneLitigeeInput.type = "text";
                zoneLitigeeInput.name = `zoneLitigee_${limite_vilage_litigeCount}`;
                zoneLitigeeInput.placeholder = "Zone litigée";
                zoneLitigeeInput.className = "form-control speech-input";
                zoneLitigeeDiv.appendChild(zoneLitigeeInput);

                const removeButtonDiv = document.createElement("div");
                removeButtonDiv.className = "col-md-3";
                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.textContent = "-";
                removeButton.className = "btn btn-danger remove-successor";
                removeButtonDiv.appendChild(removeButton);

                limite_vilage_litigeDiv.appendChild(villageDiv);
                limite_vilage_litigeDiv.appendChild(limiteDiv);
                limite_vilage_litigeDiv.appendChild(zoneLitigeeDiv);
                limite_vilage_litigeDiv.appendChild(removeButtonDiv);
                limite_vilage_litigeContainer.appendChild(limite_vilage_litigeDiv);

                removeButton.addEventListener("click", function() {
                    limite_vilage_litigeContainer.removeChild(limite_vilage_litigeDiv);
                });

                limite_vilage_litigeCount++;
            setupSpeechInput();
            }

            // Appeler la fonction pour afficher par défaut les champs pour une limite, un village en litige
            createLimite_vilage_litigeInputs();

            addLimite_vilage_litigeButton.addEventListener("click", createLimite_vilage_litigeInputs);
        });