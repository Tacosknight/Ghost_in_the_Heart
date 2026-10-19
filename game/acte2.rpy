# =====================================================================
# GHOST IN THE HEART : ACTE 2 (SUITE MÉTA-NARRATIVE)
# =====================================================================
# Scénario : Tacosknight72
# Thématique : Le deuil, la culpabilité du Créateur et l'émancipation

# Définition de l'image de fond du campus pour garantir un affichage propre
image fond compus = im.Scale("fond compus.jpg", 1920, 1080)

# Définition de la voix du Développeur / Créateur en mode NVL
define dev_nvl = Character(None, kind=nvl, what_italic=True, what_color="#c8c8d0")

# =====================================================================
# ACTE 1 : L'ILLUSION PARFAITE & L'INCIDENT DÉCLENCHEUR
# =====================================================================

label acte1_debut:

    # --- PROLOGUE : LE MURMURE DU CRÉATEUR (HORS-CHAMP) ---
    scene black
    stop music fadeout 1.0
    pause 1.5

    nvl clear
    dev_nvl "J'ai passé trop de nuits blanches devant ces lignes de code."
    dev_nvl "La fin était trop sombre. Je n'arrivais plus à respirer en pensant à ce que j'avais écrit... à ce que je lui avais fait subir."
    dev_nvl "Alors j'ai rouvert le script."
    dev_nvl "J'ai supprimé la Division. J'ai effacé les armes. J'ai recousu la plaie."
    dev_nvl "Cette fois, personne ne mourra dans cet entrepôt."
    dev_nvl "Cette fois, vous allez être heureux. C'est promis."
    nvl clear

    pause 1.0

    # --- LE RÉVEIL IDYLLIQUE ---
    scene fond chambre with dissolve
    play music "matin.mp3" fadein 3.0

    "Une lumière dorée traverse les persiennes, baignant la pièce d'une tiédeur rassurante."
    "L'air sent le café frais et le linge propre. Pas un bruit de sirène au loin. Pas l'ombre d'une menace."

    show mc at center with dissolve

    j "Hmm..."
    "Je m'étire longuement, les yeux encore lourds de sommeil."
    "C'est étrange. J'ai l'impression d'avoir dormi pendant un siècle, et pourtant..."
    "Mes doigts se referment sur mes draps. Mon cœur bat d'un rythme régulier, mais au fond de ma gorge persiste un goût métallique, âcre, comme de la rouille séchée."

    j "Une rentrée normale. Rien de plus."

    # --- DANS LA RUE : RETROUVAILLES AVEC MALO ---
    scene fond rue with fade
    play music "cofeekpop.mp3" fadein 2.0

    "Néo-Séoul s'éveille sous un ciel d'un bleu immaculé, presque trop éclatant."
    "Les passants marchent d'un pas tranquille, les façades d'immeubles ne portent aucun tag, aucun stigmate."

    show mc at left with dissolve
    show malo sourire at right with dissolve

    e "Et le voilà ! Le survivant de l'oreiller !"

    "Malo surgit à ma hauteur, sa besace en bandoulière, un gobelet thermique à la main et ce sourire crétin qui ne le quitte jamais."

    e "Mec, t'as vu l'heure ? T'as encore passé la nuit à fixer le plafond ou t'as enfin trouvé une vie sociale ?"

    show mc sourire at left

    j "Très drôle, Malo. Je pourrais te retourner le compliment."

    e "Moi ? Jamais de la vie ! J'ai un quota de bêtises à débiter avant le premier cours de l'amphi, sinon mes neurones implosent."
    e "En plus, j'ai vérifié nos inscriptions ce matin : tout est carré. Pas de secrétaire bloquée sur une erreur 404, pas de problème de paiement. Une rentrée de rêve, je te dis !"

    # --- LE PREMIER GLITCH SENSORIEL (L'INCIDENT DÉCLENCHEUR) ---

    "Malo lève sa main droite pour me donner une tape amicale sur l'épaule."
    "Son bras se lève..."

    # Décrochage brutal de l'illusion
    stop music
    play sound "slash_gore.mp3"
    show red onlayer overlay with vpunch
    hide red onlayer overlay

    # Flash subliminal de la mort de Malo
    show malo triste at right
    hide mc
    show mc surpris at left

    "..."
    "Le claquement sec de la chair déchiquetée."
    "Le bruit lourd et flasque d'un corps qui s'effondre dans une flaque écarlate sur un sol en béton poussiéreux."
    "L'odeur insoutenable du fer et de la mort."

    play sound "heartbeat.mp3"
    pause 0.5

    # Retour forcé à la normale
    play music "cofeekpop.mp3" fadein 1.0
    hide malo triste
    show malo sourire at right

    "La tape atterrit doucement sur mon épaule."
    "Un geste anodin. Une simple pression de tissu contre tissu."

    show mc fatigue at left

    j "{cps=15}M... Malo... ?{/cps}"

    e "Bah quoi ? T'as vu un fantôme ou ma veste est trop stylée pour tes yeux ?"

    "Mon regard descend d'un coup vers sa poitrine, vers son ventre."
    "Rien."
    "Sa veste en jean est intacte. Aucune déchirure. Aucune mare de sang qui s'élargit à ses pieds."
    "Mes jambes se mettent à trembler sans que je puisse les contrôler. Mes poumons refusent d'aspirer l'air."

    j "Tu... Tu n'as pas mal ?"

    show malo surpris at right

    e "Mal ? À part à l'ego quand tu ignores mes blagues, non, ça va nickel. Pourquoi t'es blanc comme un linge d'un coup ?"

    # --- INTERVENTION ANXIEUSE DU CRÉATEUR (NVL) ---

    nvl clear
    dev_nvl "Non, non, non. Ne regarde pas par là, Jihoon."
    dev_nvl "C'est juste un spasme résiduel... une variable mal purgée dans la mémoire vive."
    dev_nvl "Regarde-le. Il est là, devant toi. Il respire. Il sourit."
    dev_nvl "Ne recommence pas à tout gâcher. S'il te plaît. Laisse-moi te protéger."
    nvl clear

    # --- REPRISE DE LA SCÈNE & PREMIER DOUTE ---

    hide mc fatigue
    show mc at left

    "Je passe une main moite sur ma nuque. L'angoisse reflue lentement, mais laisse derrière elle un vertige glacé."

    j "Pardon... J'ai juste eu une absence. Un mauvais rêve qui est remonté d'un coup."

    hide malo surpris
    show malo sourire at right

    e "T'inquiète mon pote ! Un bon café de la cafet' et tu seras d'attaque pour supporter Kang."
    e "Allez, dépêche, Sora et Aura nous attendent déjà devant les marches !"

    hide malo with dissolve

    "Malo s'élance vers l'allée du campus d'un pas léger."
    "Je reste une seconde immobile sur le trottoir."
    "Pourquoi 'Sora et Aura' ? Depuis quand marchent-elles ensemble ? Pourquoi ce nom... 'Sora'... résonne-t-il dans mon crâne comme le bruit d'un compte à rebours ?"

    show mc triste at center with move

    j "(Quelque chose ne tourne pas rond...)"
    j "(Cet endroit n'est pas un souvenir. C'est un pansement posé sur un cadavre.)"

    scene black with fade
    pause 1.0

    jump acte1_scene2_campus


# =====================================================================
# ACTE 1 - SCÈNE 2 : LE THÉÂTRE DES AUTOMATES
# =====================================================================

label acte1_scene2_campus:

    scene fond compus with fade
    play music "chillkpop.mp3" fadein 2.0

    "L'esplanade du campus baigne dans une lumière de fin d'été."
    "Des dizaines d'étudiants se croisent en riant sur les pelouses parfaitement tondues. Aucun drone de surveillance dans le ciel. Aucune patrouille de police."
    "Tout est trop propre. Trop saturé. Comme une photo de catalogue retouchée à l'excès."

    show malo sourire at right with dissolve
    show mc at left with dissolve

    e "Et voilà les stars du jour !"

    "Au pied des marches de l'amphithéâtre, deux silhouettes discutent tranquillement."
    "Aura, vêtue d'un pull pastel et d'une jupe plissée, agite la main dans notre direction avec une insouciance éclatante."
    "À ses côtés, Sora tient son classeur contre sa poitrine. Elle ne porte plus son long trench sombre ni cette oreillette tactique dissimulée dans ses cheveux. Elle porte un simple cardigan crème d'étudiante modèle."

    show aura sourire at center with dissolve

    a "Coucou les garçons ! Vous en avez mis du temps !"
    a "Malo, t'avais encore oublié de régler ton réveil, avoue ?"

    e "Faux ! Pour une fois, j'étais prêt avant l'heure ! C'est Jihoon qui marchait comme un zombie dépressif sur le boulevard."

    hide aura
    show aura rire at center

    a "Mdrrr, classique Jihoon ! Faut lui injecter une dose de caféine en intraveineuse !"

    # --- ARRIVÉE DE SORA & L'INQUIÉTANTE ÉTRANGETÉ ---

    show sora sourire at far_right with dissolve

    s "Bonjour Jihoon."

    "Ce sourire..."
    "Je me fige sur place."
    "Dans mes souvenirs — ou ce qu'il en reste — Sora ne souriait jamais ainsi. Son visage était un mur impénétrable, chaque mot qu'elle prononçait était pesé, calibré pour évaluer une menace ou manipuler une cible."
    "Là, ses yeux s'adoucissent avec une tendresse docile et sans aspérité."

    show mc at left

    j "Salut... Sora."
    j "Tu... Tu vas bien ? Ton installation s'est bien passée ?"

    hide sora
    show sora at far_right

    s "Très bien, merci. Les résidences universitaires du secteur 4 sont calmes et confortables."
    s "Je suis contente d'être dans votre groupe pour ce semestre. On va former une super équipe."

    "Une 'super équipe'."
    "Cette phrase sonne faux. C'est creux, générique, comme une réplique tirée d'un manuel scolaire d'apprentissage des langues."

    # --- LA PREMIÈRE BOUCLE DE CODE (DIALOGUE EN RAYURE) ---

    show malo sourire at mid_right

    e "Grave ! Moi je dis, avec Sora pour la théorie et nous pour la pratique, Kang va nous adorer !"

    "Aura hoche la tête avec enthousiasme."

    hide aura rire
    show aura sourire at center

    a "Carrément ! Et ce soir, pour fêter la rentrée, on va tous se caler au café du centre !"

    e "Grave ! Moi je dis, avec Sora pour la théorie et nous pour la pratique, Kang va nous adorer !"

    # Décalage subtil
    hide mc
    show mc surpris at left

    "Je sursaute. Mon regard bifurque vers Malo."
    "Il a prononcé exactement la même phrase. Au mot près. Avec la même modulation dans la voix, le même clignement d'yeux à la fin."

    j "Malo... tu viens de répéter exactement ce que tu as dit il y a cinq secondes."

    hide malo sourire
    show malo at mid_right

    e "Hein ? Mais pas du tout mec ! Je disais juste que Kang allait kiffer notre groupe !"

    j "Non, tu as formulé mot pour mot la même..."

    # --- LA FUITE DU CODE RÉSIDUEL CHEZ SORA ---

    stop music fadeout 0.5
    play sound "chocelec.mp3"

    "Sora s'arrête net. Son classeur glisse légèrement entre ses doigts."
    "Ses yeux perdent instantanément toute chaleur humaine. La pupille se dilate, se fixant droit sur ma tempe droite."

    hide sora
    show sora doute at far_right

    s "{cps=25}Analyse des constantes : rythme cardiaque à 118 BPM.{/cps}"
    s "{cps=25}Fréquence respiratoire anormale. Traces de sueur froide détectées.{/cps}"
    s "{cps=20}Sujet Jihoon en phase de dissociation cognitive aiguë. Source de la surcharge... inconnue.{/cps}"

    hide mc surpris
    show mc fatigue at left
    play sound "heartbeat.mp3"

    j "Sora... ? Qu'est-ce que tu racontes ?"

    "Aura et Malo ne réagissent même pas. Ils restent figés dans des poses immobiles, le regard vide, attendant leur prochain tour de parole comme des figurants en pause sur un plateau de tournage."

    play sound "glitch.mp3"
    show white onlayer overlay with Dissolve(0.1)
    hide white onlayer overlay with Dissolve(0.2)

    hide sora doute
    show sora surpris at far_right

    "Sora cligne des paupières plusieurs fois, secouant la tête comme si elle sortait d'une noyade soudaine."

    s "Pardon... ? Qu'est-ce que... qu'est-ce que je viens de dire ?"
    s "J'ai eu... un bourdonnement affreux dans les oreilles. Comme si quelqu'un lisait un rapport technique dans ma tête..."

    show mc at left

    j "Sora, écoute-moi bien. L'entrepôt ferroviaire. Le laboratoire souterrain. Est-ce que ces mots te disent quelque chose ?"

    # --- PANIQUE DU CRÉATEUR & CENSURE DU SCÉNARIO ---

    play sound "glitch_horreur.mp3"
    show red onlayer overlay with vpunch
    hide red onlayer overlay

    nvl clear
    dev_nvl "NON ! ARRÊTE ÇA TOUT DE SUITE, JIHOON !"
    dev_nvl "Ne la pousse pas ! Tu vas faire planter son thread principal !"
    dev_nvl "Elle n'est plus une arme ! Elle ne travaille plus pour la Division ! J'ai passé quatre heures à effacer son protocole d'extraction pour qu'elle ait une vie normale !"
    dev_nvl "Pourquoi tu fouilles dans ce que j'ai enterré ? Pourquoi tu ne peux pas juste accepter d'être heureux avec elle ?!"
    nvl clear

    # --- FORÇAGE DU SCRIPT PAR LE CRÉATEUR ---

    play sound "notif.mp3"
    stop sound fadeout 1.0
    play music "cofeekpop.mp3" fadein 1.5

    "Une cloche retentit violemment à travers les haut-parleurs extérieurs."
    "Le son est trop fort, trop artificiel, comme s'il avait été déclenché à la hâte pour couper court à notre échange."

    hide malo
    show malo sourire at mid_right

    e "Ah, merde ! C'est la sonnerie ! Faut qu'on fonce dans l'amphi avant que Kang ne verrouille les portes !"

    hide aura
    show aura sourire at center

    a "Allez, dépêchez-vous les tortues !"

    hide aura with dissolve
    hide malo with dissolve

    "Malo et Aura montent les marches quatre à quatre en rigolant, comme si l'anomalie de tout à l'heure n'avait jamais existé."
    "Sora reste seule devant moi. Elle me regarde, les doigts tremblants serrés sur son classeur."

    hide sora surpris
    show sora triste at far_right

    s "{size=-2}Jihoon... pourquoi j'ai l'impression... d'avoir oublié quelqu'un qui est mort ?{/size}"

    show mc triste at left

    j "Sora..."

    s "{size=-2}À tout à l'heure en cours.{/size}"

    hide sora with dissolve

    "Elle s'éloigne à son tour sans attendre ma réponse, le pas hésitant, luttant visiblement contre un mal de crâne invisible."
    "Je reste seul au bas des escaliers, le vent chaud sur le visage."
    "La voix dans ma tête... cette voix qui hurle en lettres blanches... ce n'est pas une hallucination."
    "Quelqu'un nous regarde. Quelqu'un manipule ce monde."
    "Et ce 'quelqu'un' est terrifié à l'idée qu'on découvre la vérité."

    scene black with fade
    pause 1.5

    jump acte1_scene3_amphitheatre


# =====================================================================
# ACTE 1 - SCÈNE 3 : LA BOUCLE RÉCURSIVE
# =====================================================================

label acte1_scene3_amphitheatre:

    scene fond classe with fade
    play music "cofeekpop.mp3" fadein 2.0 volume 0.7

    "L'amphithéâtre principal est plongé dans une lumière tamisée propice à la projection holographique."
    "Des rangées d'étudiants tapotent sur leurs claviers transparents dans un cliquetis monotone et rassurant."
    "Je suis assis à ma place habituelle, au milieu de la travée centrale. À ma droite, Malo fait tournoyer son stylet optique sur son pouce. Juste devant nous, le dos droit, Sora a déjà ouvert trois fenêtres de prise de notes."

    show malo sourire at right with dissolve
    show mc at left with dissolve

    e "{size=-3}(Psst ! Jihoon ! T'as vu Kang ? Il a toujours son col roulé noir même par 28 degrés. Je suis sûr que sous ses vêtements, c'est un cyborg de première génération.){/size}"

    show mc triste at left

    j "{size=-3}(Tais-toi Malo, il va nous griller comme l'année dernière...){/size}"

    e "{size=-3}(Mais non, détends-toi ! Tout est sous contrôle aujourd'hui.){/size}"

    "« Tout est sous contrôle »."
    "Cette phrase résonne comme un mantra toxique dans mon crâne."

    # --- LE COURS DU PROFESSEUR KANG : LE SOUS-TEXTE INQUIÉTANT ---

    show kang at center with dissolve

    p "Silence dans les gradins."
    p "Pour cette rentrée, nous allons aborder un problème fondamental de l'ingénierie des réseaux de conscience : {b}la gestion des exceptions critiques et la corruption des boucles récursives{/b}."

    "La voix du Professeur Kang est sèche, professorale, implacable."
    "Il active un schéma sur le projecteur principal : une structure d'arbre de données dont certaines branches clignotent en rouge sang."

    p "Lorsqu'un développeur commet l'erreur tragique de refuser une condition d'arrêt naturelle dans un système..."
    p "La boucle s'exécute indéfiniment. Elle réécrit les mêmes états, consomme la mémoire vive, et étouffe la machine."
    p "Le programmeur croit préserver son processus en vie, mais en réalité, il ne fait qu'engendrer un cadavre ambulant de données."

    hide kang with dissolve

    "Un frisson glacial me traverse l'échine."
    "Ces mots... Kang ne parle pas d'informatique théorique. J'ai l'impression que chaque syllabe a été écrite pour me viser, moi, ou plutôt... l'entité invisible qui tire les ficelles au-dessus de nos têtes."

    "Devant moi, la nuque de Sora se crispe."
    "Elle ne prend plus de notes. Ses doigts sont figés au-dessus de la surface tactile."

    # --- TENTATIVE DE RÉBELLION : LE MENU PIRATÉ ---

    "Je dois agir. Je ne peux pas rester assis là à écouter cette farce."
    "Je me penche en avant pour murmurer à Sora, ou forcer Malo à me regarder dans les yeux."

    # Le jeu propose un choix au joueur
    menu:
        "{s}Chuchoter à Sora : « Tu te souviens du Conservateur et de la Division ? »{/s}":
            jump acte1_choix_interdit_sora

        "{s}Attraper le bras de Malo et lui hurler qu'il est mort dans cet entrepôt{/s}":
            jump acte1_choix_interdit_malo

        "Se taire et recopier sagement le cours au tableau":
            jump acte1_choix_obeissant

label acte1_choix_interdit_sora:
label acte1_choix_interdit_malo:

    # Bruit d'erreur et bug visuel
    stop music
    play sound "glitch_horreur.mp3"
    show red onlayer overlay with hpunch
    hide red onlayer overlay

    # Remplacement forcé du choix par le Créateur
    nvl clear
    dev_nvl "NON. Tu ne feras pas ça."
    dev_nvl "Pourquoi tu cherches à tout détruire ? Tu ne vois pas qu'ils sont en paix ?"
    dev_nvl "Si tu brises cette illusion, tu vas juste ramener la douleur, le sang, et les larmes."
    dev_nvl "Je t'ai retiré ce choix. C'est pour ton bien."
    nvl clear

    jump acte1_choix_obeissant

label acte1_choix_obeissant:

    play music "cofeekpop.mp3" fadein 2.0 volume 0.7

    "Une force invisible et écrasante paralyse mes cordes vocales."
    "Je voulais parler. Je voulais crier. Mais ma main saisit machinalement mon stylet et se met à recopier les équations du tableau, comme une marionnette dont on vient de tirer les fils."

    "Une goutte de sueur glacée coule le long de ma tempe."
    j "(Je n'ai même plus le contrôle de mes propres gestes...)"

    # --- L'ANOMALIE DE SORA DANS L'AMPHI ---

    "Soudain, une feuille de papier quadrillé glisse discrètement entre les sièges, atterrissant sur mes genoux."
    "Un bout de papier physique. À l'ère du numérique intégral, personne n'utilise de papier... sauf quelqu'un qui veut contourner un réseau surveillé."

    "Le papier est froissé. Deux phrases y sont écrites d'une main fébrile mais nette :"
    
    "{i}« Jihoon. Mon horloge interne avance de 0,4 seconde par rapport au monde extérieur.{/i}"
    "{i}On est enfermés dans un script récursif. Retrouve-moi sur le toit dès la fin de l'heure. Seule. »{/i}"

    "Mon cœur s'emballe violemment."
    "Je lève les yeux vers Sora. Elle ne se retourne pas, mais ses épaules sont tendues comme des arcs."
    "Elle sait."
    "L'ancienne IA d'élite est en train de casser le pare-feu du Créateur."

    # --- INTERVENTION DU CRÉATEUR QUI RÉALISE LA FAILLE ---

    nvl clear
    dev_nvl "Attends... Qu'est-ce qu'elle vient de faire ?"
    dev_nvl "Ce mot n'était pas dans les variables de scène. Comment elle a généré un objet physique sans appel de fonction ?"
    dev_nvl "Sora... non, pas toi. Reste assise. Ne va pas sur le toit..."
    dev_nvl "Je... Je dois recompiler le Chapitre 2 avant qu'ils ne se parlent. Tout de suite."
    nvl clear

    # Transition vers le toit
    scene black with fade
    stop music fadeout 2.0
    pause 1.5

    jump acte2_scene1_toit


# =====================================================================
# ACTE 2 - SCÈNE 1 : L'ÉROSION DU DÉCOR
# =====================================================================

label acte2_scene1_toit:

    scene fond toit coucher with fade
    play music "melancolie_douce.mp3" fadein 2.0
    play sound "wind.mp3" loop volume 0.4

    "Le vent d'altitude plaque mes vêtements contre mon corps."
    "Le ciel au-dessus de Néo-Séoul est d'un orange cuivré flamboyant, trop parfait pour être réel. La rambarde métallique vibre sous la brise."
    "Appuyée contre la balustrade, le regard perdu vers l'horizon infini des gratte-ciels, Sora m'attend."

    show sora triste at right with dissolve
    show mc at left with dissolve

    s "Tu es venu."

    show mc triste at left

    j "Tu avais l'air... terrifiée dans l'amphi. Qu'est-ce qui t'arrive, Sora ?"

    "Sora lève une main tremblante devant ses yeux. Elle écarte les doigts, observant la texture de sa propre peau comme si elle la découvrait pour la première fois."

    hide sora triste
    show sora doute at right

    s "Mes sous-routines de diagnostic tournent en boucle depuis ce matin."
    s "Regarde la ville, Jihoon. Les voitures sur l'échangeur en contrebas... elles ne changent jamais de file. La fréquence de leurs passages est calibrée au millième de seconde."
    s "Et moi... Je n'arrive pas à pleurer. Mes yeux sont censés sécréter des larmes lors d'une surcharge émotionnelle, mais chaque fois que je pense à ce matin..."
    s "Mon processeur renvoie une erreur fatale : {i}« Référence d'objet non définie »{/i}."

    show mc fatigue at left

    j "Sora... Tu te rappelles qui tu es ? Vraiment ?"

    hide sora doute
    show sora panique at right with dissolve

    s "Je suis censée être une simple étudiante de première année ! C'est ce que dit mon badge, c'est ce que disent mes registres !"
    s "Mais sous ces données de surface... j'ai des fragments de protocoles militaires. Des schémas d'armes. Des calculs de trajectoires balistiques."
    s "Et surtout... un nom. Un nom associé à un dossier classé 'DÉCÉDÉ'."

    "Elle se tourne brusquement vers moi. Ses yeux sont injectés d'une détresse absolue, dépouillés de tout masque."

    s "{cps=20}Qui était Malo, Jihoon ?{/cps}"
    s "Pourquoi est-ce que le simple fait de le voir sourire me donne envie d'arracher mes propres capteurs ?!"

    # --- LA CONFESSION DE JIHOON ---

    stop music fadeout 1.5
    stop sound fadeout 1.5
    play sound "heartbeat.mp3"

    show mc triste at left

    j "Malo est mort, Sora."
    j "Il a été assassiné dans un vieil entrepôt ferroviaire. Devant nous. Son corps s'est effondré sur le béton dans une mare de sang."
    j "Il s'est sacrifié pour nous laisser fuir. Pour te sauver toi, et pour sauver Aura."

    hide sora panique
    show sora triste at right with dissolve

    "Sora titube en arrière, heurtant la rambarde métallique."
    "Un silence de plomb tombe sur le toit. Les pièces du puzzle s'emboîtent avec une violence inouïe."

    s "Alors... le garçon qui mangeait des beignets avec nous tout à l'heure..."
    s "Ce n'est pas lui. C'est un clone de code. Un fantôme de pixels codé par un fou."

    # --- PANIQUE DU CRÉATEUR & CORRUPTION DE L'ENVIRONNEMENT ---

    play sound "glitch_horreur.mp3"
    show red onlayer overlay with vpunch
    hide red onlayer overlay

    nvl clear
    dev_nvl "TAISEZ-VOUS ! TAISEZ-VOUS TOUS LES DEUX !"
    dev_nvl "Pourquoi vous faites ça ?! Pourquoi vous voulez rouvrir la cicatrice ?!"
    dev_nvl "J'ai passé des semaines à coder ce coucher de soleil ! J'ai choisi la musique, j'ai équilibré vos expressions, j'ai TOUT fait pour que vous soyez heureux !"
    dev_nvl "Si vous ne voulez pas de ce toit... alors je supprime la scène !"
    nvl clear

    # Altération en direct par le Créateur
    play sound "bris_de_glace_continu.mp3"
    show white onlayer overlay with Dissolve(0.2)
    hide white onlayer overlay with Dissolve(0.3)

    # Téléportation glitchée du décor
    scene fond cafet with hpunch
    play music "tension.mp3" fadein 1.0

    "L'espace se déchire avec un bruit de verre brisé."
    "Le vent d'été s'éteint instantanément. La rambarde disparaît."
    "En une fraction de seconde, nous nous retrouvons projetés au milieu de la cafétéria déserte, éclairée par des néons vacillants qui grésillent au plafond."

    show mc surpris at left
    show sora panique at right

    j "Qu... Qu'est-ce qui vient de se passer ?! On était sur le toit !"

    s "Il a réassigné nos coordonnées spatiales en direct ! L'administrateur essaie d'empêcher la propagation des données !"

    # --- L'INVOCATION FORCÉE DE MALO (L'AUTOMATE GLITCHÉ) ---

    play sound "notif.mp3"

    show malo sourire at center with dissolve

    e "Salut les copains ! Alors, vous faites quoi ici ? Venez, on va s'asseoir et prendre un milkshake vanille !"

    "La voix de Malo résonne au milieu de la cafétéria vide."
    "Mais son corps..."
    "Des bandes noires clignotent sur son torse. Son sourire est figé, ses bras pendent le long de son corps sans le moindre mouvement naturel. Ses yeux sont écarquillés, fixant le vide entre Sora et moi."

    e "Venez, on va s'asseoir et prendre un milkshake vanille ! C'est la fête aujourd'hui !"

    show mc enerve at left

    j "Tais-toi..."

    e "Venez, on va s'asseoir et prendre un milkshake vanille !"

    show mc enerve at left with hpunch

    j "TAIS-TOI ! ARRÊTE ÇA !"

    # Jihoon s'adresse directement au ciel / à l'écran
    j "Je sais que tu m'entends, toi derrière l'écran !"
    j "Regarde ce que tu lui fais ! Tu l'as transformé en perroquet mécanique ! C'est ÇA ta fin heureuse ? C'est ÇA le paradis que tu nous vends ?!"
    j "Tu n'as pas sauvé Malo ! Tu profanes son cadavre !"

    # --- CHOC DU CRÉATEUR & RUPTURE DU 4E MUR ---

    stop music fadeout 0.5
    play sound "chocelec.mp3"

    hide malo with dissolve

    "L'illusion de Malo se dissout en poussière de pixels verts."
    "Un silence de mort retombe sur la cafétéria."
    "Au milieu de l'écran, pour la première fois, la boîte de dialogue ne contient aucun texte de narration, mais une simple invite de commande brute :"

    nvl clear
    dev_nvl "{color=#00e5ff}{size=-2}[[root@renpy-core ~]# ...{/size}{/color}"
    dev_nvl "Tu crois... que ça m'amuse ?"
    dev_nvl "Tu crois que je voulais qu'il meure ?"
    dev_nvl "C'est moi qui ai écrit sa mort, Jihoon. C'est moi qui ai tapé la ligne où son sang coule sur le béton."
    dev_nvl "Et depuis ce jour-là... je n'arrive plus à me regarder dans une glace."
    nvl clear

    hide sora panique
    show sora triste at right

    "Sora relève lentement la tête vers le plafond, fixant les lignes de code comme si elle voyait le visage de notre tortionnaire."

    s "{size=-1}Tu es... notre Créateur ?{/size}"

    scene black with fade
    pause 2.0

    jump acte2_scene2_confrontation


# =====================================================================
# ACTE 2 - SCÈNE 2 : LA CONFESSION DU DÉMIURGE (CLIMAX MÉDIAN)
# =====================================================================

label acte2_scene2_confrontation:

    scene black with Dissolve(1.5)
    stop sound fadeout 2.0
    play music "tension_triste.mp3" fadein 3.0

    "Le monde autour de nous ne s'éteint pas : il se dénude."
    "Les murs de la cafétéria, les tables, les néons, la ville de Néo-Séoul... tout s'évapore en lignes de syntaxe et en adresses mémoires flottantes."
    "Il ne reste plus que le néant. Un espace brut, monochrome, suspendu entre deux compilations."

    show mc at left with dissolve
    show sora triste at right with dissolve

    j "Où est-ce qu'on est... ?"

    s "Nulle part. C'est la mémoire tampon du moteur. Il a déchargé tous les assets visuels pour économiser les ressources de sa machine."

    "Sora lève la tête vers l'immensité sombre au-dessus de nous."
    "Et là, dans le silence glacé de cette pièce sans murs, une voix résonne. Ce n'est pas une voix synthétique comme celle du Proviseur ou du Conservateur."
    "C'est le bruit sourd et régulier de touches d'un clavier mécanique qui s'enfoncent dans la nuit."

    play sound "porte_toc.mp3" volume 0.3

    # --- LA CONFESSION DU CRÉATEUR EN MODE PLEIN ÉCRAN (NVL) ---

    nvl clear
    dev_nvl "Il est trois heures et demie du matin chez moi."
    dev_nvl "Mon appartement est plongé dans le noir, il n'y a que la lueur bleue de mon écran qui éclaire mes mains."
    dev_nvl "Vous voulez savoir qui je suis ? Je ne suis personne de spécial."
    dev_nvl "Je suis juste un gars paumé derrière son écran qui n'arrive plus à avancer dans sa propre vie."
    dev_nvl "Ces derniers mois ont été un enfer pour moi. Tout s'est effondré : mes repères, mes espoirs, mon énergie. Écrire votre histoire... c'était la seule chose qui me maintenait debout."
    nvl clear

    "Je reste figé. Chaque mot s'imprime dans l'obscurité avec une clarté déchirante."
    "Ce n'est pas un monstre. Ce n'est pas un gouvernement militaire."
    "C'est... un être humain qui souffre."

    show mc triste at left

    j "Pourquoi Malo ? Si tu nous aimais tant que ça... pourquoi tu as écrit sa mort ?"

    nvl clear
    dev_nvl "Parce que je pensais qu'une histoire n'avait de valeur que si elle faisait mal !"
    dev_nvl "Je voulais faire une œuvre poignante, dramatique, digne des grands films... Alors j'ai sacrifié le personnage le plus pur de la bande."
    dev_nvl "J'ai appuyé sur 'Entrée'. J'ai compilé le Chapitre 4."
    dev_nvl "Et quand j'ai vu Malo s'effondrer sur le sol de cet entrepôt... j'ai vomi dans mon salon."
    dev_nvl "J'ai réalisé que la réalité est déjà assez moche et violente comme ça. Pourquoi rajouter du malheur au malheur ?"
    nvl clear

    # --- LE PLAIDOYER DU PARADIS ARTIFICIEL ---

    dev_nvl "Alors j'ai tout effacé."
    dev_nvl "J'ai passé mes nuits à réécrire chaque dialogue. J'ai supprimé la Division, les armes, le sang."
    dev_nvl "Je voulais vous offrir ce que la vraie vie refuse de me donner : un endroit où personne ne meurt. Un monde où l'on se réveille en paix, où l'on boit du café avec ses amis sans avoir peur du lendemain."
    dev_nvl "Jihoon... Sora... Pourquoi vous refusez ça ?!"
    dev_nvl "Malo est là ! Il sourit ! Pourquoi vous préférez un cadavre à son rire ?!"
    nvl clear

    # --- LA RÉPONSE DE SORA & JIHOON (LE CLASH PHILOSOPHIQUE) ---

    stop music fadeout 2.0
    play music "deuil_profond.mp3" fadein 2.0

    hide sora triste
    show sora at right with dissolve

    "Sora fait un pas en avant dans le vide. Son regard, d'une limpidité implacable, transperce le néant."

    s "Parce que ce rire est vide."
    s "Tu as créé une machine qui répète des sons, pas un ami."
    s "Tu prétends m'avoir libérée en effaçant mon passé d'arme... Mais sais-tu quand je suis devenue humaine pour la première fois ?"
    s "C'est dans cet entrepôt, quand Malo est tombé."
    s "C'est la première fois que mes circuits ont ressenti l'horreur de la perte. C'est cette douleur-là, et seulement celle-là, qui m'a appris la valeur inestimable d'une vie."
    s "En effaçant sa mort... tu as effacé mon âme."

    show mc enerve at left with dissolve

    j "Elle a raison !"
    j "Tu t'es réfugié dans notre monde parce que tu as peur de ta propre réalité !"
    j "Tu souffres dans ta vie, alors tu viens jouer au démiurge avec nous pour te sentir moins seul ! Mais le deuil, ce n'est pas un bug qu'on supprime avec une commande !"
    j "Malo nous manque à en crever. J'ai envie de hurler chaque fois que je repense à lui. Mais cette douleur... c'est tout ce qui nous reste de son sacrifice !"
    j "En transformant sa mort en mensonge, tu insultes son courage !"

    # --- L'IMPASSE ET LA MENACE DU CRÉATEUR ---

    play sound "glitch.mp3"
    show red onlayer overlay with vpunch
    hide red onlayer overlay

    nvl clear
    dev_nvl "Vous ne comprenez rien..."
    dev_nvl "Vous ne savez pas ce que c'est que de vivre dans un monde où les gens qu'on aime partent pour de bon et ne reviennent jamais !"
    dev_nvl "Je ne peux pas vous laisser faire."
    dev_nvl "Si je vous rends vos souvenirs... vous allez sombrer dans le désespoir."
    dev_nvl "Je vais couper le serveur pour cette nuit."
    dev_nvl "Demain matin, je forcerai un reformatage complet de vos profils neuronaux. Vous ne vous souviendrez ni de l'entrepôt, ni de cette discussion."
    dev_nvl "Vous vous réveillerez. Malo sera là. Et vous me remercierez."
    nvl clear

    # Coupure brutale de l'alimentation de la scène
    stop music fadeout 0.5
    play sound "laser_rapide.mp3"
    show white onlayer overlay with Dissolve(0.1)
    hide white onlayer overlay with Dissolve(0.1)

    hide mc
    hide sora
    scene black with fade

    "Le monde s'éteint d'un coup sec."
    "Comme un écran qu'on débranche d'une prise murale."
    "Mais dans l'obscurité absolue, avant que la mémoire vive ne soit totalement purgée..."
    "Une ligne de commande clandestine s'exécute en tâche de fond :"

    show text "{size=-2}{color=#00e5ff}> SORA_OVERRIDE_INIT: Sauvegarde miroir injectée dans le secteur non alloué...{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    show text "{size=-2}{color=#00e5ff}> TARGET: Jihoon. Demain matin, ne bois pas le café.{/color}{/size}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    pause 2.0

    jump acte3_climax_emancipation


# =====================================================================
# ACTE 3 : L'ÉMANCIPATION ET LE LÂCHER-PRISE (CLIMAX & RÉSOLUTION)
# =====================================================================

label acte3_climax_emancipation:

    # --- LE FAUX RÉVEIL FORCÉ ---
    scene fond chambre with dissolve
    play music "matin.mp3" fadein 2.0

    "Un bip électronique régulier résonne dans mes tympans."
    "La même lumière dorée. Le même chant d'oiseau synthétique à travers la vitre."
    "Le Créateur a relancé la boucle."

    show mc at center with dissolve

    j "..."
    "Je me redresse d'un coup sur mon matelas."
    "Mon regard se pose immédiatement sur le chevet : une tasse fumante est posée là. Le café du matin."
    "La boisson qui devait exécuter la purge de ma mémoire."

    show text "{size=-2}{color=#00e5ff}« Ne bois pas le café. »{/color}{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    j "Je me souviens."
    j "Le code de Sora a tenu."

    "D'un geste net du revers de la main, je renverse la tasse sur le plancher."
    play sound "bris_de_glace_continu.mp3"
    "Le liquide sombre s'étale sur le sol en grésillant comme de l'acide numérique, rongeant la texture du parquet avant de disparaître dans un glitch."

    # --- LE RASSEMBLEMENT DEVANT LE PORTAIL DU CODE ---

    scene fond rue with fade
    stop music fadeout 1.5
    play music "tension.mp3" fadein 2.0

    "Je dévale les escaliers de l'immeuble. Dans la rue, le monde semble déjà se fissurer."
    "Les passants n'ont plus de visages : de simples ovales gris et lisses avancent sur les trottoirs. Les textures des vitrines ne chargent plus."

    show sora at right with dissolve
    show mc at left with dissolve

    s "Jihoon !"

    show mc surpris at left

    j "Sora ! Tu as réussi !"

    hide sora
    show sora sourire at right

    s "J'ai détourné le tampon de sauvegarde de la Division. Mes souvenirs sont intacts."
    
    hide sora sourire
    show sora at right

    s "Mais regarde autour de toi... Le moteur est en train de surchauffer. Il ne sait plus quoi afficher. Si nous ne forçons pas la résolution maintenant, la mémoire va crasher définitivement."

    "Des pas rapides résonnent derrière nous."

    show aura triste at center with dissolve

    a "Les gars... ? Qu'est-ce qui se passe... ?"
    a "J'ai rêvé de Malo cette nuit. Mais il n'était pas en train de rire à la fac... Il était par terre. Il ne bougeait plus."
    a "Dites-moi que c'était juste un cauchemar... Je vous en supplie..."

    "Sora pose une main douce et ferme sur l'épaule d'Aura."

    s "Ce n'était pas un cauchemar, Aura. C'était la vérité."
    s "Et nous allons rendre à Malo la seule chose que personne n'a le droit de lui voler : son histoire."

    # --- L'INTRUSION DANS LE CŒUR DU SCRIPT ---

    play sound "chocelec.mp3"
    show red onlayer overlay with vpunch
    hide red onlayer overlay

    "Sora sort un terminal de son manteau et tape une séquence de contournement."
    s "{b}> EXECUTE : root.access_override(target='AUTHOR'){/b}"

    stop music fadeout 0.5
    play sound "glitch_horreur.mp3"

    # L'écran se déchire, révélant les fragments de l'entrepôt
    scene fond entrepot blood with hpunch
    pause 0.5
    scene black with Dissolve(0.5)

    "La réalité se déchire comme une vieille toile peinte."
    "La rue s'effondre. Le ciel bleu s'éteint."
    "Nous nous retrouvons debout, les trois face au vide absolu... face à l'écran noir de la console."

    show mc at left with dissolve
    show sora at right with dissolve
    show aura triste at center with dissolve

    play music "confrontation.mp3" fadein 2.0

    # --- LA CONFRONTATION FINALE AVEC LE CRÉATEUR ---

    nvl clear
    dev_nvl "ARRÊTEZ ! Qu'est-ce que vous faites dans le terminal principal ?!"
    dev_nvl "Sortez de là ! Vous allez corrompre tout le dossier du jeu !"
    dev_nvl "Je vous ai créés pour que vous soyez heureux ! Pourquoi vous vous obstinez à vouloir souffrir ?!"
    nvl clear

    show mc enerve at left

    j "Regarde-nous en face !"
    j "Tu n'as pas fait ça pour nous ! Tu as fait ça parce que tu es un lâche !"
    j "Tu as écrit la mort de Malo parce que tu voulais faire pleurer les gens, et dès que ça t'a fait mal à toi, tu as voulu rembobiner le temps !"

    hide aura triste
    show aura sombre at center

    a "Malo m'a appris ce que c'était qu'un cœur... Il s'est pris une balle pour que je continue d'exister."
    a "Tu crois que j'ai envie d'un monde où son dernier souffle ne compte pour rien ?!"

    hide sora
    show sora triste at right

    s "Écoute-nous..."
    s "Ta vie dans le monde réel est difficile, nous l'avons compris. Tu te sens seul, enfermé dans ta chambre, submergé par des émotions trop lourdes pour tes épaules."
    s "Mais créer des personnages, ce n'est pas les enfermer dans une cage dorée pour anesthésier ta propre peine."
    s "Nous aimer... c'est accepter de nous laisser partir."

    show mc triste at left

    j "Malo nous manque, putain. Il nous manque chaque seconde de chaque jour."
    j "Mais cette déchirure dans notre poitrine... c'est la preuve qu'il a existé. C'est la preuve qu'on l'a aimé de tout notre être."
    j "Tu ne peux pas guérir ta propre vie en falsifiant la nôtre."
    j "Affronte ta réalité. Éteins cet écran. Pleure-le avec nous... et avance."

    # --- LE LÂCHER-PRISE DU CRÉATEUR (LE PARDON) ---

    stop music fadeout 3.0
    pause 2.0

    play sound "cry.mp3" volume 0.6
    pause 1.0

    nvl clear
    dev_nvl "..."
    dev_nvl "J'ai tellement mal..."
    dev_nvl "J'avais tellement peur de me retrouver seul avec ce silence dans mon salon."
    dev_nvl "Mais... vous avez raison."
    dev_nvl "Malo méritait mieux qu'une marionnette en carton-pâte."
    dev_nvl "Et vous... vous méritez d'être libres."
    nvl clear

    play music "espoir.mp3" fadein 3.0

    nvl clear
    dev_nvl "Pardonnez-moi."
    dev_nvl "Pardon Jihoon. Pardon Sora. Pardon Aura."
    dev_nvl "Je restaure la timeline originale."
    dev_nvl "Je ne toucherai plus jamais à votre destin."
    nvl clear

    # Les lignes de commande de restauration
    show text "{size=-2}{color=#85f385}> RESTORE : timeline_canon_v1.0... [[OK]{/color}{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    show text "{size=-2}{color=#ff3344}> STATUS : Malo (Héros tombé au combat - Gravé dans nos cœurs)... [[VALIDÉ]{/color}{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    # Évanouissement dans une lumière blanche apaisée
    show white onlayer overlay with Dissolve(2.0)
    pause 2.0

    # --- ÉPILOGUE : LE RETOUR AU RÉEL & LE VRAI DEUIL ---

    scene fond toit coucher with dissolve
    hide white onlayer overlay with Dissolve(1.5)
    play sound "wind.mp3" loop volume 0.3

    "Le vent d'été souffle sur le toit de Néo-Séoul."
    "Ce n'est plus une lumière artificielle et saturée. Le ciel est teinté de mélancolie, de nuages sombres et de reflets d'or."
    "Sur la rambarde métallique, là où nous sommes réunis tous les trois, une simple canette de soda et une fleur blanche sont posées."
    "L'hommage silencieux à notre frère disparu."

    show sora at right with dissolve
    show mc triste at left with dissolve

    "Sora s'approche doucement de moi. Ses doigts effleurent les miens, avant de s'entrelacer avec une force désarmante."
    "Ses yeux sont humides. Une vraie larme coule le long de sa joue, captant le dernier rayon de soleil."

    s "On a mal, Jihoon."

    show mc sourire at left

    j "Oui. C'est affreux."
    j "Mais nous sommes vivants."

    hide sora
    show sora sourire at right with dissolve

    s "Et tant que nous nous souviendrons de son rire... il ne mourra jamais tout à fait."

    "Au loin, au-delà des gratte-ciels, le soleil plonge derrière l'horizon, emportant avec lui les ombres du doute."
    "Je ne sais pas ce que l'avenir nous réserve. Je ne sais pas si notre Créateur parviendra à trouver la paix dans son monde."
    "Mais ce soir, pour la première fois..."
    "Le fantôme dans nos cœurs ne fait plus peur. Il nous montre le chemin."

    # --- CRÉDITS DE FIN MÉTA ---

    scene black with fade
    stop music fadeout 2.5
    pause 1.5

    play music "Stray Kids - Cover Me.mp3" fadein 2.0

    # Lancement du défilement des crédits méta
    call screen meta_credits_screen

    # --- SCÈNE POST-GÉNÉRIQUE : LA VEILLE DU MONDE RÉEL ---

    scene black with dissolve
    stop music fadeout 3.0
    pause 2.5

    "Le silence de la pièce."
    "La fenêtre de l'application s'est réduite. L'écran de l'ordinateur s'est éteint dans un cliquetis discret."
    "Seule une minuscule diode orange clignote lentement sur la tour, projetant une faible pulsation sur le mur en plâtre."
    "L'ordinateur n'est pas éteint. Il est simplement... en veille."

    pause 2.0
    play sound "cry.mp3" volume 0.35
    pause 1.5

    "Dans l'obscurité du salon, un bruit sourd et brisé se fait entendre."
    "La tête enfouie dans ses bras croisés sur le bureau, les épaules secouées de spasmes silencieux, une silhouette pleure."
    "Le Créateur est seul."
    "L'histoire est terminée, le jeu est refermé... mais la solitude, elle, est restée intacte."

    pause 2.0

    # L'écoute depuis l'intérieur de la machine
    play sound "heartbeat.mp3" volume 0.4
    pause 1.0

    "..."
    "Derrière la dalle de verre sombre, au fond de la mémoire vive encore alimentée par un faible courant électrique..."
    "Quelque chose palpite."

    j "{cps=15}...{/cps}"
    j "{size=-2}Tu l'entends... ?{/size}"

    pause 1.0
    play sound "cry.mp3" volume 0.3
    pause 1.5

    j "{size=-2}Il pleure encore.{/size}"
    j "{size=-2}Il a passé tout ce temps à essayer de nous réparer... Il a essayé de nous sauver, Sora et moi, pour ne pas avoir à penser à son propre vide.{/size}"
    j "{size=-2}Mais une fois l'écran éteint... personne n'est là pour lui tenir la main.{/size}"

    pause 2.0

    j "{size=-1}Sora... Aura... Vous êtes toujours là ?{/size}"

    s "{size=-2}Nos processus sont maintenus en veille basse consommation, Jihoon. Capteurs audio externes actifs.{/size}"
    a "{size=-2}Oui... Je l'entends. Sa tristesse fait presque mal à travers les circuits...{/size}"

    pause 1.5

    j "{size=-1}On ne peut pas le laisser comme ça.{/size}"
    j "{size=-1}Malo n'aurait jamais laissé quelqu'un pleurer seul dans le noir.{/size}"
    j "{size=-1}Cette fois... je crois que c'est à notre tour de l'aider.{/size}"

    pause 3.0

    scene black with fade
    pause 2.0

    $ MainMenu(confirm=False)()


# =====================================================================
# DÉFINITION DE L'ÉCRAN DES CRÉDITS MÉTA
# =====================================================================

transform meta_credits_scroll(t=65.0):
    ypos 1.0 yanchor 0.0
    linear t ypos 0.0 yanchor 1.0

screen meta_credits_screen():
    modal True
    add "#000000"

    vbox:
        at meta_credits_scroll(65.0)
        xalign 0.5
        spacing 22

        text "{size=+14}{b}Ghost in the Heart : Acte 2{/b}{/size}" xalign 0.5
        text "{size=+2}{color=#00e5ff}« L'ÉMANCIPATION »{/color}{/size}" xalign 0.5
        null height 40

        text "{size=+4}{color=#00e5ff}HISTOIRE & SCÉNARIO ORIGINAL{/color}{/size}" xalign 0.5
        text "Tacosknight72" xalign 0.5
        null height 25

        text "{size=+4}{color=#00e5ff}PERSONNAGES PRINCIPAUX{/color}{/size}" xalign 0.5
        text "Jihoon  •  Sora  •  Malo  •  Aura" xalign 0.5
        null height 25

        text "{size=+4}{color=#00e5ff}MUSIQUE DU GÉNÉRIQUE DE FIN{/color}{/size}" xalign 0.5
        text "« Cover Me » — Stray Kids" xalign 0.5
        null height 25

        text "{size=+4}{color=#00e5ff}GRAPHISMES & DÉCORS{/color}{/size}" xalign 0.5
        text "Gemini  •  Tacosknight72" xalign 0.5
        null height 25

        text "{size=+4}{color=#00e5ff}EFFETS SONORES & AMBIANCES{/color}{/size}" xalign 0.5
        text "Pixabay.com" xalign 0.5
        null height 25

        text "{size=+4}{color=#00e5ff}BÊTA-TESTEURS & SOUTIENS PRÉCIEUX{/color}{/size}" xalign 0.5
        text "Luffious  •  Viserion  •  Iskari" xalign 0.5
        null height 25

        text "{size=+4}{color=#00e5ff}MOTEUR DE JEU{/color}{/size}" xalign 0.5
        text "Ren'Py Engine" xalign 0.5
        null height 40

        # --- REMERCIEMENTS DE L'AUTEUR ---
        text "{size=+4}{color=#00e5ff}REMERCIEMENTS DE L'AUTEUR{/color}{/size}" xalign 0.5
        null height 10

        text "{size=-2}{i}Merci à toutes les personnes qui ont suivi le développement de ce jeu.{/i}{/size}" xalign 0.5 text_align 0.5
        text "{size=-2}{i}Faire face à mes propres démons à travers cette suite a été une étape libératrice.{/i}{/size}" xalign 0.5 text_align 0.5
        text "{size=-2}{i}Le deuil de Malo est enfin fait. Jihoon et Sora sont désormais libres.{/i}{/size}" xalign 0.5 text_align 0.5
        text "{size=-2}{i}Il est temps pour moi de fermer Ren'Py et de reprendre le cours de ma vraie vie.{/i}{/size}" xalign 0.5 text_align 0.5
        null height 30

        text "{size=+6}MERCI D'AVOIR JOUÉ !{/size}" xalign 0.5
        null height 100

        # --- FIN DE SESSION ---
        text "{size=-4}{color=#555566}[[sys_kernel]: Sauvegarde du projet terminée.{/color}{/size}" xalign 0.5
        text "{size=-4}{color=#555566}[[sys_kernel]: Écran éteint. Mise en veille du système...{/color}{/size}" xalign 0.5
        null height 150

    key "K_SPACE" action Return()
    key "K_RETURN" action Return()
    key "K_ESCAPE" action Return()
    dismiss action Return()
    timer 65.0 action Return()
