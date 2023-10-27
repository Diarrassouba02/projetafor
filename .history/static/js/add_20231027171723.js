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
                firstNameInput.name = `firstName_${successorCount}`;
                firstNameInput.placeholder = "Prénom du successeur";
                firstNameInput.className = "form-control speech-input";
                firstNameDiv.appendChild(firstNameInput);

                const accessionDateDiv = document.createElement("div");
                accessionDateDiv.className = "col-md-3";
                const accessionDateInput = document.createElement("input");
                accessionDateInput.type = "date";
                accessionDateInput.name = `accessionDate_${successorCount}`;
                accessionDateDiv.placeholder = "date d'accession";
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
                });

                successorCount++;
                setupSpeechInput()
            }

            // Appeler la fonction pour afficher par défaut les champs pour un successeur
            createSuccessorInputs();

            addSuccessorButton.addEventListener("click", createSuccessorInputs);
        });




 document.addEventListener("DOMContentLoaded", function() {
            const linesContainer = document.getElementById("lines");
            const addLineButton = document.getElementById("add-line");

            let lineCount = 0;

            function createLineInputs() {
                const lineDiv = document.createElement("div");
                lineDiv.className = "form-row mb-3";

                const nameDiv = document.createElement("div");
                nameDiv.className = "col-md-4"; // Utilisez une colonne de longueur 4
                const nameInput = document.createElement("input");
                nameInput.type = "text";
                nameInput.name = `lineName_${lineCount}`;
                nameInput.placeholder = "Nom de la lignée";
                nameInput.className = "form-control speech-input";
                nameDiv.appendChild(nameInput);

                const orderDiv = document.createElement("div");
                orderDiv.className = "col-md-4"; // Utilisez une colonne de longueur 4
                const orderInput = document.createElement("input");
                orderInput.type = "number";
                orderInput.name = `lineOrder_${lineCount}`;
                orderInput.placeholder = "Ordre d'arrivée";
                orderInput.className = "form-control";
                orderDiv.appendChild(orderInput);

                const removeButtonDiv = document.createElement("div");
                removeButtonDiv.className = "col-md-4"; // Utilisez une colonne de longueur 4
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
                });

                lineCount++;
                setupSpeechInput();
            }

            // Appeler la fonction pour afficher par défaut les champs pour une lignée
            createLineInputs();

            addLineButton.addEventListener("click", createLineInputs);
        });






document.addEventListener("DOMContentLoaded", function() {
            const campementsContainer = document.getElementById("campements");
            const addCampementButton = document.getElementById("add-campement");

            let campementCount = 0;

            function createCampementInputs() {
                const campementDiv = document.createElement("div");
                campementDiv.className = "form-row mb-3";

                const campementNameDiv = document.createElement("div");
                campementNameDiv.className = "col-md-3";
                const campementNameInput = document.createElement("input");
                campementNameInput.type = "text";
                campementNameInput.id = `campementName_${campementCount}`;
                campementNameInput.placeholder = "Campement du village";
                campementNameInput.className = "form-control speech-input";
                campementNameDiv.appendChild(campementNameInput);

                const campementPeupleDiv = document.createElement("div");
                campementPeupleDiv.className = "col-md-3";
                const campementPeupleInput = document.createElement("input");
                campementPeupleInput.type = "text";
                campementPeupleInput.id = `campementPeuple_${campementCount}`;
                campementPeupleInput.placeholder = "Peuple";
                campementPeupleInput.className = "form-control speech-input";
                campementPeupleDiv.appendChild(campementPeupleInput);

                const campementOrigineDiv = document.createElement("div");
                campementOrigineDiv.className = "col-md-3";
                const campementOrigineInput = document.createElement("input");
                campementOrigineInput.type = "text";
                campementOrigineInput.id = `campementOrigine_${campementCount}`;
                campementOrigineInput.placeholder = "Origine";
                campementOrigineInput.className = "form-control speech-input";
                campementOrigineDiv.appendChild(campementOrigineInput);

                const removeCampementButtonDiv = document.createElement("div");
                removeCampementButtonDiv.className = "col-md-3";
                const removeCampementButton = document.createElement("button");
                removeCampementButton.type = "button";
                removeCampementButton.textContent = "-";
                removeCampementButton.className = "btn btn-danger remove-successor";
                removeCampementButtonDiv.appendChild(removeCampementButton);

                campementDiv.appendChild(campementNameDiv);
                campementDiv.appendChild(campementPeupleDiv);
                campementDiv.appendChild(campementOrigineDiv);
                campementDiv.appendChild(removeCampementButtonDiv);
                campementsContainer.appendChild(campementDiv);

                removeCampementButton.addEventListener("click", function() {
                    campementsContainer.removeChild(campementDiv);
                });

                campementCount++;
            }

            // Appeler la fonction pour afficher par défaut les champs pour un campement
            createCampementInputs();
            setupSpeechInput();

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
            }

            // Appeler la fonction pour afficher par défaut les champs pour un site d'adoration
            createSiteInputs();
            setupSpeechInput();

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
                ancientSiteNameDiv.className = "col-md-3";
                const ancientSiteNameInput = document.createElement("input");
                ancientSiteNameInput.type = "text";
                ancientSiteNameInput.id = `ancientSiteName_${ancientSiteCount}`;
                ancientSiteNameInput.placeholder = "Ancient Site";
                ancientSiteNameInput.className = "form-control";
                ancientSiteNameDiv.appendChild(ancientSiteNameInput);

                const ancientSiteMotifDiv = document.createElement("div");
                ancientSiteMotifDiv.className = "col-md-3";
                const ancientSiteMotifInput = document.createElement("input");
                ancientSiteMotifInput.type = "text";
                ancientSiteMotifInput.id = `ancientSiteMotif_${ancientSiteCount}`;
                ancientSiteMotifInput.placeholder = "Motif";
                ancientSiteMotifInput.className = "form-control";
                ancientSiteMotifDiv.appendChild(ancientSiteMotifInput);

                const removeAncientSiteButtonDiv = document.createElement("div");
                removeAncientSiteButtonDiv.className = "col-md-3";
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
            }

            // Appeler la fonction pour afficher par défaut les champs pour un ancien site
            createAncientSiteInputs();

            addAncientSiteButton.addEventListener("click", createAncientSiteInputs);
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
                nomInput.className = "groupement-input speech-input form-control";
                nomInput.setAttribute('placeholder', 'Parlez maintenant');

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