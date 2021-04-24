class Alien:
    def __init__(self,
                 name='temp',
                 species='temp',
                 homeworld='temp',
                 image=None,
                 description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse'):
        self.name = name
        self.species = species
        self.homeworld = homeworld
        self.image = image
        self.description = description


aliens = {
    "heatblast": Alien('Heatblast', 'Pyronite', 'Pyros',
                       'https://static.wikia.nocookie.net/ben10/images/d/dd/HeatblastUAOfficial.png/revision/latest/scale-to-width-down/187?cb=20180825112954',
                       '''Pyrokinesis
Fire Absorption
Fire Breath
Fire Surfing
Heat Generation
Heat Absorption
Enhanced Strength
Enhanced Durability
Enhanced Jumping
Enhanced Acrobatics
Enhanced Agility
Enhanced Reflexes
Pyro Immunity
Cryo Immunity
Pyrokinetic Flight
Enhanced Speed (via Pyrokinetic Flight)
Limited Terrakinesis
Underwater Survivability
Speed Swimming
Limited Pyroportation
Gas Immunity'''),
    'wildmutt': Alien('Wildmutt', 'Vulpimancer', 'Vulpin',
                      'https://static.wikia.nocookie.net/ben10/images/5/51/Wildmutt_UA_Season_2-12.png/revision/latest/scale-to-width-down/310?cb=20140428151405', '''
Enhanced Smelling
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Acrobatics
Enhanced Strength
Enhanced Hearing
Enhanced Digging
Enhanced Speed
Enhanced Jumping
Enhanced Reflexes
Enhanced Tracking
Quadrupedalism
Bipedalism
Sharp Teeth
Sharp Claws
Prehensile Feet
Wall Climbing
Quill Projection
Sightless Sensing
Invisibility Sight
Nightmarish Face Immunity
  '''),
    'diamondhead': Alien('Diamondhead', 'Petrosapien', 'Petropia',
                         'https://static.wikia.nocookie.net/ben10/images/b/b6/DiamondHead_in_AF.PNG/revision/latest/scale-to-width-down/299?cb=20210314015220',
                         '''
Crystallokinesis
Crystalline Constructs
Crystal Shard Projectiles
Sharp Back Shards
Metamorphic Arms
Weapon Manifestation
Regeneration
Body Alteration
Energy Refraction
Energy Absorption
Energy Redirection
Aging Immunity
Decay Immunity
Time Ray Immunity
Acid Immunity
Heat Resistance
Space Survivability
Enhanced Strength
Enhanced Durability
Crystal Board Surfing
Crystallization
Enhanced Dexterity
Enhanced Jumping
Enhanced Digging
Enhanced Reflexes
Enhanced Acrobatics
Crystal Spit (via cold virus)'''),
    'xlr8': Alien('XLR8', 'Kineceleran', 'Kinet',
                  'https://static.wikia.nocookie.net/ben10/images/5/57/XLR8_OV2.png/revision/latest/scale-to-width-down/310?cb=20140722155203',
                  '''
Enhanced Speed
Enhanced Agility
Enhanced Stamina
Enhanced Jumping
Enhanced Reflexes
Enhanced Recovery
Enhanced Strength
Enhanced Dexterity
Enhanced Durability
Enhanced Directionality
Accelerated Thinking
Sharp Elbow Blades
Sharp Claws
Sharp Feet
Gas Immunity
Wall and Water Running
Prehensile Tail
Vortex Creation'''),
    'greymatter': Alien('Grey Matter', 'Galvan', 'Galvan Prime',
                        'https://static.wikia.nocookie.net/ben10/images/0/02/OmniverseGreyMatter.png/revision/latest/scale-to-width-down/244?cb=20140722160610', '''
Enhanced Intelligence
Enhanced Agility
Enhanced Flexibility
Enhanced Jumping
Wall Crawling
Sharp Teeth
Slippery Body
Underwater Breathing
Prehensile Tongue
Small Space Maneuvering'''),
    'fourarms': Alien('Four Arms', 'Tetramand', 'Khoros',
                      'https://static.wikia.nocookie.net/ben10/images/b/ba/FourArmsUAOfficial.png/revision/latest/scale-to-width-down/279?cb=20180824060056', '''
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Speed
Enhanced Reflexes
Enhanced Jumping
Enhanced Acrobatics
Wrestling Proficiency
Strong/Sharp Teeth
Sonic Clap
Shock Waves
Earthquake Generation
Wall Climbing
Heat Resistance
Gas Immunity
Slime Spit (via cold virus)'''),
    'stinkfly': Alien('Stinkfly', 'Lepidopterran', 'Lepidopterra',
                      'https://static.wikia.nocookie.net/ben10/images/4/4d/Stinkfly_os_render.png/revision/latest/scale-to-width-down/310?cb=20141129032451',
                      '''
Flight
Slime Projectiles
Slime Spit
Methane Gas
Herbicide Projection
Sharp Claws
Sharp Feet
Sharp Tail
Movable Eyes
360° Vision
Wall Crawling
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Dexterity
Enhanced Reflexes
Enhanced Speed (via Flight)'''),
    'ripjaws': Alien('Ripjaws', 'Piscciss Volann', 'Piscciss',
                     'https://static.wikia.nocookie.net/ben10/images/9/9e/Ripjaws_ov_official.png/revision/latest/scale-to-width-down/310?cb=20150925140842', '''
Underwater Breathing
Underwater Vortex Generation
Tail Formation
Speed Swimming
Steel-Bending Jaws
Mouth Expansion
Strong/Sharp Teeth
Sharp Claws
Glowing Eyes
Glowing Lure
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility (underwater)'''),
    'upgrade': Alien('Upgrade', 'Galvanic Mechamorph', 'Galvan B',
                     'https://static.wikia.nocookie.net/ben10/images/6/62/Upgrade_Model.png/revision/latest/scale-to-width-down/310?cb=20200511092500',
                     '''
Technokinesis
Optic Laser
Technological Possession
Technological Enhancement
Technological Repairment
Electrokinesis
Electroporation
Regeneration
Body Alteration
Size Alteration
Arm Extension
Weapon Hands
Tentacles
Elasticity
Space Survivability
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Flexibility
Light Generation'''),
    'ghostfreak': Alien('Ghostfreak', 'Ectonurite', 'Anur Phaetos',
                        'https://static.wikia.nocookie.net/ben10/images/6/6d/Ghostfreak_ov_official.png/revision/latest/scale-to-width-down/230?cb=20150928191817', '''
Flight
Levitation
Deformation
Density Shifting
Smoke Mimicry
Instant Regeneration
Body Possession
Invisibility
Intangibility
Longevity
Mana Absorption Immunity
Corrodium Immunity
Protective and Removable Skin
Movable Eye
Tentacles
Soul Consumption
Life Force Absorption Immunity
Space Survivability
Night Vision
Electronic Disruption
Enhanced Strength
Enhanced Durability
Enhanced Speed
Enhanced Agility
Sharp Claws
True Form Only:
Telekinesis
Darkness Empowerment
Energy Beams
Skull Rotation
Sharp Teeth'''),
    'cannonbolt': Alien('Cannonbolt', 'Arburian Pelarota', 'Arburia',
                        'https://static.wikia.nocookie.net/ben10/images/1/1a/Updated_Cannonbolt.PNG/revision/latest/scale-to-width-down/310?cb=20190801042840', '''
Enhanced Speed
Sphere Transformation
Enhanced Strength
Enhanced Durability
Enhanced Balance
Enhanced Agility
Enhanced Jumping
Enhanced Ricocheting
Enhanced Dexterity
Enhanced Reflexes
Enhanced Hearing
Enhanced Directionality
Shock Waves
Tornadoes
Echolocation
Energy Deflection
Sharp Claws
Sharp Teeth
Sharp Feet
Heat Resistance
Cold Resistance
Acid Immunity
Lava Immunity
Radiation Immunity
Plasma Ball Immunity
Mobile Invulnerability
Electrical Empowerment
Limited Space Survivability'''),
    'wildvine': Alien('Wildvine', 'Florauna', 'Flors Verdance',
                      'https://static.wikia.nocookie.net/ben10/images/2/23/OmniverseWildvine.png/revision/latest/scale-to-width-down/310?cb=20140526205023', '''
Chlorokinesis
Explosive Fruit Pods
Camouflage
Regeneration
Elasticity
Size Alteration
Body Alteration
Plant Merging
Sharp Flytrap
Sharp Teeth
Sharp Thorn Claws
Tentacles
Vine Generation
Prehensile Vines
Thorn Generation
Gas Immunity
Hypnosis Immunity
Enhanced Strength
Enhanced Digging
Enhanced Durability
Enhanced Agility
Enhanced Flexibility
Enhanced Jumping
Corruptura Resistance'''),
    'spitter': Alien('Spitter', 'Sphoeroid', 'Scalpasc',
                     'https://static.wikia.nocookie.net/ben10/images/f/fe/Spitter_Model.png/revision/latest/scale-to-width-down/310?cb=20180824040912', '''
Slime Spit
Sharp Teeth
Body Inflation
Enhanced Strength
Poison Gas Immunity'''),
    'buzzshock': Alien('Buzzshock', 'Nosedeenian', 'Nosedenn Quasar',
                       'https://static.wikia.nocookie.net/ben10/images/1/17/Buzzshock_official.png/revision/latest/scale-to-width-down/256?cb=20141129095705', '''
Electrokinesis
Technokinesis
Electric Absorption
Electric Redirection
Electric Teleportation
Electrical Possession
Electrokinetic Flight
Sonic Scream
Enhanced Strength
Enhanced Agility
Enhanced Speed
Enhanced Durability
Self Duplication (with enough power)
Sphoeroid Slime Conductivity'''),
    'arctiguana': Alien('Arctiguana', 'Polar Manzardill', 'X\'Nelli',
                        'https://static.wikia.nocookie.net/ben10/images/e/e6/OV_Teen_Arctiguana.png/revision/latest/scale-to-width-down/310?cb=20200518004848', '''
Freeze Ray Emission
Cryokinetic Flight
Cryo Immunity
Gas Immunity
Sharp Teeth
Sharp Claws
Sharp Back Spikes
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Dexterity
Quadrupedalism
Bipedalism
Wall Crawling'''),
    'blitzwolfer': Alien('Blitzwolfer', 'Loboan', 'Luna Lobo',
                         'https://static.wikia.nocookie.net/ben10/images/a/a8/20298.png/revision/latest/scale-to-width-down/310?cb=20200522084648', '''
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Reflexes
Enhanced Speed
Enhanced Jumping
Enhanced Stamina
Enhanced Smelling
Enhanced Hearing
Sonic Howls
Sonic Propulsion
Sonic Redirection
Sharp Claws
Sharp Teeth
Prehensile/Sharp Feet
Sharp Elbow Spikes
Sharp Shoulder Spikes
Prehensile Tail
Night Vision
Quadrupedalism
Corrodium Immunity'''),
    'upchuck': Alien('Upchuck', 'Gourmand', 'Peptos XII',
                     'https://static.wikia.nocookie.net/ben10/images/8/87/Upchuck_Clear.png/revision/latest/scale-to-width-down/310?cb=20210318135358', '''
Solid Matter Ingestion
Energy Ingestion
Explosive Vomit
Acid Spit
Slime Spit
Mouth Expansion
Strong Prehensile Tongues
Strong Teeth
Flight (via Propulsion)
Swarm Gastronomy
Sharp Claws
Sharp Feet
Space Survivability
Enhanced Agility
Enhanced Speed
Enhanced Durability
Enhanced Jumping
Enhanced Flexibility'''),
    'snareoh': Alien('Snare-oh', 'Thep Khufan', 'Anur Khufos',
                     'https://static.wikia.nocookie.net/ben10/images/e/ea/Ben-10-omniverse-ben-snare-oh.png/revision/latest/scale-to-width-down/310?cb=20141129032220', '''
Shapeshifting
Elasticity
Small Space Maneuvering
Regeneration
Body Separation
Bandage Generation
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Reflexes
Enhanced Flexibility
Enhanced Jumping
Enhanced Speed
Wall Scaling
Night Vision
Underwater Breathing
Space Survivability
Gas Immunity
Corrodium Immunity
Magic Curse Usage'''),
    'frankenstrike': Alien('Frankenstrike', 'Transylian', 'Anur Transyl',
                           'https://static.wikia.nocookie.net/ben10/images/d/d7/OmniverseFrankenstrike.png/revision/latest/scale-to-width-down/288?cb=20140404172804', '''
Enhanced Strength
Enhanced Durability
Enhanced Speed
Enhanced Dexterity
Enhanced Reflexes
Enhanced Jumping
Technokinesis
Electromagnetism
Electrokinetic Levitation
Electrokinesis
Electrical Redirection
Space Survivability
Immense Life Span
Heat Resistance
Corrodium Immunity'''),
    'ditto': Alien('Ditto', 'Splixson', 'Hathor',
                   'https://static.wikia.nocookie.net/ben10/images/8/8f/Ditto_Model.png/revision/latest/scale-to-width-down/219?cb=20200511092800', '''
Self-Duplication
Sensory Web
Enhanced Flexibility
Enhanced Agility
Enhanced Acrobatics
Enhanced Jumping
Enhanced Digging
Enhanced Speed
Enhanced Strength
Enhanced Durability
Underwater Breathing'''),
    'waybig': Alien('Way Big', 'To\'kustar', 'Cosmic Storms',
                    'https://static.wikia.nocookie.net/ben10/images/5/52/AF_WayBig.png/revision/latest/scale-to-width-down/184?cb=20200521143317', '''
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Acrobatics
Enhanced Reflexes
Cosmic Rays
Sharp Head Fin
Sharp Arm Blades
Sharp Shoulder Blades
Sharp Wristbands
Space Survivability
Temperature Resistance
Enhanced Speed'''),
    'eyeguy': Alien('Eye Guy', 'Opticoid', 'Sightra',
                    'https://static.wikia.nocookie.net/ben10/images/a/ad/OmniverseEyeGuy.png/revision/latest/scale-to-width-down/285?cb=20200915123830', '''
Mátikinesis
Movable Eyes
Eye Merging
Elastic Chest Eye
Optic Beams
Energy Beams
Electrical Beams
Freeze Rays
Fire Blasts
Eye Goo
360° Vision
Vision Smelling
Enhanced Hearing
Sharp Claws
Enhanced Strength
Enhanced Reflexes
Enhanced Dexterity
Enhanced Agility
Enhanced Jumping
Enhanced Acrobatics'''),
    'swampfire': Alien('Swampfire', 'Methanosian', 'Methanos',
                       'https://static.wikia.nocookie.net/ben10/images/d/d0/Swampfire_uaf_official.png/revision/latest/scale-to-width-down/199?cb=20141129034947', '''
Chlorokinesis
Pyrokinesis
Methane Generation
Fertilizer Gas Generation
Sleeping Spores
Adhesive Mud
Seed Generation
Vine Generation
Vine Tentacles
Regeneration
Elasticity
Body Alteration
Pyrokinetic Flight
Gas Immunity
Strong Teeth
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Flexibility
Enhanced Digging
Enhanced Jumping
Enhanced Speed
Enhanced Stamina
After Blossoming:
Strength Enhancement
Vine Whips
Levitation
Sharp Arm Spikes
Sharp Shoulder Spikes
Sharp Foot Thorns
Sentient Plant Manipulation'''),
    'echoecho': Alien('Echo Echo', 'Sonorosian', 'Sonorosia',
                      'https://static.wikia.nocookie.net/ben10/images/c/c8/EEAFT.png/revision/latest/scale-to-width-down/238?cb=20171022040816', '''
Audiokinesis
Sonic Redirection
Sonic Force Fields
Self-Duplication
Echolocation
Enhanced Jumping
Enhanced Agility
Enhanced Acrobatics
Enhanced Speed
Enhanced Strength
Enhanced Durability
Vibration Detection
Vibration Empowerment
Levitation
Object Duplication
Sonic Sneezes (via Cold Virus)'''),
    'humungousaur': Alien('Humungousaur', 'Vaxasaurian', 'Terradino',
                          'https://static.wikia.nocookie.net/ben10/images/f/fa/Humungousaur_UAF_Model.png/revision/latest/scale-to-width-down/310?cb=20190731071035', '''
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Reflexes
Enhanced Jumping
Stegosauride Features
Size Alteration
Strength Enhancement (when growing)
Quadrupedalism
Powerful Roar
Powerful Tail
Strong/Sharp Teeth
Sonic Clap
Shock Waves
Wind Resistance
Suction Immunity
Heat Resistance
Limited Space Survivability
Slime Spit (via Cold Virus)'''),
    'jetray': Alien('Jetray', 'Aerophibian', 'Aeropela',
                    'https://static.wikia.nocookie.net/ben10/images/6/61/JetrayProfilePicture.png/revision/latest/scale-to-width-down/310?cb=20200921154751', '''
Enhanced Speed
Neuroshock Blasts
Prehensile Tail
Prehensile/Sharp Feet
Sharp Claws
Sharp Teeth
Space Survivability
Hyperspace Entrance
Speed Swimming
Underwater Breathing
Heat Resistance
Fire Generation (via Neuroshock Blasts)
Enhanced Stamina
Enhanced Agility
Enhanced Strength
Enhanced Durability
Electricity Immunity
Radiation Immunity'''),
    'bigchill': Alien('Big Chill', 'Necrofriggian', 'Kylmyys',
                      'https://static.wikia.nocookie.net/ben10/images/2/29/BCAF2T.png/revision/latest/scale-to-width-down/310?cb=20171022040816', '''
Cryokinesis
Ice Breath
Wind Breath
Freezing Touch
Flight
Levitation
Intangibility
Sharp Claws
Sharp/Prehensile Feet
Strong Teeth
Solid Matter Ingestion
Gas Immunity
Hypnosis Resistance
Enhanced Strength
Enhanced Durability
Enhanced Agility
Temperature Resistance
Radiation Immunity
Space Survivability
Underwater Breathing'''),
    'chromastone': Alien('Chromastone', 'Crystalsapien', 'Petropia',
                         'https://static.wikia.nocookie.net/ben10/images/f/fe/Chromastone_Clear.png/revision/latest/scale-to-width-down/167?cb=20200823212127', '''
Ultraviolet Manipulation
Dynakinesis
Energy Absorption
Energy Aura
Energy Redirection
Mana Absorption
Heat Resistance
Radiation Immunity
Electricity Immunity/Conductivity
Flight
Light Generation
Rainbow Generation
Force Field Generation
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Jumping
Sharp Crystals
Space Survivability
Arachnichimp Webbing Dissolving
Xenocite Possession Immunity'''),
    'brainstorm': Alien('Brainstorm', 'Cerebrocrustacean', 'Encephalonus IV',
                        'https://static.wikia.nocookie.net/ben10/images/e/e9/Accurate_Brainstorm.png/revision/latest/scale-to-width-down/310?cb=20210314023450', '''
Enhanced Intelligence
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Acrobatics
Accelerated Calculations
Sharp Pincers
Sharp Legs
Sharp Spikes
Mnemokinesis
Technokinesis
Electrokinesis
Electrical Telekinesis
Electrical Telepathy
Electric Force Fields
Levitation
Wall Scaling
Web Scaling
Cold Resistance
Underwater Breathing'''),
    'spidermonkey': Alien('Spidermonkey', 'Arachnichimp', 'Aranhachimmia',
                          'https://static.wikia.nocookie.net/ben10/images/8/84/Spidermonkey_UAF.png/revision/latest/scale-to-width-down/310?cb=20210320001700',
                          '''
Webbing Generation
Enhanced Agility
Enhanced Balance
Enhanced Reflexes
Enhanced Dexterity
Enhanced Acrobatics
Enhanced Hearing
Enhanced Strength
Enhanced Durability
Enhanced Reorientation
Web Scaling
Wall Scaling
Sharp Teeth
Sticky Fur
Prehensile Feet
Prehensile Tail
Bipedalism
Sextupedalism
Skilled Melee Combatant'''),
    'goop': Alien('Goop', 'Polymorph', 'Viscosia',
                  'https://static.wikia.nocookie.net/ben10/images/3/36/Goop_Clear.png/revision/latest/scale-to-width-down/289?cb=20181002093250', '''
Indestructibility
Regeneration
Gookinetic Shapeshifting
Slime Generation
Adhesive Slime
Acidic Slime
Slippery Body
Body Alteration
Body Separation
Elasticity
Levitation
Flight
Movable Eyes
Enhanced Strength
Enhanced Agility
Enhanced Flexibility
Underwater Breathing
Wall Scaling
Density Shifting
Heat Resistance
Object Mimicry
Small Space Maneuvering
'''),
    'alienx': Alien('Alien X', 'Celestialsapien', 'Forge of Creation',
                    'https://static.wikia.nocookie.net/ben10/images/e/ee/Alien_X_2.png/revision/latest/scale-to-width-down/179?cb=20210314022316',
                    '''Omnipotence'''),
    'lodestar': Alien('Lodestar', 'Biosovortian', 'Unknown',
                      'https://static.wikia.nocookie.net/ben10/images/1/1c/Lodestar.png/revision/latest/scale-to-width-down/238?cb=20210319224513', '''
Magnetokinesis
Magnetoreception
Magno-Telekinesis
Magnetic Dismantlement
Magnetic Force Field Generation
Electro-Magnetokinesis
Levitation
Flight
Magnetic Regeneration
Sharp Claws
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Space Survivability
Ferrokinesis (via Magnetism)'''),
    'rath': Alien('Rath', 'Appoplexian', 'Appoplexia',
                  'https://static.wikia.nocookie.net/ben10/images/5/56/Rath_1.png/revision/latest/scale-to-width-down/310?cb=20210314024327', '''
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Reflexes
Enhanced Balance
Enhanced Speed
Enhanced Jumping
Enhanced Stamina
Quadrupedalism
Wall Scaling
Wrestling Proficiency
Shock Waves
Powerful Roar
Strong/Sharp Teeth
Sharp Retractable Claws
Gas Immunity
Space Survivability'''),
    'nanomech': Alien('Nanomech', '1/2Human 1/2Nanochip', 'None',
                      'https://static.wikia.nocookie.net/ben10/images/c/cd/UAF-Nanomech.png/revision/latest/scale-to-width-down/304?cb=20191119094941', '''
Bio-Electrokinesis
Size Alteration
Flight
Sharp Claws
Energy Tentacles
Adaptability
Technological Expertise
Technological Disassembly
Technopathy
Nanochip Queen Control Immunity
Enhanced Strength
Enhanced Agility (via Flight)
Enhanced Speed (via Flight)'''),
    'waterhazard': Alien('Water Hazard', 'Orishan', 'Kiusana',
                         'https://static.wikia.nocookie.net/ben10/images/7/7b/Waterguy.png/revision/latest/scale-to-width-down/277?cb=20210314025341', '''
Hydrokinesis
Hydrokinetic Flight
Moisture Absorption
Water Whips
Bubble Shields
Sharp Claws
Sharp Leg Spikes
Sharp Foot Spikes
Gas Immunity
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Reflexes
Enhanced Jumping
Underwater Breathing
Radiation Immunity'''),
    'ampfibian': Alien('AmpFibian', 'Amperi', 'Tesslos',
                       'https://static.wikia.nocookie.net/ben10/images/e/e1/Ns457Wv.png/revision/latest/scale-to-width-down/272?cb=20210314022620', '''
Electrokinesis
Electroportation
Electrical Absorption
Electrical Redirection
Electrical Telepathy
Stretchable Arms
Flight
Intangibility
Circuitry Travel
Energy Shield
Enhanced Durability
Enhanced Strength
Enhanced Agility
Enhanced Flexibility
Enhanced Speed
Enhanced Dexterity
Space Survivability
Speed Swimming
Underwater Breathing'''),
    'armodrillo': Alien('Armodrillo', 'Talpaedan', 'Terraexcava',
                        'https://static.wikia.nocookie.net/ben10/images/f/f3/Armodrillo_2.png/revision/latest/scale-to-width-down/310?cb=20210314023024', '''
Terrakinesis
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Jumping
Enhanced Digging
Shock Waves
Earthquake Generation
Fissure Creation
Gas Immunity
Arm Extension
Sharp Claws
Drill Hands
Jackhammer Arms
Jackhammer Propulsion'''),
    'terraspin': Alien('Terraspin', 'Geochelone Aerio', 'Aldabra',
                       'https://static.wikia.nocookie.net/ben10/images/4/4d/Terraspin_2T.png/revision/latest/scale-to-width-down/310?cb=20200521143609', '''
Shell Flight
Aerokinesis
Tornado Generation
Air Suction
Levitation
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility (via Shell Flight)
Enhanced Speed (via Shell Flight)
Sharp Spinning Arms
Sharp Retractable Claws
Sharp Teeth
Retractable Head and Limbs
Mouth Expansion
Object Redirection (via Wind Blasts)
Fire Suppression (via Wind Blasts)
Poisonous Gas Immunity
Selective Mana Immunity
Selective Magic Immunity'''),
    'nrg': Alien('NRG', 'Prypiatosian-B', 'Prypiatos',
                 'https://static.wikia.nocookie.net/ben10/images/9/97/NRG.png/revision/latest/scale-to-width-down/310?cb=20200523084245', '''
Radiokinesis
Nucleokinesis
Intense Heat Generation
Lava Eruptions
Heat/Cold Immunity
Lead Immunity
Radiation Immunity
Enhanced Strength
Enhanced Durability
Lucubra Possession Immunity
Corruptura Immunity
Outside of Armor:
Shapeshifting
Enhanced Agility
Flight
Intangibility
Light Generation
Energy Absorption
Energy Consumption
Size Alteration (via Energy Absorption)
Underwater Survivability'''),
    'fasttrack': Alien('Fasttrack', 'Citrakayah', 'Chalybeas',
                       'https://static.wikia.nocookie.net/ben10/images/f/f4/FasttrackUAOfficial.png/revision/latest/scale-to-width-down/158?cb=20180827014032', '''
Enhanced Speed
Enhanced Agility
Enhanced Stamina
Enhanced Strength
Enhanced Jumping
Enhanced Reflexes
Enhanced Recovery
Enhanced Balance
Enhanced Dexterity
Enhanced Durability
Enhanced Directionality'''),
    'clockwork': Alien('Clockwork', 'Chronosapien', 'Unknown',
                       'https://static.wikia.nocookie.net/ben10/images/0/0f/20229.png/revision/latest/scale-to-width-down/310?cb=20200522084942', '''
Chronokinesis
Chronopathy
Time Rays
Time Travel
Time Reduction
Retrocognitive Projections
Space Survivability
360° Head Rotation
Enhanced Strength
Chronosapien Power Detection'''),
    'chamalien': Alien('Chamalien', 'Merlinisapien', 'Unknown',
                       'https://static.wikia.nocookie.net/ben10/images/d/d3/UltimateAlienChamAlien.png/revision/latest/scale-to-width-down/302?cb=20190820072643', '''
Camouflage
Sharp Teeth
Sharp Claws
Sharp Head Spike
Retractable Tail Stinger
Slippery Body
Wall Scaling
Bipedalism
Quadrupedalism
Enhanced Flexibility
Enhanced Agility
Enhanced Strength
Enhanced Durability
Enhanced Speed (via Wall Scaling and/or Quadrupedalism)'''),
    'eatle': Alien('Eatle', 'Oryctini', 'Coleop Terra',
                   'https://static.wikia.nocookie.net/ben10/images/8/82/UAeatlepose.png/revision/latest/scale-to-width-down/310?cb=20180904085628', '''
Solid Matter Ingestion
Laser Beams (after eating)
Strong/Sharp Horn
Sharp Claws
Strong Teeth
Wall Climbing
Enhanced Speed
Enhanced Charging
Enhanced Agility
Enhanced Jumping
Enhanced Strength
Enhanced Durability
Broken Limb Immunity'''),
    'juryrigg': Alien('Juryrigg', 'Planchaküle', 'Aul-Turrhen',
                      'https://static.wikia.nocookie.net/ben10/images/9/98/Jury_Rigg.png/revision/latest/scale-to-width-down/189?cb=20141129041657', '''
Mechanical Intuition
Technological Disassembly
Technological Repairment
Technological Modification
Wall Climbing
Sharp Teeth
Sharp Spikes
Sharp Claws
Sharp/Prehensile Tail
Enhanced Agility
Enhanced Strength
Enhanced Dexterity
Enhanced Intelligence
Enhanced Jumping
Enhanced Durability
Enhanced Speed (while Breaking/Fixing Machinery)'''),
    'shocksquatch': Alien('Shocksquatch', 'Gimlinopithecus', 'Pattersonea',
                          'https://static.wikia.nocookie.net/ben10/images/a/a6/Shocksquatch_omniverse_official.png/revision/latest/scale-to-width-down/310?cb=20200529102853', '''
Electrokinesis
Electrical Telekinesis
Force Field Generation
Quadrupedalism
Cold Immunity
Radiation Immunity
Sharp Teeth
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Speed
Enhanced Jumping
Enhanced Agility
Enhanced Reflexes'''),
    'feedback': Alien('Feedback', 'Conductoid', 'Teslavorr Nebula',
                      'https://static.wikia.nocookie.net/ben10/images/f/f3/Teen_Feedback_Stand.png/revision/latest/scale-to-width-down/310?cb=20200522083458', '''
Electrokinesis
Energy Absorption
Energy Redirection
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Agility
Enhanced Jumping
Enhanced Reflexes
Enhanced Speed (on electrical lines)
Radiolocation
Quadrupedalism
Electrokinetic Levitation
Electrokinetic Flight
Space Survivability
Sharp Teeth
Elastic Antennae Tentacles'''),
    'bloxx': Alien('Bloxx', 'Segmentasapien', 'Polyominus',
                   'https://static.wikia.nocookie.net/ben10/images/5/5b/Bloxx.png/revision/latest/scale-to-width-down/310?cb=20190816100150', '''
Shapeshifting
Building Block Manipulation
Explosive Projectiles
Elasticity
Regeneration
Size Alteration
Body Alteration
Body Separation
Body Encasing
Sphere Transformation
Heat Resistance
Radiation Immunity
Enhanced Strength
Enhanced Agility
Enhanced Durability
Enhanced Dexterity
Enhanced Jumping
Enhanced Reflexes
Enhanced Speed (via Sphere Transformation)
Space Survivability'''),
    'gravattack': Alien('Gravattack', 'Galilean', 'Keplorr\'s Orbit',
                        'https://static.wikia.nocookie.net/ben10/images/e/ed/Gravattack_Pose.png/revision/latest/scale-to-width-down/310?cb=20130801094446', '''
Gravikinesis
Black Hole Generation
Quasar Generation
Force Field Generation
Levitation
Speed Reduction
Orbitakinesis
Self-Gravity Manipulation
Planetoid Form
Flight
Enhanced Strength
Enhanced Durability
Enhanced Agility
Space Survivability'''),
    'crashhopper': Alien('Crashhopper', 'Orthopterran', 'Unknown',
                         'https://static.wikia.nocookie.net/ben10/images/4/43/OV_Crashhopper.png/revision/latest/scale-to-width-down/200?cb=20200613085908', '''
Enhanced Jumping
Enhanced Agility
Enhanced Acrobatics
Enhanced Reflexes
Enhanced Ricocheting
Enhanced Strength
Enhanced Durability
Enhanced Speed
Hard/Sharp Head
Strong Knees
Sharp Claws
Sharp Arm Spikes
Sharp Leg Spikes
Sharp Feet
Shock Waves
Quadrupedalism
Wall Climbing'''),
    'ballweevil': Alien('Ball Weevil', 'Unknown', 'Atrocius 0',
                        'https://static.wikia.nocookie.net/ben10/images/2/2c/Ball_weevil_omniverse_official.png/revision/latest/scale-to-width-down/300?cb=20141129094309', '''
Plasma Ball Generation
Plasma Whips
Sharp Jaws
Sharp Horn
, 'Enhanced Agility
Enhanced Balancing
Enhanced Dexterity
Enhanced Speed
Enhanced Strength
Wall Climbing
Bipedalism
Via Plasma Balls:
Matter Absorption
Energy Absorption'''),
    'walkatrout': Alien('Walkatrout', 'Ickthyperambuloid', 'Gilli-Perambulous Promenade',
                        'https://static.wikia.nocookie.net/ben10/images/a/a8/20211.png/revision/latest/scale-to-width-down/310?cb=20200522085205', '''
Slippery Body
Enhanced Agility
Enhanced Acrobatics
Enhanced Durability
Strong Tail
Underwater Breathing
Enhanced Dexterity
Corruptura Immunity'''),
    'peskydust': Alien("Pesky Dust", 'Nemuina', 'Nemunimos IV',
                       'https://static.wikia.nocookie.net/ben10/images/2/24/Pesky_dust.png/revision/latest/scale-to-width-down/230?cb=20190612103548', '''
Projectile Sleep Dust
Oneirokinesis
Dream Viewing
Dream Entering
Flight
Enhanced Speed
Enhanced Agility'''),
    'molestache': Alien('Mole-Stache', 'Unknown', 'Unknown',
                        'https://static.wikia.nocookie.net/ben10/images/7/70/Mole-Stache_official.png/revision/latest/scale-to-width-down/269?cb=20200603082802', '''
Comakinesis
Mustache Reshaping
Mustache Regeneration
Mustache Flotation
Comakinetic Flight
Skilled Hand-to-Hand Combatant
Enhanced Strength
Enhanced Digging'''),
    'theworst': Alien('The Worst', 'Atrocian', 'Atrocius 0',
                      'https://static.wikia.nocookie.net/ben10/images/8/8a/OmniverseTheWorst.png/revision/latest/scale-to-width-down/250?cb=20131123233550', '''
Indestructibility
Enhanced Durability
Heat Resistance
Acid Immunity'''),
    'kickinhawk': Alien('Kickin Hawk', 'Unknown', 'Unknown',
                        'https://static.wikia.nocookie.net/ben10/images/4/4b/Kicken_Hawk_Omniverse_official.png/revision/latest/scale-to-width-down/287?cb=20140722163036', '''
Strong Powerful Legs
Skilled Hand-to-Hand Combatant
Enhanced Kicking
Enhanced Strength
Enhanced Durability
Enhanced Dexterity
Enhanced Speed
Enhanced Agility
Enhanced Acrobatics
Enhanced Reflexes
Enhanced Jumping
Enhanced Flexibility
Sharp Retractable Talons
Prehensile/Sharp Feet
Sharp Elbow Blades
Shock Waves
Limited Space Survivability'''),
    'toepick': Alien('Toepick', 'Unknown', 'Unknown',
                     'https://static.wikia.nocookie.net/ben10/images/0/0d/Toepick_art.png/revision/latest/scale-to-width-down/310?cb=20141226163903', '''
Nightmarish Face
Nightmarish Sounds
Acid Generation
Gas Generation
Sharp Claws
Enhanced Strength
Enhanced Durability (Helmet only)'''),
    'astrodactyl': Alien('Astrodactyl', 'Unknown', 'Terradino',
                         'https://static.wikia.nocookie.net/ben10/images/a/a2/Astrodactyl_Wings.png/revision/latest/scale-to-width-down/310?cb=20200522084519', '''
Flight (via Jetpack)
Retractable Wings
Propulsion Blast
Energy Weaponry
Energy Whips
Energy Breath
Energy Shockwaves
Internal Star Power
Star Weaponry
Space Survivability
Enhanced Speed (via Flight)
Enhanced Agility
Enhanced Strength
Enhanced Durability
Gas Immunity
Sharp Claws
Sharp/Prehensile Feet'''),
    'bullfrag': Alien('Bullfrag', 'Incursean', 'Unknown',
                      'https://static.wikia.nocookie.net/ben10/images/2/26/Bullfrag_OV_4.png/revision/latest/scale-to-width-down/230?cb=20141129043410', '''
Long Prehensile Tongue
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Smelling
Enhanced Reflexes
Enhanced Jumping
Chest Inflation
Limited Space Survivability'''),
    'atomix': Alien('Atomix', 'Unknown', 'Unknown',
                    'https://static.wikia.nocookie.net/ben10/images/c/c5/OmniverseAtomix.png/revision/latest/scale-to-width-down/271?cb=20200601012256', '''
Atomkinesis
Nucleokinesis
Radiokinesis
Ergokinesis
Photokinesis
Chemical Generation
Heat Generation
Space Survivability
Flight
Jet Feet
Sharp Shoulder Blades
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Speed (via Flight)'''),
    'gutrot': Alien('Gutrot', 'Unknown', 'Unknown',
                    'https://static.wikia.nocookie.net/ben10/images/e/eb/Gutrot_official.png/revision/latest/scale-to-width-down/310?cb=20141129043754', '''
Chemokinesis
Benzinikinesis
Gas Absorption
Gas Immunity
Gas Neutralization
Chemical Reaction Creation
Chemical Repository
Nemuina Sleep Dust Immunity
Enhanced Intelligence
Enhanced Jumping
Vast Chemistry Knowledge
Space Survivability'''),
    'whampire': Alien('Whampier', 'Vladat', 'Anur Vladias',
                      'https://static.wikia.nocookie.net/ben10/images/7/7a/Whampire_facebook_profileT.png/revision/latest/scale-to-width-down/196?cb=20171022040815', '''
Hypnosis
Hypnosis Resistance
Corruptura Projectiles
Energy Absorption
Life Force Draining
Sonic Explosions
Space Survivability
Smoke Mimicry
Bat Transformation
Flight
Infrared Vision
Night Vision
Sharp Fangs
Sharp Claws
Prehensile Feet
Quadrupedalism
Enhanced Strength
Enhanced Durability
Enhanced Agility
Enhanced Reflexes
Enhanced Speed (via Flight and/or Quadrupedalism)
Enhanced Stamina
Enhanced Jumping''')
}
