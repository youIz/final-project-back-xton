from django_seed import Seed
from .models import *
from django.contrib.auth.hashers import make_password


# SEED CONNEXION________________________________________________________________________
def runConnexion():
    seeder = Seed.seeder()
    roles = [
        {'role': 'Admin'},
        {'role': 'Stock'},
        {'role': 'Web'},
        {'role': 'Member'},
    ]
    for item in roles:
        seeder.add_entity(Role, 1, item)
    print(seeder.execute())

    users = [
        {'username': 'admin', 'email': 'admin@admin.com', 'password': make_password('admin'), 'role': Role.objects.all()[0], 'img_url':'https://png.pngtree.com/png-vector/20191023/ourlarge/pngtree-army-soldier-icon-flat-style-png-image_1846702.jpg', 'newsletter': True},
        {'username': 'stock', 'email': 'stock@stock.com', 'password': make_password('stock'), 'role': Role.objects.all()[1], 'img_url':'https://c8.alamy.com/compfr/r1pj1k/icone-vecteur-soldat-isole-sur-fond-transparent-soldat-transparence-concept-logo-r1pj1k.jpg', 'newsletter': True},
        {'username': 'web', 'email': 'web@web.com', 'password': make_password('web'), 'role': Role.objects.all()[2], 'img_url':'https://cdn-icons-png.flaticon.com/512/5238/5238516.png', 'newsletter': True},
        {'username': 'member', 'email': 'member@member.com', 'password': make_password('member'), 'role': Role.objects.all()[3], 'img_url':'https://www.shutterstock.com/image-illustration/illustration-profile-icon-avatar-military-260nw-2116703420.jpg', 'newsletter': False},
    ]
    for item in users:
        seeder.add_entity(User, 1, item)
    print(seeder.execute())



# SEED BLOG____________________________________________________________________
def runBlog():
    seeder = Seed.seeder()
    tags = [
        {'tag': 'TechBlaster'},
        {'tag': 'LaserStrike'},
        {'tag': 'PlasmaCannon'},
        {'tag': 'QuantumBlade'},
        {'tag': 'CyberPulse'},
        {'tag': 'HoloBlade'},
    ]
    for item in tags:
        seeder.add_entity(Tag, 1, item)
    print(seeder.execute())
    categories = ["Laser Weapons", "Plasma Tech", "Nanotech Arsenal", "Quantum Armaments", "Cybernetic Blades"]
    for category in categories:
        CategoryArticle.objects.create(category=category)

    articles = [
        {
            "title": "Le Monde Obscur des Mercenaires",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130796868050374676/ryakeb_A_gritty_hyper-realistic_image_of_a_mercenary_in_a_dimly_bd451592-21d1-464f-b5f8-5805e773a253.png",
            "description": "Découvrez l'univers mystérieux et sans pitié des mercenaires. Plongez dans les opérations clandestines, les contrats dangereux et les missions secrètes qui défient l'éthique militaire conventionnelle.",
            "category": CategoryArticle.objects.get(category="Cybernetic Blades"),
            "tag": Tag.objects.filter(tag__in=["TechBlaster", "LaserStrike"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "L'Armurerie Futuriste : Technologies au Service du Soldat",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130796927726915684/ryakeb_A_futuristic_soldier_clad_in_an_exoskeleton_armor_standi_413fa606-afa9-4bb9-a5bc-708eae520a0b.png",
            "description": "Explorez les avancées les plus récentes dans le domaine des armes futuristes. Des armures exosquelettes aux drones de combat, découvrez comment la technologie transforme le champ de bataille.",
            "category": CategoryArticle.objects.get(category="Quantum Armaments"),
            "tag": Tag.objects.filter(tag__in=["PlasmaCannon",]),
            "user": User.objects.get(username="web"),
            "validate": True,
        },
        {
            "title": "La Guerre des Ombres: Enquête sur le Trafic d'Armes",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130796897381134376/ryakeb_A_clandestine_meeting_in_a_dark_alley_where_shadowy_figu_f380e8b7-a225-4cbc-a820-74fd569ad6a2.png",
            "description": "Plongez au cœur des réseaux clandestins qui alimentent le trafic d'armes à l'échelle mondiale. Découvrez les figures obscures qui tirent les ficelles de ce commerce illégal et ses implications dévastatrices.",
            "category": CategoryArticle.objects.get(category="Nanotech Arsenal"),
            "tag": Tag.objects.filter(tag__in=["PlasmaCannon", "QuantumBlade"]),
            "user": User.objects.get(username="web"),
            "validate": True,
        },
        {
            "title": "Forces Spéciales: Les Héros Méconnus",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130797044437618749/ryakeb_A_group_of_special_forces_soldiers_in_a_moment_of_quiet__f1e3d6ff-2645-458e-a4bd-e8be0dc579d2.png",
            "description": "Suivez les récits inspirants des hommes et des femmes des forces spéciales. Leurs missions audacieuses et leurs sacrifices désintéressés font d'eux de véritables héros de l'ombre.",
            "category": CategoryArticle.objects.get(category="Quantum Armaments"),
            "tag": Tag.objects.filter(tag__in=["TechBlaster"]),
            "user": User.objects.get(username="web"),
            "validate": True,
        },
        {
            "title": "L'Art de la Guerre : Stratégies et Tactiques Militaires",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130797004625281024/ryakeb_A_grand_military_strategy_room_filled_with_maps_figurine_7eecfc28-a66a-4e99-b37e-c380e94f51d5.png",
            "description": " Explorez les tactiques de guerre utilisées par les grandes puissances militaires. De l'art de la guérilla aux batailles épiques, découvrez comment l'histoire a été façonnée par des stratégies militaires audacieuses.",
            "category": CategoryArticle.objects.get(category="Plasma Tech"),
            "tag": Tag.objects.filter(tag__in=["CyberPulse"]),
            "user": User.objects.get(username="web"),
            "validate": True,
        },
        {
            "title": "Traqués par la Loi : La Chasse aux Criminels",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130797463150809148/ryakeb_A_tense_standoff_between_law_enforcement_and_organized_c_c6e3562d-18bd-4711-b2d5-fb68bdde5809.png",
            "description":"Plongez dans le monde complexe de la lutte contre le crime organisé. Des enquêtes policières aux opérations d'infiltration, suivez la traque incessante des forces de l'ordre contre la mafia.",
            "category": CategoryArticle.objects.get(category="Plasma Tech"),
            "tag": Tag.objects.filter(tag__in=["HoloBlade", "TechBlaster"]),
            "user": User.objects.get(username="web"),
            "validate": True,
        },
        {
            "title": "Les Soldats de l'Ombre : Guerre Secrète contre le Terrorisme",
            "img": "https://cdn.discordapp.com/attachments/1080505525701185557/1130797097650749461/ryakeb_A_special_forces_unit_conducting_a_covert_operation_at_n_331047b3-e23e-4f1b-bf39-6827d40ca45a.png",
            "description": "Découvrez les missions confidentielles menées par les unités spéciales pour combattre le terrorisme. Du renseignement stratégique aux opérations secrètes, explorez le monde méconnu de la guerre contre le terrorisme.",
            "category": CategoryArticle.objects.get(category="Laser Weapons"),
            "tag": Tag.objects.filter(tag__in=["QuantumBlade"]),
            "user": User.objects.get(username="member"),
            "validate": False,
        },
    ]
    for art in articles:
        article = Article.objects.create(
            title=art["title"],
            img=art["img"],
            description=art["description"],
            category=art["category"],
            user=art["user"],
            validate=art["validate"],
        )
        article.tag.set(art["tag"])
    print("Seeding completed successfully!")



# SEED CONTACT_______________________________________________________________
def runContact():
    seeder = Seed.seeder()
    contacts = [
        {
            'tel': '0470 67 51 41', 
            'adresse': 'Pl. de la Minoterie 10, 1080 Molenbeek-Saint-Jean', 
            'email': 'contact@molengeek.be', 
            'fax': '+123456789'
        },
    ]
    for item in contacts:
        seeder.add_entity(Contact, 1, item)
    print(seeder.execute())




# SEED PRODUCT______________________________________________
def runProduct():
    seeder = Seed.seeder()
    categories = [
        {'value': 'Fusil'},
        {'value': 'Arme de poing'},
        {'value': 'Marteau'},
        {'value': 'Arbalète'},
    ]
    for item in categories:
        seeder.add_entity(Category, 1, item)
    print(seeder.execute())
    
    products = [
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340579873050634/ryakeb_a_futuristic_weapon_with_a_sleek_high-tech_aesthetic._It_f547717a-8934-4441-937e-887d074c2345.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340574026186862/ryakeb_a_futuristic_weapon_with_a_sleek_high-tech_aesthetic._It_6e7d3556-bceb-4bef-a8b1-5a993ab08469.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340567919263937/ryakeb_a_futuristic_weapon_with_a_sleek_high-tech_aesthetic._It_420e2dfd-6345-4efb-9720-b334ca7038de.png",
            "description":"Fusil haute technologie, précision inégalée, balles à guidage intelligent.",
            "name":"Spectre-XR",
            'category': Category.objects.all()[0],
            "price":13559,
            'promo': 15,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340600282517504/ryakeb_envision_a_weapon_that_exudes_a_sense_of_mystery_and_res_d61aed1a-5e4d-4444-ab96-b732292297eb.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340606573989968/ryakeb_envision_a_weapon_that_exudes_a_sense_of_mystery_and_res_bafbc314-1068-4cfe-9234-88aa97eaa3b0.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340613658169454/ryakeb_envision_a_weapon_that_exudes_a_sense_of_mystery_and_res_db0d6e44-8556-4524-bd6f-4dfba484bbd8.png",
            "description":"Épée ultra-légère, lame en alliage spécial incassable. Précision et maniabilité exceptionnelles.",
            "name":"Lumina-XS",
            'category': Category.objects.all()[1],
            'price': 399.99,
            'promo': 10,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340635032322078/ryakeb_a_weapon_that_combines_the_old_with_the_new._Its_a_futur_36dd0fcc-c3a7-47a8-a23e-090f2923b800.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340643597107352/ryakeb_a_weapon_that_combines_the_old_with_the_new._Its_a_futur_a852db36-8cc8-4f0c-af94-2283c0e60f15.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340646591832145/ryakeb_a_weapon_that_combines_the_old_with_the_new._Its_a_futur_37c9adcd-fa2f-45ef-8589-019b5da986a5.png",
            "description":"Arbalète silencieuse et puissante. Munitions à tête chercheuse pour une précision maximale.", 
            "name":"Shadow-Bolt",
            'category': Category.objects.all()[3],
            'price': 4549.99,
            'promo': 0,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340674161000478/ryakeb_a_weapon_that_looks_like_it_came_straight_out_of_a_sci-f_565b936d-ecb2-4f2d-81a7-5c63cedf8127.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340683052912640/ryakeb_a_weapon_that_looks_like_it_came_straight_out_of_a_sci-f_ef112c09-8c0c-427d-8dd0-b3d3da350067.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340688102867004/ryakeb_a_weapon_that_looks_like_it_came_straight_out_of_a_sci-f_f99543ea-c147-4afb-b07d-7f0ae96530b7.png",
            "description":"Arme à laser, discrète et mortelle. Faisceau haute précision pour des tirs ciblés.",
            "name":"Viper-Green",
            'category': Category.objects.all()[0],
            'price': 15450,
            'promo': 25,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340702023757886/ryakeb_a_weapon_that_seems_to_defy_the_laws_of_physics._Its_a_g_f750ae2f-5e1d-4c7a-a234-fd15e4cccbee.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340707254063115/ryakeb_a_weapon_that_seems_to_defy_the_laws_of_physics._Its_a_g_cbfe0359-c4e2-43f6-b37d-e5d78657d921.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340725956456539/ryakeb_a_weapon_that_seems_to_defy_the_laws_of_physics._Its_a_g_fe4efec8-fa6c-4105-951f-e4a6fe70165e.png",
            "description":"Marteau surpuissant, forgé dans un alliage indestructible. Frappe destructrice et imposante.",
            "name":"Thunderstrike",
            'category': Category.objects.all()[2],
            'price': 950.50,
            'promo': 15,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340740913332265/ryakeb_a_weapon_that_merges_nature_and_technology._Its_a_bio-en_b340363c-55f6-432c-8e97-9128bc754ac6.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340752200208485/ryakeb_a_weapon_that_merges_nature_and_technology._Its_a_bio-en_f1d03f51-77e2-47bf-8d5f-a592891559e4.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1129340756000260116/ryakeb_a_weapon_that_merges_nature_and_technology._Its_a_bio-en_9d5d83c2-83f2-4cfc-9bfd-e1a22b909172.png",
            "description":"Arbalète silencieuse et rapide, munie de flèches furtives.",
            "name":"Stealth-Arrow",
            'category': Category.objects.all()[3],
            'price': 1049.99,
            'promo': 40,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1130835054159986738/ryakeb_a_futuristic_hand_weapon_that_combines_the_old_with_the__b70f86f7-9eff-4999-8c6f-1c79e1c64c51.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1130835263845847050/ryakeb_a_futuristic_hand_weapon_that_combines_the_old_with_the__f3b430d8-7606-4a4e-a77e-6446cd521fd0.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1130841888933556254/ryakeb_a_futuristic_hand_weapon_that_combines_the_old_with_the__a414f41c-969f-401e-ae3b-a746c89428ea.png",
            "description":"Marteau furtif et acéré, idéal pour l'infiltration.",
            "name":"ShadowBlade-X",
            'category': Category.objects.all()[2],
            'price': 699.99,
            'promo': 20,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1130835286197289020/ryakeb_a_futuristic_hand_weapon_that_looks_like_it_came_straigh_85ada0ee-9613-418d-a9b8-d90fb9848fc2.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1130835283731034184/ryakeb_a_futuristic_hand_weapon_that_looks_like_it_came_straigh_3418f9e5-3546-40aa-a4eb-5aaecbac3211.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1130835277158551562/ryakeb_a_futuristic_hand_weapon_that_looks_like_it_came_straigh_6c8e1d50-635f-44e7-8c39-91cf05c5e61c.png",
            "description":"Couteau tactique et toxique pour neutraliser rapidement les cibles.",
            "name":"VenomStriker-Z",
            'category': Category.objects.all()[1],
            'price': 925,
            'promo': 40,
            'stock':5,
            'wish': False
        },
        {
            "img1":"https://cdn.discordapp.com/attachments/1080505525701185557/1130841935045738546/ryakeb_a_futuristic_firearm_with_a_high-tech_aesthetic._Its_a_p_b1df0b65-f2ca-4289-9251-95e1f18e9889.png",
            "img2":"https://cdn.discordapp.com/attachments/1080505525701185557/1130841929094013050/ryakeb_a_futuristic_firearm_with_a_high-tech_aesthetic._Its_a_p_a6e027fe-d3f5-4323-8b81-4d79635fd0d2.png",
            "img3":"https://cdn.discordapp.com/attachments/1080505525701185557/1130841918377558147/ryakeb_a_futuristic_firearm_with_a_high-tech_aesthetic._Its_a_p_887ba1ff-5d7a-4344-a475-7d2f14dfb93b.png",
            "description":"Arme bleue aux flammes éblouissantes, puissante et envoûtante",
            "name":"AzureFire-X",
            'category': Category.objects.all()[0],
            'price': 14500,
            'promo': 15,
            'stock':5,
            'wish': False
        },
        {
            'img1': 'https://cdn.discordapp.com/attachments/1080505525701185557/1130835040486567986/ryakeb_a_futuristic_firearm_that_exudes_power_and_precision._It_ed7622aa-ee14-4603-9793-aa162ce4cac5.png', 
            'img2': "https://cdn.discordapp.com/attachments/1080505525701185557/1130841858914922637/ryakeb_a_futuristic_firearm_that_exudes_power_and_precision._It_70bb12ec-6baa-40e4-b15a-783a7bd8839e.png", 
            'img3': "https://cdn.discordapp.com/attachments/1080505525701185557/1130835027106738317/ryakeb_a_futuristic_firearm_that_exudes_power_and_precision._It_6573f713-9d0f-4cda-9c2a-91c38c024086.png",
            "description":"Arme puissante, déchaînant une tempête de destruction avec brutalité",
            "name":"Viper-Green22X",
            'category': Category.objects.all()[0],
            'price': 12550,
            'promo': 30,
            'stock':5,
            'wish': False
        },
    ]
    for item in products:
        seeder.add_entity(Product, 1, item)
    print(seeder.execute())