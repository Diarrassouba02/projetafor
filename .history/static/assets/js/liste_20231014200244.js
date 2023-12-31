
        var paysSelect = document.getElementById("pays");
        var villeSelect = document.getElementById("departement");
        var quartierSelect = document.getElementById("quartier");

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

        paysSelect.addEventListener("change", mettreAJourVilles);
        villeSelect.addEventListener("change", mettreAJourQuartiers);

        mettreAJourVilles();
        mettreAJourQuartiers();

