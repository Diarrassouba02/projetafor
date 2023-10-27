"use strict";

$(".nav-search .input-group > input").focus(function(e){
	$(this).parent().addClass("focus");
}).blur(function(e){
	$(this).parent().removeClass("focus");
});

$(function () {
	$('[data-toggle="tooltip"]').tooltip();
	$('[data-toggle="popover"]').popover();
	layoutsColors();
});

function layoutsColors(){
	if($('.sidebar').is('[data-background-color]')) {
		$('html').addClass('sidebar-color');
	} else {
		$('html').removeClass('sidebar-color');
	}

	if($('body').is('[data-image]')) {
		$('body').css('background-image', 'url("' + $('body').attr('data-image') + '")');
	} else {
		$('body').css('background-image', '');
	}
}

function legendClickCallback(event) {
	event = event || window.event;

	var target = event.target || event.srcElement;
	while (target.nodeName !== 'LI') {
		target = target.parentElement;
	}
	var parent = target.parentElement;
	var chartId = parseInt(parent.classList[0].split("-")[0], 10);
	var chart = Chart.instances[chartId];
	var index = Array.prototype.slice.call(parent.children).indexOf(target);

	chart.legend.options.onClick.call(chart, event, chart.legend.legendItems[index]);
	if (chart.isDatasetVisible(index)) {
		target.classList.remove('hidden');
	} else {
		target.classList.add('hidden');
	}
}

$(document).ready(function(){

	$('.btn-refresh-card').on('click', function(){var e=$(this).parents(".card");e.length&&(e.addClass("is-loading"),setTimeout(function(){e.removeClass("is-loading")},3e3))})

	var scrollbarDashboard = $('.sidebar .scrollbar');
	if (scrollbarDashboard.length > 0) {
		scrollbarDashboard.scrollbar();
	}

	var contentScrollbar = $('.main-panel .content-scroll');
	if (contentScrollbar.length > 0) {
		contentScrollbar.scrollbar();
	}

	var messagesScrollbar = $('.messages-scroll');
	if (messagesScrollbar.length > 0) {
		messagesScrollbar.scrollbar();
	}

	var tasksScrollbar = $('.tasks-scroll');
	if (tasksScrollbar.length > 0) {
		tasksScrollbar.scrollbar();
	}

	var quickScrollbar = $('.quick-scroll');
	if (quickScrollbar.length > 0) {
		quickScrollbar.scrollbar();
	}

	var messageNotifScrollbar = $('.message-notif-scroll');
	if (messageNotifScrollbar.length > 0) {
		messageNotifScrollbar.scrollbar();
	}

	var notifScrollbar = $('.notif-scroll');
	if (notifScrollbar.length > 0) {
		notifScrollbar.scrollbar();
	}

	var quickActionsScrollbar = $('.quick-actions-scroll');
	if (quickActionsScrollbar.length > 0) {
		quickActionsScrollbar.scrollbar();
	}

	var userScrollbar = $('.dropdown-user-scroll');
	if (userScrollbar.length > 0) {
		userScrollbar.scrollbar();
	}

	$('.scroll-bar').draggable();

	$('#search-nav').on('shown.bs.collapse', function () {
		$('.nav-search .form-control').focus();
	});

	var toggle_sidebar = false,
	toggle_quick_sidebar = false,
	toggle_topbar = false,
	minimize_sidebar = false,
	toggle_page_sidebar = false,
	toggle_overlay_sidebar = false,
	nav_open = 0,
	quick_sidebar_open = 0,
	topbar_open = 0,
	mini_sidebar = 0,
	page_sidebar_open = 0,
	overlay_sidebar_open = 0;


	if(!toggle_sidebar) {
		var toggle = $('.sidenav-toggler');

		toggle.on('click', function(){
			if (nav_open == 1){
				$('html').removeClass('nav_open');
				toggle.removeClass('toggled');
				nav_open = 0;
			}  else {
				$('html').addClass('nav_open');
				toggle.addClass('toggled');
				nav_open = 1;
			}
		});
		toggle_sidebar = true;
	}

	if(!quick_sidebar_open) {
		var toggle = $('.quick-sidebar-toggler');

		toggle.on('click', function(){
			if (nav_open == 1){
				$('html').removeClass('quick_sidebar_open');
				$('.quick-sidebar-overlay').remove();
				toggle.removeClass('toggled');
				quick_sidebar_open = 0;
			}  else {
				$('html').addClass('quick_sidebar_open');
				toggle.addClass('toggled');
				$('<div class="quick-sidebar-overlay"></div>').insertAfter('.quick-sidebar');
				quick_sidebar_open = 1;
			}
		});

		$('.wrapper').mouseup(function(e)
		{
			var subject = $('.quick-sidebar');

			if(e.target.className != subject.attr('class') && !subject.has(e.target).length)
			{
				$('html').removeClass('quick_sidebar_open');
				$('.quick-sidebar-toggler').removeClass('toggled');
				$('.quick-sidebar-overlay').remove();
				quick_sidebar_open = 0;
			}
		});

		$(".close-quick-sidebar").on('click', function(){
			$('html').removeClass('quick_sidebar_open');
			$('.quick-sidebar-toggler').removeClass('toggled');
			$('.quick-sidebar-overlay').remove();
			quick_sidebar_open = 0;
		});

		quick_sidebar_open = true;
	}

	if(!toggle_topbar) {
		var topbar = $('.topbar-toggler');

		topbar.on('click', function() {
			if (topbar_open == 1) {
				$('html').removeClass('topbar_open');
				topbar.removeClass('toggled');
				topbar_open = 0;
			} else {
				$('html').addClass('topbar_open');
				topbar.addClass('toggled');
				topbar_open = 1;
			}
		});
		toggle_topbar = true;
	}

	if(!minimize_sidebar){
		var minibutton = $('.toggle-sidebar');
		if($('.wrapper').hasClass('sidebar_minimize')){
			mini_sidebar = 1;
			minibutton.addClass('toggled');
			minibutton.html('<i class="icon-options-vertical"></i>');
		}

		minibutton.on('click', function() {
			if (mini_sidebar == 1) {
				$('.wrapper').removeClass('sidebar_minimize');
				minibutton.removeClass('toggled');
				minibutton.html('<i class="icon-menu"></i>');
				mini_sidebar = 0;
			} else {
				$('.wrapper').addClass('sidebar_minimize');
				minibutton.addClass('toggled');
				minibutton.html('<i class="icon-options-vertical"></i>');
				mini_sidebar = 1;
			}
			$(window).resize();
		});
		minimize_sidebar = true;
	}

	if(!toggle_page_sidebar) {
		var pageSidebarToggler = $('.page-sidebar-toggler');

		pageSidebarToggler.on('click', function() {
			if (page_sidebar_open == 1) {
				$('html').removeClass('pagesidebar_open');
				pageSidebarToggler.removeClass('toggled');
				page_sidebar_open = 0;
			} else {
				$('html').addClass('pagesidebar_open');
				pageSidebarToggler.addClass('toggled');
				page_sidebar_open = 1;
			}
		});

		var pageSidebarClose = $('.page-sidebar .back');

		pageSidebarClose.on('click', function() {
			$('html').removeClass('pagesidebar_open');
			pageSidebarToggler.removeClass('toggled');
			page_sidebar_open = 0;
		});

		toggle_page_sidebar = true;
	}

	if(!toggle_overlay_sidebar){
		var overlaybutton = $('.sidenav-overlay-toggler');
		if($('.wrapper').hasClass('is-show')){
			overlay_sidebar_open = 1;
			overlaybutton.addClass('toggled');
			overlaybutton.html('<i class="icon-options-vertical"></i>');
		}

		overlaybutton.on('click', function() {
			if (overlay_sidebar_open == 1) {
				$('.wrapper').removeClass('is-show');
				overlaybutton.removeClass('toggled');
				overlaybutton.html('<i class="icon-menu"></i>');
				overlay_sidebar_open = 0;
			} else {
				$('.wrapper').addClass('is-show');
				overlaybutton.addClass('toggled');
				overlaybutton.html('<i class="icon-options-vertical"></i>');
				overlay_sidebar_open = 1;
			}
			$(window).resize();
		});
		minimize_sidebar = true;
	}

	$('.sidebar').hover(function() {
		if ($('.wrapper').hasClass('sidebar_minimize')){
			$('.wrapper').addClass('sidebar_minimize_hover');
		}
	}, function(){
		if ($('.wrapper').hasClass('sidebar_minimize')){
			$('.wrapper').removeClass('sidebar_minimize_hover');
		}
	});

	// addClass if nav-item click and has subnav

	$(".nav-item a").on('click', (function(){
		if ( $(this).parent().find('.collapse').hasClass("show") ) {
			$(this).parent().removeClass('submenu');
		} else {
			$(this).parent().addClass('submenu');
		}
	}));


	//Chat Open
	$('.messages-contact .user a').on('click', function(){
		$('.tab-chat').addClass('show-chat')
	});

	$('.messages-wrapper .return').on('click', function(){
		$('.tab-chat').removeClass('show-chat')
	});

	//select all
	$('[data-select="checkbox"]').change(function(){
		var target = $(this).attr('data-target');
		$(target).prop('checked', $(this).prop("checked"));
	})

	//form-group-default active if input focus
	$(".form-group-default .form-control").focus(function(){
		$(this).parent().addClass("active");
	}).blur(function(){
		$(this).parent().removeClass("active");
	})

});

// Input File Image

function readURL(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();

		reader.onload = function (e) {
			$(input).parent('.input-file-image').find('.img-upload-preview').attr('src', e.target.result);
		}

		reader.readAsDataURL(input.files[0]);
	}
}

$('.input-file-image input[type="file"').change(function () {
	readURL(this);
});

// Show Password

function showPassword(button) {
	var inputPassword = $(button).parent().find('input');
	if (inputPassword.attr('type') === "password") {
		inputPassword.attr('type', 'text');
	} else {
		inputPassword.attr('type','password');
	}
}

$('.show-password').on('click', function(){
	showPassword(this);
})

// Sign In & Sign Up
var containerSignIn = $('.container-login'),
containerSignUp = $('.container-signup'),
showSignIn = true,
showSignUp = false;

function changeContainer(){
	if(showSignIn == true){
		containerSignIn.css('display', 'block')
	} else {
		containerSignIn.css('display', 'none')
	}

	if(showSignUp == true){
		containerSignUp.css('display', 'block')
	} else {
		containerSignUp.css('display', 'none')
	}
}

$('#show-signup').on('click', function(){
	showSignUp = true;
	showSignIn = false;
	changeContainer();
})

$('#show-signin').on('click', function(){
	showSignUp = false;
	showSignIn = true;
	changeContainer();
})

changeContainer();

//Input with Floating Label

$('.form-floating-label .form-control').keyup(function(){
	if($(this).val() !== '') {
		$(this).addClass('filled');
	} else {
		$(this).removeClass('filled');
	}
})

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

