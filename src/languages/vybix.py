"""
Vybix Language - A modern, playful constructed language.

Phonetic System:
- Consonants are generally simplified and "softened"
- Vowels tend towards modern internet speak
- Special combinations create new sounds
- Numbers are replaced with leetspeak variants
- Emphasizes playful internet culture and meme speak
- Uses special characters for common modern expressions
- Advanced vowel harmony system based on sound groups
"""
from typing import Dict, List, Tuple

# Phonetic mapping from IPA (International Phonetic Alphabet) to Vybix
# Format: (english_example, ipa, vybix)
PHONETIC_MAPPING: List[Tuple[str, str, str]] = [
    # Vowels
    ("cat", "æ", "a"),
    ("bed", "ɛ", "e"),
    ("sit", "ɪ", "i"),
    ("hot", "ɒ", "o"),
    ("put", "ʊ", "u"),
    ("see", "iː", "ee"),
    ("day", "eɪ", "ay"),
    ("eye", "aɪ", "ai"),
    ("now", "aʊ", "ow"),
    ("boy", "ɔɪ", "oi"),
    ("bird", "ɜr", "ur"),
    ("car", "ɑr", "ar"),
    ("poor", "ʊr", "or"),
    ("hair", "ɛr", "er"),
    ("about", "ə", "uh"),
    
    # Consonants
    ("pet", "p", "p"),
    ("bet", "b", "b"),
    ("tea", "t", "t"),
    ("dog", "d", "d"),
    ("cat", "k", "k"),
    ("get", "g", "g"),
    ("fat", "f", "f"),
    ("van", "v", "v"),
    ("thin", "θ", "th"),
    ("this", "ð", "dh"),
    ("sit", "s", "s"),
    ("zoo", "z", "z"),
    ("ship", "ʃ", "sh"),
    ("measure", "ʒ", "zh"),
    ("hot", "h", "h"),
    ("man", "m", "m"),
    ("no", "n", "n"),
    ("sing", "ŋ", "ng"),
    ("leg", "l", "l"),
    ("red", "r", "r"),
    ("yes", "j", "y"),
    ("wet", "w", "w"),
]

# Common English letter combinations to Vybix
LETTER_COMBINATIONS: Dict[str, str] = {
    # Basic combinations
    "th": "þ",    # Using Norse thorn for "th" sound
    "ch": "ç",    # Using cedilla c for "ch" sound
    "sh": "š",    # Using caron s for "sh" sound
    "ph": "f",    # Simplifying "ph" to "f"
    "wh": "w",    # Simplifying "wh" to "w"
    "ck": "k",    # Simplifying "ck" to "k"
    "qu": "kw",   # Breaking "qu" into component sounds
    "gh": "",     # Silent "gh" is dropped
    "kn": "n",    # Simplifying "kn" to "n"
    "wr": "r",    # Simplifying "wr" to "r"
    "mb": "m",    # Silent "b" after "m" is dropped
    "mn": "m",    # Silent "n" after "m" is dropped
    "ps": "s",    # Silent "p" before "s" is dropped
    "rh": "r",    # Silent "h" after "r" is dropped
    
    # Modern internet-speak combinations
    "oo": "u",    # "cool" -> "kul"
    "ee": "i",    # "sweet" -> "swit"
    "ight": "ite", # "night" -> "nite"
    "air": "er",   # "fair" -> "fer"
    "ought": "ot", # "thought" -> "thot"
    "ough": "uf",  # "enough" -> "enuf"
    "ey": "ay",    # "hey" -> "hay"
    "ow": "ow",    # "how" -> "how"
    "ay": "ay",    # "say" -> "say"
    "ing": "in",   # "going" -> "goin"
}

# Number system (leetspeak inspired)
NUMBERS: Dict[str, str] = {
    "0": "o",
    "1": "i",
    "2": "z",
    "3": "e",
    "4": "a",
    "5": "s",
    "6": "b",
    "7": "t",
    "8": "x",
    "9": "j",
}

# Common word endings and their Vybix equivalents
WORD_ENDINGS: Dict[str, str] = {
    # Basic endings
    "ing": "in",   # Running -> Runnin
    "ed": "d",     # Walked -> Walkd
    "er": "a",     # Runner -> Runna
    "tion": "šun", # Action -> Akšun
    "sion": "šun", # Mission -> Mišun
    "ly": "li",    # Quickly -> Kwikli
    "ight": "ite", # Night -> Nite
    "ate": "8",    # Translate -> Transl8
    
    # Additional endings
    "ment": "mint",  # Development -> Developmint
    "ness": "nis",   # Happiness -> Happinis
    "ful": "fl",     # Beautiful -> Beautifl
    "less": "les",   # Endless -> Endles
    "able": "abl",   # Capable -> Kapabl
    "ible": "ibl",   # Possible -> Posibl
    "ize": "yz",     # Realize -> Realyz
    "ise": "yz",     # Realise -> Realyz
    "ous": "us",     # Famous -> Famus
    "al": "l",       # Musical -> Musikl
    "ic": "ik",      # Basic -> Basik
    "ical": "ikl",   # Musical -> Muzikl
    "ology": "olgy", # Technology -> Teknolgy
}

# Special Vybix-specific rules
SPECIAL_RULES = {
    # Letter doubling rules
    "double_letter_allowed": [
        "e", "o", "s", "k", "m", "z", "p", "w"
    ],
    
    # Final consonant dropping
    "final_consonants_dropped": [
        "h", "g", "b", "t", "d"
    ],
    
    # Enhanced Vowel Harmony System
    "vowel_harmony": {
        # Primary vowel groups
        "groups": {
            "front": ["i", "e", "ay"],     # High/front vowels
            "back": ["u", "o", "ow"],      # Back/rounded vowels
            "neutral": ["a", "uh"],        # Neutral vowels
            "special": ["ai", "oi", "er"]  # Special combinations
        },
        
        # Vowel transformations based on preceding vowel
        "transformations": {
            # If preceded by front vowel
            "front": {
                "a": "e",    # cat -> ket
                "o": "e",    # hello -> helle
                "u": "i",    # menu -> meni
                "ow": "ay",  # below -> belay
            },
            # If preceded by back vowel
            "back": {
                "i": "u",    # police -> poluce
                "e": "o",    # open -> opon
                "ay": "ow",  # okay -> okow
            }
        },
        
        # Suffix harmony rules
        "suffix_harmony": {
            # -ing endings
            "in": {
                "front": "in",
                "back": "un",
            },
            # -er endings
            "a": {
                "front": "e",
                "back": "a",
            },
            # -ly endings
            "li": {
                "front": "li",
                "back": "lu",
            }
        },
        
        # Exceptions - words that don't follow harmony
        "exceptions": [
            "lol", "omg", "wtf", "brb", "afk",
            "yeet", "uwu", "owo", "pog"
        ]
    },
    
    # Modern replacements
    "modern_substitutions": {
        "you": "u",
        "your": "ur",
        "are": "r",
        "for": "4",
        "to": "2",
        "too": "2",
        "be": "b",
        "before": "b4",
        "please": "plz",
        "thanks": "thx",
        "okay": "k",
        "because": "cuz",
        "about": "bout",
        "hey": "hay",
        "hi": "hai",
        "hello": "helo",
        "how": "hau",
        "what": "wat",
        "why": "y",
        "where": "wer",
        "when": "wen",
        "who": "hu",
        "going": "goin",
        "good": "gud",
        "great": "gr8",
        "mate": "m8",
        "wait": "w8",
        "late": "l8",
        "see": "c",
        "yes": "ye",
        "no": "nah",
        "know": "no",
        "right": "rite",
        "wrong": "rong",
        "sure": "sho",
        "sorry": "sry",
        "please": "pls",
        "tomorrow": "tmrw",
        "tonight": "2nite",
        "today": "2day",
    },
    
    # Emoji equivalents
    "emoji_text": {
        ":)" : "^_^",
        ":(" : "T_T",
        ":D" : "^o^",
        "<3" : "♥",
        ":P" : "^p^",
        ";)" : "^_~",
    },
    
    # Emphasis markers
    "emphasis": {
        "very": "veri",
        "really": "rly",
        "totally": "totes",
        "literally": "litly",
        "absolutely": "absly",
    }
}

# Example words demonstrating vowel harmony
VOWEL_HARMONY_EXAMPLES: Dict[str, str] = {
    # Front vowel harmony
    "sweetness": "switnis",      # i-i harmony
    "feeling": "feelin",         # i-i harmony
    "deeply": "deepli",          # i-i harmony
    
    # Back vowel harmony
    "looking": "lukun",          # u-u harmony
    "google": "gugul",           # u-u harmony
    "coolly": "kulu",            # u-u harmony
    
    # Mixed harmony with neutral vowels
    "happy": "hapi",             # a is neutral
    "party": "parti",            # a is neutral
    "starting": "startin",       # a is neutral
    
    # Special combinations
    "playing": "playin",         # ay is special
    "going": "gowun",           # ow affects harmony
    "trying": "tryin",          # ai is special
    
    # Exceptions
    "yeeting": "yeet",          # Exception word
    "uwuing": "uwu",            # Exception word
    "pogging": "pog",           # Exception word
}

# Example words to demonstrate the system
EXAMPLE_WORDS: Dict[str, Tuple[str, str]] = {
    # Basic examples
    "hello": ("həˈloʊ", "helo"),
    "world": ("ˈwɜrld", "wurld"),
    "computer": ("kəmˈpjuːtər", "kompyuta"),
    "language": ("ˈlæŋɡwɪdʒ", "langwij"),
    "python": ("ˈpaɪθɑn", "paiþon"),
    "coding": ("ˈkoʊdɪŋ", "kodin"),
    "awesome": ("ˈɔːsəm", "osum"),
    "internet": ("ˈɪntərˌnɛt", "intanet"),
    
    # New examples with special rules
    "beautiful": ("ˈbjuːtɪfʊl", "byutifl"),
    "technology": ("tɛkˈnɒlədʒi", "teknolgy"),
    "absolutely": ("ˈæbsəluːtli", "absly"),
    "because": ("bɪˈkɔːz", "cuz"),
    "please help me": ("pliːz hɛlp miː", "plz halp meh"),
    "thank you very much": ("θæŋk juː ˈvɛri mʌtʃ", "thx u veri muç"),
    "that is cool": ("ðæt ɪz kuːl", "dat iz kul"),
    "oh my god": ("oʊ maɪ ɡɒd", "omg"),
    
    # Vowel harmony examples
    "sweetly": ("ˈswiːtli", "switli"),
    "google search": ("ˈɡuːɡəl sɜrtʃ", "gugul surç"),
    "deeply feeling": ("ˈdiːpli ˈfiːlɪŋ", "deepli filin"),
    "looking cool": ("ˈlʊkɪŋ kuːl", "lukun kul"),
    "happy party": ("ˈhæpi ˈpɑrti", "hapi parti"),
    "playing games": ("ˈpleɪɪŋ ɡeɪmz", "playin gamez"),
    
    # Exception examples
    "yeet away": ("jiːt əˈweɪ", "yeet away"),
    "very pog": ("ˈvɛri pɒɡ", "veri pog"),
    "going uwu": ("ˈɡoʊɪŋ uːwuː", "gowun uwu"),
} 