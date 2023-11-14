/*global webkitSpeechRecognition */
(function() {
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

			// If the <input> has data-instant-submit and a value,
			if (inputEl.dataset.instantSubmit !== undefined && inputEl.value) {
				// submit the form it's in (if it is in one).
				if (inputEl.form) inputEl.form.submit();
			}
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

			// set cursur and scroll to end
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
})();






        var paysSelect = document.getElementById("pays");
        var villeSelect = document.getElementById("departement");
        var quartierSelect = document.getElementById("quartier");
        var citerSelect = document.getElementById("citer");

        var villesParPays = {
            abidjan: {
                abidjan: ["Abobo", "Adjame", "Attecoube ","Cocody ","Plateau","Yopougon",
                          "Koumassi","Marcory","Port-Bouet","Treichville","Bingerville",
                           "Brofodoumé","Anyama","Songon"],
            },
            tiassa: {
                Agboville: ["Aboude", "Ananguie ", "Agboville","Attobrou","Azaguié",
                           "Céchi","Grand-Morié","Guessiguié","Loviguié","Oress-Krobou","Rubino"],
                Sikensi: ["Gomon","Sikensi"],
                Taabo : ["Taabo", "Pacobo"],
                Tiassalé:["Gbolouville","Morokro","N’Douci","Tiassalé"],
                Grand_Lahou :["Ahouanou","Bacanda","Ebounou ","Grand-Lahou ","Toukouzou"],
                Jacqueville:["Attoutou ","Jacqueville"]
            },
            bafing: {
                Koro : ["Koro", "Booko", "Borotou","Mahandougou","Niokosso "],
                Ouaninou: ["Gbelo", "Gouekan", "Ouaninou","Koonan ","Saboudougou","Santa"],
                Touba: ["Dioman", "Foungbesso","Guintéguéla", "Touba"],
                Kounahiri :["Kongasso","Kounahiri"],
                Mankono:["Bouandougou","Mankono","Marandalah","Sarhala","Tiéningboué"]
            },


           bagoue:{
                Boundiali: ["Baya", "Boundiali", "Ganaoni","Kasséré","Siempurgo"],
                Kouto: ["Blességué", "Gbon", "Kolia","Kouto","Sianhala"],
                Tengréla: ["Débété", "Kanakono","Papara", "Tengréla "],
                Bengué :["Bougou","Katiala","Katogo","M'Bengué" ],
                Sinématiali :["Bouakaha","Kagbolodougou","Sediego","Sinématiali"]
            },


            belier:{
                   Didiévi:["Bollo","Didiévi","Molonou-Blé","Raviart","Tié-N'Diékro"],
                   Djékanou:["Bonikro","","Djékanou"],
                   Tiébissou:["Yakpabo-Sakassou","Tiébissou","Molonou","Tiébissou","Yakpabo-Sakassou"],
                   Toumodi:["Angoda","Kokoumbo","Kpouébo","Toumodi"],
                    Prikro:["Anianou","Famienkro ","Koffi-Amonkro","Nafana","Prikro "]
            },



             bere:{
                Dianra: ["Dianra", "Dianra-Village"]
                  },




           boukani:{
                Bouna: ["Bouka ", "Bouna", "Ondefidouo","Youndouo "],
                Doropo: ["Danoa", "Doropo", "Kalamon","Niamoue"],
                Nassian: ["Bogofa", "Kakpin" ,"Kotouba ","Nassian", "Sominassé"],
                Téhini:["Gogo","Téhini","Tougbo" ],
                Bondoukou:["Appimandou","Pinda-Boroko","Bondo","Bondoukou","Gouméré "
                           ,"Laoud-Iba","Sapli-Sépingo","Sorobango","Tabagne","Tagadi","Taoudi","Yezimala"],
                Koun_Fao :["Boahia","Kokomian","Kouassi-Dattékro","Koun-Fao ","Tankéssé ","Tienkoikro"],
                Sandégué:["Bandakagni-Tomora","Dimandougou","Sandégué","Yorobodi"]
            },





           cavally:{
                Bloléquin: ["Bloléquin", "Diboké", "Doké","Tinhou","Zéaglo"],
                Guiglo: ["Bedy-Goazon ", "Guiglo", "Kaade","Nizahon"],
                Taï: ["Taï", "Zagne"],
                Toulépleu:["Bakoubly","Meo","Nezobly","Péhé","Tiobly","Toulépleu"],
                Kouibly:["Kouibly","Nidrou","Ouyably-Gnondrou","Totrodrou"],

            },


        folon:{
                Kaniasso:["Goulia", "Kaniasso", "Mahandiana-Sokourani"],
                Minignan:["Kimbirila-Nord", "Minignan", "Sokoro","Tienko"],
                Madinani:["Fengolo","Madinani ","N'Goloblasso"],
                Odienné:["Bako","Bougousso ","Dioulatièdougou","Odienné","Tiémé"],
                Samatiguila:["Kimbirila-Sud","Samatiguila"],
                Séguélon:["Séguélon","Gbongaha"]


            },

        Séguélon:{
                Kaniasso:["Goulia", "Kaniasso", "Mahandiana-Sokourani"],
                Minignan:["Kimbirila-Nord", "Minignan", "Sokoro","Tienko"],
                Madinani:["Fengolo","Madinani ","N'Goloblasso"],
                Odienné:["Bako","Bougousso ","Dioulatièdougou","Odienné","Tiémé"],
                Samatiguila:["Kimbirila-Sud","Samatiguila"],



            },

        gbeke:{
                Béoumi:["Ando-Kékrénou","Béoumi ", "Bodokro", "Kondrobo","Lolobo","Marabadiassa","N'Guessankro"],
                Botro:["Botro", "Diabo", "Krofoinsou","Languibonou"],
                Bouaké:["Bouaké-Ville","Bouaké-SP","Bounda","Brobo","Djébonoua","Mamini"],
                Sakassou:["Ayaou-Sran","Dibri-Assirikro","Sakassou","Toumodi-Sakassou"],


             },



        gbokle:{
                Fresco:["Dahiri","Fresco", "Gbagbam", "Kondrobo","Lolobo","Marabadiassa","N'Guessankro"],
                Sassandra:["Dakpadou","Grihiri","Lobakuya", "Medon", "Sago","Sassandra"],
                Méagui:["Gnamangui","Méagui","Oupoyo"],
                Soubré:["Grand-Zattry ","Liliyo","Okrouyo","Soubré"],

             },




        goh:{
                Gagnoa:["Bayota","Dahiepa-Kehi", "Dignago", "Dougroupalegnaoa","Doukouyo","Gagnoa",
                "Galebre-Galébouo","Gnagbodougnoa","Guibéroua","Ouragahio","Sérihio","Yopohue"],
                Oumé:["Diégonéfla","Guépahouo ","Oumé", "Tonla"]


             },




        gontougo:{
                Bondoukou:["Appimandou","Pinda-Boroko", "Bondo", "Bondoukou","Gouméré"
                ,"Laoud-Iba ","Sapli-Sépingo","Sorobango","Tabagne","Tagadi","Taoudi ","Yezimala"],
                Koun_Fao :["Boahia","Kokomian","Kouassi-Dattékro", "Koun-Fao", "Tankéssé","Tienkoikro"],
                Sandégué:["Bandakagni-Tomora","Dimandougou","Sandégué","Yorobodi"],
                Tanda:["Amanvi","Diamba","Tanda","Tchedio"],
                Transua:["Assuéfry","Kouassi-Niaguini","Transua"]

             },




        };



        var citésParQuartier = {
        // Ajoutez les quartiers et leurs cités correspondantes ici
        abobo: ["cité1", "cité2", "cité3"],
        quartier2: ["cité4", "cité5", "cité6"],
        };


        function mettreAJourVilles() {
            var paysSelectionne = paysSelect.value;

            villeSelect.innerHTML = "<option value=''>Sélectionnez un Département</option>";
            quartierSelect.innerHTML = "<option value=''>Sélectionnez une sous préfecture</option>";

            if (paysSelectionne in villesParPays) {
                for (var ville in villesParPays[paysSelectionne]) {
                    var optionVille = document.createElement("option");
                    optionVille.value = ville;
                    optionVille.text = ville.charAt(0).toUpperCase() + ville.slice(1);
                    villeSelect.appendChild(optionVille);
                }
            }
        }

        function mettreAJourQuartiers() {
            var paysSelectionne = paysSelect.value;
            var villeSelectionnee = villeSelect.value;

            quartierSelect.innerHTML = "<option value=''>Sélectionnez sous préfecture</option>";

            if (paysSelectionne in villesParPays && villeSelectionnee in villesParPays[paysSelectionne]) {
                for (var i = 0; i < villesParPays[paysSelectionne][villeSelectionnee].length; i++) {
                    var quartier = villesParPays[paysSelectionne][villeSelectionnee][i];
                    var optionQuartier = document.createElement("option");
                    optionQuartier.value = quartier;
                    optionQuartier.text = quartier;
                    quartierSelect.appendChild(optionQuartier);
                }
            }
        }


          function mettreAJourCiters() {
        var quartierSelectionne = quartierSelect.value;
        citerSelect.innerHTML = "<option value=''>Sélectionnez une cité</option>";

        if (quartierSelectionne in citésParQuartier) {
            citésParQuartier[quartierSelectionne].forEach(function(cité) {
                var optionCité = document.createElement("option");
                optionCité.value = cité;
                optionCité.textContent = cité;
                citerSelect.appendChild(optionCité);
            });
        }
    }

        paysSelect.addEventListener("change", mettreAJourVilles);
        villeSelect.addEventListener("change", mettreAJourQuartiers);
        quartierSelect.addEventListener("change", mettreAJourCiters);

        mettreAJourVilles();
        mettreAJourQuartiers();
        mettreAJourCiters();

