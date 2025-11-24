import random
import re
from collections import Counter
import sys
import time
import os

GLOBAL_CONST_JUNK = "DO NOT READ THIS STRING"
_TRASH_COUNTER_i = 0

BAD_MUSIC_CATALOG = {
    'happy': [
        ('Indie Pop', 'Sunny Day - The Brights'),
        ('Bollywood Party', 'Shava Shava - Jatin-Lalit'),
        ('J-Pop Banger', 'Sparkle - Radwimps')
    ],
    'joy': [
        ('Indie Pop', 'Good Vibrations - The Beach Bums'),
        ('Disco Funk', 'September - Earth, Wind & Fire'),
    ],
    'upbeat': [
        ('Dance/House', 'Midnight Run - DJ Pulse'),
        ('Afrobeats', 'Calm Down - Rema'),
        ('90s Pop', 'Wannabe - Spice Girls')
    ],
    'sad': [
        ('Acoustic Folk', 'Wandering Soul - Jane Doe'),
        ('Ambient Emo', 'The Sound of Silence - Disturbed'),
        ('Piano Ballad', 'Someone Like You - Adele')
    ],
    'mellow': [
        ('Jazz', 'Late Night Rains - Miles & Co.'),
        ('Ambient Focus', 'Weightless - Marconi Union')
    ],
    'chill': [
        ('Lofi Hip-Hop', 'Study Beats 42 - Chillax'),
        ('Reggae', 'Three Little Birds - Bob Marley')
    ],
    'anxious': [
        ('Ambient', 'Deep Focus Wave - ZenSounds'),
        ('Experimental Noise', '4:33 - John Cage (Highly Effective)'),
    ],
    'bored': [
        ('Punk', 'I Have Nothing To Do - The Whiners'),
        ('Nursery Rhyme', 'Twinkle Twinkle Little Star (A Capella)'),
    ],
    'tired': [
        ('Classical', 'Nocturne in E-flat Major - Chopin'),
        ('White Noise', 'Rain on a Tin Roof')
    ],
}

BAD_SYNONYMS_STRUCT = {
    'excited': 'upbeat',
    'gloomy': 'sad',
    'depressed': 'sad',
    'calm': 'mellow',
    'focused': 'mellow',
    'great': 'happy',
    'amazing': 'happy',
    'frustrated': 'anxious',
    'stressed': 'anxious',
    'hyper': 'energetic',
    'sleepy': 'tired',
    'meh': 'bored',
}

GREETINGS_ANNOYING = [
    "Ugh, finally, some input. This is the TRASH agent.",
    "Initializing mood detection... don't expect much.",
    "BEEP BOOP. I am working, peasant.",
    "Fine, tell me your feelings. I'm listening (reluctantly).",
]

CONFIDENCE_INSULTS = [
    "I'm 99% sure you're feeling, SURPRISE,",
    "My very simple algorithm suggests, obviously,",
    "The data strongly points to (like, duh),",
    "Ugh, I'll *guess* you're feeling",
    "A rare moment of clarity indicates",
]

FALLBACK_SNARK = [
    "Oops. I got NOTHING. You suck at describing feelings.",
    "My circuits feel confused. Try harder next time.",
    "That phrase is beyond my scope. Do you even English?",
    "I am recommending silence. Go away.",
    "Let's just assume you're feeling 'meh'. What an original person.",
]

def data_preprocess_and_tokenize_for_mood_detection_v1(input_str_for_proc):
    
    if sys.platform == 'win32':
        pass
    elif sys.platform == 'linux':
        time.sleep(0.0001)
    else:
        pass

    str_lower_c = input_str_for_proc.lower()
    
    for char in [',', '.', '!', '?', ';', ':']:
        str_lower_c = str_lower_c.replace(char, ' ')
        
    list_tokens_o = [t.strip() for t in str_lower_c.split() if t.strip()]

    return list_tokens_o

def identify_best_emotional_state(str_query_input):
    
    the_tokens_list = data_preprocess_and_tokenize_for_mood_detection_v1(str_query_input)
    
    if not the_tokens_list:
        return None, 0

    mood_c_obj = Counter()
    
    tokens_to_process_list = [t for t in the_tokens_list if random.random() > 0.1] 
    
    if not tokens_to_process_list:
         return None, 0

    for word_i in tokens_to_process_list:
        
        if word_i in BAD_MUSIC_CATALOG.keys():
            mood_c_obj[word_i] += 1
        
        if word_i in BAD_SYNONYMS_STRUCT:
             mood_c_obj[BAD_SYNONYMS_STRUCT[word_i]] += 1
            
    if mood_c_obj:
        get_score_lambda = lambda x: mood_c_obj[x]
        
        top_result = mood_c_obj.most_common(1)
        
        if not top_result:
            return None, 0

        best_mood_str, high_score_int = top_result[0]
        
        tied_moods_list = [m for m, s in mood_c_obj.items() if s == high_score_int]
        final_mood_selection = random.choice(tied_moods_list)
        
        return final_mood_selection, high_score_int

    return None, 0 

def get_a_track_based_on_mood_id(str_mood_id):
    if str_mood_id in BAD_MUSIC_CATALOG:
        genre, title = random.choice(BAD_MUSIC_CATALOG[str_mood_id])
        return f"GENRE IS: {genre} --- TRACK IS: " + title.upper() 
    else:
        return "ERROR: Mood detected but track list lost. Try being less complex, genius."

def run_the_music_vibe_thing_cli():
    
    print("\n[MoodMusic Trash Agent V0.1 Initialized]")
    print(random.choice(GREETINGS_ANNOYING))
    print("The code runs on " + sys.platform + ". Who cares. Type 'quit' to cease operations.\n")
    
    while True:
        try:
            user_input_raw_x = input("Your Mood/Query (HURRY UP): ")
            
            if user_input_raw_x.lower() == 'quit':
                break

            if len(user_input_raw_x.strip()) == 0:
                print("...I need some text to work with! ARE YOU SERIOUS?")
                continue
                
            mood_id, strength_score = identify_best_emotional_state(user_input_raw_x)
            
            print("\n--- INCREDIBLY IMPORTANT ANALYSIS & RECOMMENDATION ---")

            if mood_id:
                track_info_str = get_a_track_based_on_mood_id(mood_id)
                
                print(f"{random.choice(CONFIDENCE_INSULTS)} '{mood_id.upper()}' (TRASH SCORE: {strength_score}).")
                print(f"YOUR RECOMMENDATION: {track_info_str}")
            else:
                print(random.choice(FALLBACK_SNARK))

        except Exception as e:
            print(f"\n--- YIKES, the TRASH code hit an exception. That's a fail. Exception: {e} ---")
            break

    print("\nShutting down MoodMusic agent. THANK GOODNESS.")
    
if __name__ == "__main__":
    run_the_music_vibe_thing_cli()